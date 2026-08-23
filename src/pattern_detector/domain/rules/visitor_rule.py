"""Visitor Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class VisitorPatternRule(BasePatternRule):
    """Detects Visitor / Tree Traversal Walker pattern instances in Clojure.

    Indicators:
    - Multimethods named `visit`, `accept`, `walk-*`, `transform-node` dispatching on node/type tags.
    - Protocols defining `accept` or `visit` methods for element hierarchies.
    - Functions using `clojure.walk` (postwalk, prewalk) to apply visitors across heterogeneous tree structures.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.VISITOR

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Multimethod Visitors (e.g. defmulti visit :type / :tag)
        for ns in model.namespaces.values():
            for mm_name, methods in ns.multimethods.items():
                name_lower = mm_name.lower()
                is_visitor_named = any(k in name_lower for k in ("visit", "walk-", "transform-node", "traverse-"))

                has_tag_dispatch = bool(methods and methods[0].dispatch_fn and any(k in methods[0].dispatch_fn for k in (":type", ":tag", ":op", "class")))
                if is_visitor_named or (has_tag_dispatch and len(methods) >= 2):
                    evidences: list[Evidence] = []
                    related_locs: list[SourceLocation] = []

                    primary_fn = methods[0]
                    evidences.append(
                        self.evidence(
                            description=f"Visitor multimethod '{mm_name}' traverses element hierarchy with polymorphic dispatch",
                            weight=0.55,
                            location=primary_fn.location,
                            code_suffix="VISITOR_MULTIMETHOD",
                        )
                    )

                    branches = [m.dispatch_val for m in methods if m.dispatch_val]
                    if len(branches) >= 2:
                        evidences.append(
                            self.evidence(
                                description=f"Implements {len(branches)} node type visitor branches: {', '.join(branches[:5])}",
                                weight=min(0.50, 0.25 + 0.08 * len(branches)),
                                location=primary_fn.location,
                                code_suffix="VISITOR_BRANCHES",
                            )
                        )
                        for m in methods:
                            related_locs.append(m.location)

                    detections.append(
                        self.create_detection(
                            target_name=mm_name,
                            target_kind="visitor_multimethod",
                            evidences=evidences,
                            primary_location=primary_fn.location,
                            related_locations=related_locs,
                            summary=f"Visitor pattern: multimethod '{mm_name}' visits and transforms {len(branches)} node element types",
                            base_score=0.25,
                        )
                    )

        # 2. Tree Walk Visitor Functions using clojure.walk
        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue
            has_walk = any(w in fn.calls for w in ("postwalk", "prewalk", "walk", "clojure.walk/postwalk", "clojure.walk/prewalk"))
            if has_walk and any(k in fn.name.lower() for k in ("walk", "visit", "transform", "rewrite")):
                evidences = [
                    self.evidence(
                        description=f"Function '{fn.name}' walks and transforms tree structures using clojure.walk visitor traversal",
                        weight=0.60,
                        location=fn.location,
                        code_suffix="CLOJURE_WALK_VISITOR",
                    ),
                ]
                detections.append(
                    self.create_detection(
                        target_name=fn.name,
                        target_kind="tree_walker_fn",
                        evidences=evidences,
                        primary_location=fn.location,
                        related_locations=[],
                        summary=f"Visitor pattern: '{fn.name}' applies visitor function over hierarchical tree structure",
                        base_score=0.25,
                    )
                )

        return detections

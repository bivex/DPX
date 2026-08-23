"""Strategy / Polymorphic Dispatch Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class StrategyPatternRule(BasePatternRule):
    """Detects Strategy Pattern instances in Clojure.

    Indicators:
    - `defmulti` dispatch function combined with 2+ `defmethod` algorithm implementations.
    - Protocols implemented by 2+ distinct records or extended types (Polymorphic Strategy).
    - Higher-order functions accepting explicit strategy/algorithm callbacks.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.STRATEGY

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Strategy via Multimethods (defmulti + defmethod branches)
        for ns in model.namespaces.values():
            for mm_name, methods in ns.multimethods.items():
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                # Find the defmulti declaration
                defmulti_fn = next((m for m in methods if not m.dispatch_val), None)
                if defmulti_fn:
                    evidences.append(
                        self.evidence(
                            description=f"Multimethod dispatch definition '(defmulti {mm_name} {defmulti_fn.dispatch_fn or '...'})'",
                            weight=0.50,
                            location=defmulti_fn.location,
                            code_suffix="MULTIMETHOD_DECLARATION",
                        )
                    )
                    primary_loc = defmulti_fn.location
                else:
                    primary_loc = methods[0].location if methods else SourceLocation(file_path=ns.file_path, line=1)

                branches = [m for m in methods if m.dispatch_val is not None]
                if branches:
                    branch_count = len(branches)
                    evidences.append(
                        self.evidence(
                            description=f"Found {branch_count} distinct interchangeable strategy branches (defmethod): {', '.join(b.dispatch_val or '' for b in branches[:5])}",
                            weight=min(0.45, 0.20 + 0.05 * branch_count),
                            location=branches[0].location,
                            code_suffix="DISPATCH_BRANCHES",
                        )
                    )
                    for b in branches:
                        related_locs.append(b.location)

                detections.append(
                    self.create_detection(
                        target_name=mm_name,
                        target_kind="multimethod_strategy",
                        evidences=evidences,
                        primary_location=primary_loc,
                        related_locations=related_locs,
                        summary=f"Strategy pattern: multimethod '{mm_name}' with {len(branches)} polymorphic dispatch strategies",
                        base_score=0.15,
                    )
                )

        # 2. Strategy via Protocols with multiple implementing records
        for proto in model.all_protocols():
            implementing_records = model.find_records_implementing(proto.name)
            extensions = [ext for ext in model.all_extensions() if ext.protocol_name in (proto.name, proto.qualified_name)]

            total_implementations = len(implementing_records) + len(extensions)
            if total_implementations >= 2:
                evidences = [
                    self.evidence(
                        description=f"Protocol '{proto.name}' defines strategy interface with methods: {', '.join(m.name for m in proto.methods)}",
                        weight=0.45,
                        location=proto.location,
                        code_suffix="PROTOCOL_STRATEGY_INTERFACE",
                    )
                ]
                related_locs = []

                for rec in implementing_records:
                    evidences.append(
                        self.evidence(
                            description=f"Record '{rec.name}' provides concrete strategy implementation for protocol '{proto.name}'",
                            weight=0.25,
                            location=rec.location,
                            code_suffix="RECORD_STRATEGY_IMPL",
                        )
                    )
                    related_locs.append(rec.location)

                for ext in extensions:
                    evidences.append(
                        self.evidence(
                            description=f"Extension on '{ext.target_type}' implements strategy protocol '{proto.name}'",
                            weight=0.20,
                            location=ext.location,
                            code_suffix="EXTENSION_STRATEGY_IMPL",
                        )
                    )
                    related_locs.append(ext.location)

                detections.append(
                    self.create_detection(
                        target_name=proto.name,
                        target_kind="protocol_strategy",
                        evidences=evidences,
                        primary_location=proto.location,
                        related_locations=related_locs,
                        summary=f"Strategy pattern: protocol '{proto.name}' with {total_implementations} interchangeable concrete implementations",
                        base_score=0.20,
                    )
                )

        return detections

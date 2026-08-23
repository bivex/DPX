"""Iterator Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import PatternType


class IteratorPatternRule(BasePatternRule):
    """Detects Iterator / Lazy Sequence Generator pattern instances in Clojure.

    Indicators:
    - Functions building lazy stream iterators using `lazy-seq` and recursion.
    - Protocols defining `next`, `has-next?`, `current`, or `iterate`.
    - Extensions to `clojure.lang.Seqable` or `java.lang.Iterable`.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ITERATOR

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Custom Lazy-Seq Iterator Functions
        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue
            has_lazy_seq = "lazy-seq" in fn.calls or "lazy-seq" in fn.body_text or "(lazy-seq" in fn.body_text
            is_seq_named = fn.name.endswith(("-seq", "_seq", "-stream", "_stream", "-iterator", "_iterator"))

            if has_lazy_seq:
                evidences = [
                    self.evidence(
                        description=f"Function '{fn.name}' generates lazy sequence stream iterator via (lazy-seq ...)",
                        weight=0.60,
                        location=fn.location,
                        code_suffix="LAZY_SEQ_GENERATOR",
                    ),
                ]
                if is_seq_named:
                    evidences.append(
                        self.evidence(
                            description=f"Follows sequence generator naming convention: '{fn.name}'",
                            weight=0.30,
                            location=fn.location,
                            code_suffix="ITERATOR_NAMING",
                        )
                    )
                # Check recursive self invocation
                if fn.name in fn.calls:
                    evidences.append(
                        self.evidence(
                            description="Uses recursive stream expansion to produce sequential element generator",
                            weight=0.25,
                            location=fn.location,
                            code_suffix="RECURSIVE_STREAM",
                        )
                    )

                detections.append(
                    self.create_detection(
                        target_name=fn.name,
                        target_kind="lazy_seq_iterator",
                        evidences=evidences,
                        primary_location=fn.location,
                        related_locations=[],
                        summary=f"Iterator pattern: '{fn.name}' provides lazy sequential traversal over elements",
                        base_score=0.25,
                    )
                )

        # 2. Iterator / Iterable Protocols
        for proto in model.all_protocols():
            methods_lower = [m.name.lower() for m in proto.methods]
            is_iter_proto = any(m in ("next", "has-next?", "has_next", "current", "peek") for m in methods_lower)
            if is_iter_proto or "iterator" in proto.name.lower() or "iterable" in proto.name.lower():
                evidences = [
                    self.evidence(
                        description=f"Protocol '{proto.name}' defines iterator traversal methods: {', '.join(m.name for m in proto.methods)}",
                        weight=0.65,
                        location=proto.location,
                        code_suffix="ITERATOR_PROTOCOL",
                    ),
                ]
                detections.append(
                    self.create_detection(
                        target_name=proto.name,
                        target_kind="iterator_protocol",
                        evidences=evidences,
                        primary_location=proto.location,
                        related_locations=[],
                        summary=f"Iterator pattern: protocol '{proto.name}' defines sequential iteration contract",
                        base_score=0.30,
                    )
                )

        return detections

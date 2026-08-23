"""Factory Method / Constructor Helpers Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class FactoryPatternRule(BasePatternRule):
    """Detects Factory Method / Builder / Constructor Helper instances in Clojure.

    Indicators:
    - Dedicated factory functions with prefixes `make-*`, `create-*`, `new-*`, `build-*`.
    - Functions encapsulating construction of records via `->Record` or `map->Record`.
    - Factory functions performing polymorphic object creation based on config parameters.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.FACTORY_METHOD

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        all_record_names = {r.name for r in model.all_records()}
        all_record_constructors = {f"->{r.name}" for r in model.all_records()} | {f"map->{r.name}" for r in model.all_records()}

        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue

            evidences: list[Evidence] = []
            related_locs: list[SourceLocation] = []

            name_lower = fn.name.lower()
            is_factory_name = name_lower.startswith(("make-", "make_", "create-", "create_", "new-", "build-", "construct-"))

            if is_factory_name:
                evidences.append(
                    self.evidence(
                        description=f"Follows factory function naming convention '{fn.name}'",
                        weight=0.35,
                        location=fn.location,
                        code_suffix="FACTORY_NAMING",
                    )
                )

            # Check if it instantiates known records
            instantiated_records = [
                rec for rec in all_record_names
                if f"->{rec}" in fn.calls or f"map->{rec}" in fn.calls or rec in fn.instantiates_types
            ]

            if instantiated_records:
                evidences.append(
                    self.evidence(
                        description=f"Encapsulates instantiation of record(s): {', '.join(instantiated_records)}",
                        weight=0.45,
                        location=fn.location,
                        code_suffix="RECORD_INSTANTIATION",
                    )
                )
                for rec_name in instantiated_records:
                    rec = model.find_record(rec_name) if hasattr(model, "find_record") else None
                    if rec:
                        related_locs.append(rec.location)

            # Check if it calls map-> or -> constructors
            has_record_ctor_call = any(call in all_record_constructors or call.startswith(("->", "map->")) for call in fn.calls)
            if has_record_ctor_call and not instantiated_records:
                evidences.append(
                    self.evidence(
                        description="Invokes record constructor (->Type or map->Type) with default parameters/validation",
                        weight=0.40,
                        location=fn.location,
                        code_suffix="CTOR_INVOCATION",
                    )
                )

            if evidences and (len(evidences) >= 2 or (is_factory_name and (instantiated_records or has_record_ctor_call))):
                detections.append(
                    self.create_detection(
                        target_name=fn.name,
                        target_kind="factory_function",
                        evidences=evidences,
                        primary_location=fn.location,
                        related_locations=related_locs,
                        summary=f"Factory pattern: constructor helper function '{fn.name}' creating structured domain objects",
                        base_score=0.15,
                    )
                )

        return detections

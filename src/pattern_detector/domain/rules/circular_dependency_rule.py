"""Circular Dependency Architectural Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class CircularDependencyRule(BasePatternRule):
    """Detects architectural circular dependencies and import loops between namespaces."""

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.CIRCULAR_DEPENDENCY

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        cycles = model.find_circular_dependencies()

        for cycle in cycles:
            evidences: list[Evidence] = []
            related_locs: list[SourceLocation] = []

            cycle_str = " ➔ ".join(cycle) + f" ➔ {cycle[0]}"

            for i, ns_name in enumerate(cycle):
                next_ns = cycle[(i + 1) % len(cycle)]
                ns = model.get_namespace(ns_name)
                loc = SourceLocation(file_path=ns.file_path, line=1) if ns else SourceLocation(file_path="", line=1)

                evidences.append(
                    self.evidence(
                        description=f"Namespace '{ns_name}' references '{next_ns}' creating part of a circular loop",
                        weight=0.45,
                        location=loc,
                        code_suffix="CYCLE_LINK",
                    )
                )
                related_locs.append(loc)

            primary_ns = model.get_namespace(cycle[0])
            primary_loc = SourceLocation(file_path=primary_ns.file_path, line=1) if primary_ns else SourceLocation(file_path="", line=1)

            detections.append(
                self.create_detection(
                    target_name=" ⇄ ".join(cycle),
                    target_kind="namespace_cycle",
                    evidences=evidences,
                    primary_location=primary_loc,
                    related_locations=related_locs,
                    summary=f"Circular dependency detected between namespaces: {cycle_str}",
                    base_score=0.40,
                )
            )

        return detections

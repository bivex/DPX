"""Abstract Factory Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class AbstractFactoryRule(BasePatternRule):
    """Detects Abstract Factory pattern instances in Clojure.

    Indicators:
    - Protocols defining multiple related factory creation methods (e.g. create-*, make-*, build-*).
    - Records implementing abstract factory protocols to produce families of related components.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ABSTRACT_FACTORY

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for proto in model.all_protocols():
            name_lower = proto.name.lower()
            is_factory_proto = "factory" in name_lower or "builder" in name_lower or "creator" in name_lower

            factory_methods = [
                m for m in proto.methods
                if m.name.lower().startswith(("create-", "make-", "build-", "new-"))
            ]

            if len(factory_methods) >= 2 or (len(factory_methods) >= 1 and is_factory_proto):
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                evidences.append(
                    self.evidence(
                        description=f"Protocol '{proto.name}' defines family of {len(factory_methods)} creation methods: {', '.join(m.name for m in factory_methods)}",
                        weight=min(0.60, 0.35 + 0.10 * len(factory_methods)),
                        location=proto.location,
                        code_suffix="FACTORY_PROTOCOL_METHODS",
                    )
                )

                if is_factory_proto:
                    evidences.append(
                        self.evidence(
                            description=f"Protocol '{proto.name}' follows Abstract Factory naming convention",
                            weight=0.35,
                            location=proto.location,
                            code_suffix="FACTORY_PROTOCOL_NAMING",
                        )
                    )

                implementing_records = model.find_records_implementing(proto.name)
                if implementing_records:
                    evidences.append(
                        self.evidence(
                            description=f"Implemented by {len(implementing_records)} concrete factory record(s): {', '.join(r.name for r in implementing_records)}",
                            weight=min(0.40, 0.20 + 0.10 * len(implementing_records)),
                            location=implementing_records[0].location,
                            code_suffix="CONCRETE_FACTORY_RECORDS",
                        )
                    )
                    for r in implementing_records:
                        related_locs.append(r.location)

                detections.append(
                    self.create_detection(
                        target_name=proto.name,
                        target_kind="abstract_factory_protocol",
                        evidences=evidences,
                        primary_location=proto.location,
                        related_locations=related_locs,
                        summary=f"Abstract Factory: protocol '{proto.name}' declares family of object creation interfaces",
                        base_score=0.30,
                    )
                )

        return detections

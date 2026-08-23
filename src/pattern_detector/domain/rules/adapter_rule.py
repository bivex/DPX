"""Adapter / Protocol Extension Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class AdapterPatternRule(BasePatternRule):
    """Detects Adapter Pattern instances in Clojure.

    Indicators:
    - `extend-type` or `extend-protocol` adapting existing external types/classes to Clojure protocols.
    - Adapter wrapper records encapsulating an existing object and implementing a target protocol.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ADAPTER

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Extensions via extend-type or extend-protocol
        for ext in model.all_extensions():
            evidences: list[Evidence] = []
            related_locs: list[SourceLocation] = []

            evidences.append(
                self.evidence(
                    description=f"Non-intrusive extension adapting type '{ext.target_type}' to protocol '{ext.protocol_name}'",
                    weight=0.65,
                    location=ext.location,
                    code_suffix="EXTERNAL_PROTOCOL_EXTENSION",
                )
            )

            # Check if target_type is standard or external (Java class or core type)
            is_core_or_java = (
                ext.target_type.startswith("java.")
                or ext.target_type.startswith("String")
                or ext.target_type.startswith("Number")
                or ext.target_type.startswith("nil")
                or ext.target_type.startswith("Object")
                or ext.target_type.startswith("clojure.")
                or "." in ext.target_type
            )
            if is_core_or_java:
                evidences.append(
                    self.evidence(
                        description=f"Adapts external/standard host platform type '{ext.target_type}' without modifying source class",
                        weight=0.30,
                        location=ext.location,
                        code_suffix="EXTERNAL_TYPE_ADAPTATION",
                    )
                )

            # Check matching protocol
            proto = model.find_protocol(ext.protocol_name)
            if proto:
                evidences.append(
                    self.evidence(
                        description=f"Provides protocol method implementations: {', '.join(m.name for m in ext.methods)}",
                        weight=0.20,
                        location=proto.location,
                        code_suffix="ADAPTER_METHODS_IMPLEMENTED",
                    )
                )
                related_locs.append(proto.location)

            detections.append(
                self.create_detection(
                    target_name=f"{ext.target_type}->{ext.protocol_name}",
                    target_kind="protocol_adapter",
                    evidences=evidences,
                    primary_location=ext.location,
                    related_locations=related_locs,
                    summary=f"Adapter pattern: adapts type '{ext.target_type}' to protocol '{ext.protocol_name}'",
                    base_score=0.15,
                )
            )

        return detections

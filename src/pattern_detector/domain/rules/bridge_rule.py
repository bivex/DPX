"""Bridge Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import PatternType, SourceLocation


class BridgePatternRule(BasePatternRule):
    """Detects Bridge / Decoupled Abstraction & Implementation pattern instances.

    Indicators:
    - High-level abstraction protocol or record holding an injected implementation driver/engine field.
    - Low-level implementation protocol (e.g. `*Driver`, `*Backend`, `*Engine`, `*Platform`).
    - Delegation from abstraction methods to implementation driver methods.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.BRIDGE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        driver_protos = [
            p for p in model.all_protocols()
            if any(k in p.name.lower() for k in ("driver", "backend", "engine", "platform", "provider", "codec"))
        ]

        for driver_p in driver_protos:
            # Look for abstraction records that hold an implementation driver
            for rec in model.all_records():
                has_driver_field = any(
                    k in f.lower() for f in rec.fields
                    for k in ("driver", "backend", "engine", "impl", "adapter", "provider")
                )
                if has_driver_field:
                    evidences = [
                        self.evidence(
                            description=f"Record '{rec.name}' maintains decoupled bridge reference to implementation driver field: {', '.join([f for f in rec.fields if any(k in f.lower() for k in ('driver', 'backend', 'engine', 'impl'))])}",
                            weight=0.55,
                            location=rec.location,
                            code_suffix="BRIDGE_ABSTRACTION_RECORD",
                        ),
                        self.evidence(
                            description=f"Driver implementation protocol '{driver_p.name}' defines concrete backend interface",
                            weight=0.40,
                            location=driver_p.location,
                            code_suffix="BRIDGE_DRIVER_PROTOCOL",
                        ),
                    ]
                    related_locs: list[SourceLocation] = [driver_p.location]

                    detections.append(
                        self.create_detection(
                            target_name=rec.name,
                            target_kind="bridge_abstraction",
                            evidences=evidences,
                            primary_location=rec.location,
                            related_locations=related_locs,
                            summary=f"Bridge pattern: abstraction record '{rec.name}' decouples domain logic from '{driver_p.name}' backend implementation",
                            base_score=0.30,
                        )
                    )

        return detections

"""Facade Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class FacadePatternRule(BasePatternRule):
    """Detects Facade / API Gateway module pattern instances in Clojure.

    Indicators:
    - Namespaces that require multiple subsystem namespaces and provide simplified unified delegating functions.
    - Functions that purely forward calls to multiple disparate internal namespaces.
    - High-level API entrypoints named `api`, `client`, `gateway`, `facade`, `service`.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.FACADE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for ns in model.namespaces.values():
            name_lower = ns.name.lower()
            is_facade_named = any(k in name_lower for k in (".api", ".client", ".gateway", ".facade", ".service"))

            # Count internal / project subsystem dependencies
            subsystem_calls: dict[str, list[str]] = {}
            for fn in ns.functions.values():
                for call in fn.calls:
                    if "/" in call:
                        prefix = call.split("/")[0]
                        if prefix != ns.name and not prefix.startswith("clojure."):
                            subsystem_calls.setdefault(prefix, []).append(fn.name)

            if len(subsystem_calls) >= 2 or (len(subsystem_calls) >= 1 and is_facade_named and len(ns.functions) >= 2):
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                evidences.append(
                    self.evidence(
                        description=f"Namespace '{ns.name}' delegates calls to {len(subsystem_calls)} distinct subsystems: {', '.join(list(subsystem_calls.keys())[:4])}",
                        weight=min(0.55, 0.25 + 0.10 * len(subsystem_calls)),
                        location=SourceLocation(file_path=ns.file_path, line=1),
                        code_suffix="SUBSYSTEM_DELEGATION",
                    )
                )

                if is_facade_named:
                    evidences.append(
                        self.evidence(
                            description=f"Namespace '{ns.name}' follows API Gateway / Facade naming convention",
                            weight=0.35,
                            location=SourceLocation(file_path=ns.file_path, line=1),
                            code_suffix="FACADE_NAMING",
                        )
                    )

                delegating_fn_count = len({fn for fns in subsystem_calls.values() for fn in fns})
                if delegating_fn_count >= 2:
                    evidences.append(
                        self.evidence(
                            description=f"Provides {delegating_fn_count} simplified unified façade wrapper functions",
                            weight=0.30,
                            location=SourceLocation(file_path=ns.file_path, line=1),
                            code_suffix="UNIFIED_API_FUNCTIONS",
                        )
                    )

                detections.append(
                    self.create_detection(
                        target_name=ns.name,
                        target_kind="facade_namespace",
                        evidences=evidences,
                        primary_location=SourceLocation(file_path=ns.file_path, line=1),
                        related_locations=related_locs,
                        summary=f"Facade pattern: namespace '{ns.name}' provides unified interface over {len(subsystem_calls)} subsystems",
                        base_score=0.25,
                    )
                )

        return detections

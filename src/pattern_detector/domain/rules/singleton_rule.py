"""Singleton Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class SingletonPatternRule(BasePatternRule):
    """Detects Singleton Pattern instances in Clojure.

    Indicators:
    - Use of `defonce` initializing a shared stateful container (atom, ref, agent, delay).
    - Single shared global state instance in a namespace with dedicated accessor functions.
    - Component system singletons (e.g. system map initialized once).
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.SINGLETON

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for state in model.all_states():
            evidences: list[Evidence] = []
            related_locs: list[SourceLocation] = []

            if state.is_once:
                evidences.append(
                    self.evidence(
                        description=f"Global singleton definition using 'defonce' for '{state.name}' ensuring single-instance lifecycle across reloads",
                        weight=0.60,
                        location=state.location,
                        code_suffix="DEFONCE_DECLARATION",
                    )
                )

            if state.kind in ("atom", "ref", "agent"):
                evidences.append(
                    self.evidence(
                        description=f"Holds mutable stateful reference container ({state.kind}) for global singleton state",
                        weight=0.35,
                        location=state.location,
                        code_suffix="STATEFUL_CONTAINER",
                    )
                )
            elif state.kind in ("delay", "promise"):
                evidences.append(
                    self.evidence(
                        description=f"Uses lazy single-evaluation construct ({state.kind}) to memoize singleton instance",
                        weight=0.40,
                        location=state.location,
                        code_suffix="LAZY_SINGLETON",
                    )
                )

            # Check if there are dedicated getter/setter functions in the same namespace accessing this state
            ns = model.get_namespace(state.namespace)
            if ns:
                accessors = [
                    f for f in ns.functions.values()
                    if state.name in f.calls or f"@{state.name}" in f.body_text or f"deref {state.name}" in f.body_text
                ]
                if accessors:
                    evidences.append(
                        self.evidence(
                            description=f"Has {len(accessors)} dedicated accessor/management functions: {', '.join(a.name for a in accessors[:3])}",
                            weight=0.25,
                            location=accessors[0].location,
                            code_suffix="ACCESSOR_FUNCTIONS",
                        )
                    )
                    for a in accessors:
                        related_locs.append(a.location)

            # Check singleton naming hints
            name_lower = state.name.lower()
            if any(hint in name_lower for hint in ("instance", "singleton", "registry", "cache", "pool", "app-state", "system")):
                evidences.append(
                    self.evidence(
                        description=f"Name '{state.name}' suggests shared singleton entity",
                        weight=0.20,
                        location=state.location,
                        code_suffix="SINGLETON_NAMING",
                    )
                )

            if state.is_once or (state.kind in ("atom", "ref") and len(evidences) >= 2):
                detections.append(
                    self.create_detection(
                        target_name=state.name,
                        target_kind="singleton_state",
                        evidences=evidences,
                        primary_location=state.location,
                        related_locations=related_locs,
                        summary=f"Singleton pattern: global state container '{state.name}' initialized via {state.kind or 'def'}",
                        base_score=0.15 if state.is_once else 0.05,
                    )
                )

        return detections

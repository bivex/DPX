"""State / Finite State Machine Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class StatePatternRule(BasePatternRule):
    """Detects State / Finite State Machine (FSM) pattern instances in Clojure.

    Indicators:
    - State transition functions or multimethods named `transition`, `step`, `next-state`, `handle-state`.
    - Multimethods dispatching on composite `[current-state event]` or state keyword.
    - Explicit state machines managing behavior transitions.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.STATE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Multimethod State Machines
        for ns in model.namespaces.values():
            for mm_name, methods in ns.multimethods.items():
                name_lower = mm_name.lower()
                is_state_named = any(k in name_lower for k in ("transition", "fsm", "state-machine", "next-state", "step-state"))

                if is_state_named or (methods and methods[0].dispatch_fn and "state" in methods[0].dispatch_fn.lower()):
                    evidences: list[Evidence] = []
                    related_locs: list[SourceLocation] = []

                    primary_fn = methods[0]
                    evidences.append(
                        self.evidence(
                            description=f"State transition multimethod '{mm_name}' defines behavioral state machine transitions",
                            weight=0.55,
                            location=primary_fn.location,
                            code_suffix="FSM_TRANSITION_MULTIMETHOD",
                        )
                    )

                    branches = [m.dispatch_val for m in methods if m.dispatch_val]
                    if len(branches) >= 2:
                        evidences.append(
                            self.evidence(
                                description=f"Defines {len(branches)} discrete state transition branches: {', '.join(branches[:5])}",
                                weight=min(0.50, 0.25 + 0.08 * len(branches)),
                                location=primary_fn.location,
                                code_suffix="STATE_BRANCHES",
                            )
                        )
                        for m in methods:
                            related_locs.append(m.location)

                    detections.append(
                        self.create_detection(
                            target_name=mm_name,
                            target_kind="state_machine_multimethod",
                            evidences=evidences,
                            primary_location=primary_fn.location,
                            related_locations=related_locs,
                            summary=f"State / FSM pattern: multimethod '{mm_name}' implements state transition logic with {len(branches)} branches",
                            base_score=0.25,
                        )
                    )

        # 2. Pure Transition Functions
        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue
            name_lower = fn.name.lower()
            if name_lower in ("transition", "next-state", "step-state", "process-state-transition"):
                params = [p.lower() for plist in fn.parameter_lists for p in plist]
                has_state_params = any("state" in p for p in params) and any("event" in p or "action" in p or "msg" in p for p in params)
                if has_state_params:
                    evidences = [
                        self.evidence(
                            description=f"Function '{fn.name}' models pure state transition with signature ({', '.join(params)})",
                            weight=0.60,
                            location=fn.location,
                            code_suffix="PURE_STATE_TRANSITION_FN",
                        ),
                    ]
                    detections.append(
                        self.create_detection(
                            target_name=fn.name,
                            target_kind="state_transition_fn",
                            evidences=evidences,
                            primary_location=fn.location,
                            related_locations=[],
                            summary=f"State pattern: pure state transition function '{fn.name}' alters behavior based on state changes",
                            base_score=0.25,
                        )
                    )

        return detections

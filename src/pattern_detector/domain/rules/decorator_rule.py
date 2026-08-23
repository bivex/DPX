"""Decorator / Ring Middleware Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class DecoratorPatternRule(BasePatternRule):
    """Detects Decorator / Middleware Pattern instances in Clojure.

    Indicators:
    - Middleware function returning an inner closure `(fn [req] ...)` wrapping the wrapped handler.
    - Function accepting a `handler` / `app` / `delegate` / `f` argument and invoking it inside its body.
    - Middleware naming convention (`wrap-*` / `with-*`).
    - Handlers composed via `comp`.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.DECORATOR

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for fn in model.all_functions():
            # Skip records/multimethod dispatch branches
            if fn.is_multimethod or fn.parent_multimethod:
                continue

            evidences: list[Evidence] = []
            related_locs: list[SourceLocation] = []

            has_handler_param = False
            handler_param_name = ""
            for params in fn.parameter_lists:
                for p in params:
                    p_lower = p.lower()
                    if p_lower in ("handler", "app", "f", "delegate", "wrapped", "next-handler"):
                        has_handler_param = True
                        handler_param_name = p
                        break
                if has_handler_param:
                    break

            is_wrap_naming = fn.name.startswith("wrap-") or fn.name.startswith("wrap_") or "middleware" in fn.name.lower()

            if has_handler_param:
                evidences.append(
                    self.evidence(
                        description=f"Function accepts a wrapped handler parameter '{handler_param_name}'",
                        weight=0.40,
                        location=fn.location,
                        code_suffix="HANDLER_PARAMETER",
                    )
                )

            if fn.returns_closure:
                evidences.append(
                    self.evidence(
                        description="Function returns an inner closure/function (fn [req ...] ...) decorating execution",
                        weight=0.45,
                        location=fn.location,
                        code_suffix="RETURNS_CLOSURE",
                    )
                )

            if is_wrap_naming:
                evidences.append(
                    self.evidence(
                        description=f"Follows idiomatic Clojure/Ring middleware decorator naming convention '{fn.name}'",
                        weight=0.35,
                        location=fn.location,
                        code_suffix="MIDDLEWARE_NAMING",
                    )
                )

            # Check if function calls handler inside body or composes
            if handler_param_name and handler_param_name in fn.calls:
                evidences.append(
                    self.evidence(
                        description=f"Explicitly delegates execution to the wrapped handler '{handler_param_name}'",
                        weight=0.30,
                        location=fn.location,
                        code_suffix="DELEGATES_TO_HANDLER",
                    )
                )

            if any(call in ("comp", "clojure.core/comp") for call in fn.calls):
                evidences.append(
                    self.evidence(
                        description="Uses function composition (comp) to chain decorator/middleware layers",
                        weight=0.25,
                        location=fn.location,
                        code_suffix="COMP_COMPOSITION",
                    )
                )

            # If evidence is sufficient to consider it a decorator/middleware
            if evidences and (len(evidences) >= 2 or (fn.returns_closure and has_handler_param) or (is_wrap_naming and fn.returns_closure)):
                detections.append(
                    self.create_detection(
                        target_name=fn.name,
                        target_kind="middleware_decorator",
                        evidences=evidences,
                        primary_location=fn.location,
                        related_locations=related_locs,
                        summary=f"Decorator pattern: Ring-style middleware function '{fn.name}' wrapping request handler",
                        base_score=0.10,
                    )
                )

        return detections

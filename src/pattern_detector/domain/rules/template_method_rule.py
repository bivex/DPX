"""Template Method / Resource Bracket Pattern Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


class TemplateMethodRule(BasePatternRule):
    """Detects Template Method / Functional Resource Bracket pattern instances.

    Indicators:
    - Macros or functions named with the `with-*` bracket convention (e.g. with-open, with-connection, with-lock).
    - Functions encapsulating invariant try/finally, acquire/release, or setup/teardown logic around a caller-supplied body/function.
    - Functions taking before/after hooks or wrapping lambda execution.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.TEMPLATE_METHOD

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue

            evidences: list[Evidence] = []
            name_lower = fn.name.lower()

            # 1. Check with-* bracket naming convention
            is_with_naming = name_lower.startswith(("with-", "with_"))
            if is_with_naming:
                evidences.append(
                    self.evidence(
                        description=f"Follows idiomatic Clojure 'with-*' resource bracket template naming: '{fn.name}'",
                        weight=0.50,
                        location=fn.location,
                        code_suffix="WITH_BRACKET_NAMING",
                    )
                )

            # 2. Check if macro wrapping body
            if fn.is_macro and is_with_naming:
                evidences.append(
                    self.evidence(
                        description="Macro encapsulates algorithmic skeleton expanding user-supplied body expressions",
                        weight=0.40,
                        location=fn.location,
                        code_suffix="MACRO_BRACKET",
                    )
                )

            # 3. Check for try/finally, try/catch, or acquire/release in body text
            has_try_finally = "try" in fn.body_text and ("finally" in fn.body_text or "catch" in fn.body_text)
            if has_try_finally:
                evidences.append(
                    self.evidence(
                        description="Encapsulates invariant resource safety skeleton (try/finally or try/catch)",
                        weight=0.45,
                        location=fn.location,
                        code_suffix="TRY_FINALLY_BRACKET",
                    )
                )

            # 4. Check for hook parameters (e.g. before, after, callback, f)
            params = [p.lower() for plist in fn.parameter_lists for p in plist]
            has_hook_param = any(p in ("f", "callback", "handler", "body", "action", "task") for p in params)
            if has_hook_param and (is_with_naming or has_try_finally):
                evidences.append(
                    self.evidence(
                        description=f"Accepts customizable callback parameter ({', '.join([p for p in params if p in ('f', 'callback', 'handler', 'body', 'action', 'task')])}) executed inside template skeleton",
                        weight=0.35,
                        location=fn.location,
                        code_suffix="CALLBACK_PARAMETER",
                    )
                )

            if (is_with_naming and (fn.is_macro or has_try_finally or has_hook_param)) or (has_try_finally and has_hook_param):
                detections.append(
                    self.create_detection(
                        target_name=fn.name,
                        target_kind="template_bracket",
                        evidences=evidences,
                        primary_location=fn.location,
                        related_locations=[],
                        summary=f"Template Method: '{fn.name}' encapsulates invariant algorithm/resource skeleton with customizable execution body",
                        base_score=0.20,
                    )
                )

        return detections

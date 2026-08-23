"""Interpreter Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class InterpreterPatternRule(BasePatternRule):
    """Detects Interpreter / Domain Expression Evaluator pattern instances in Clojure.

    Indicators:
    - Multimethods or recursive functions named `eval-expr`, `evaluate`, `interpret`, `eval-ast`, `exec-rule`.
    - Functions taking an environment / context map and an expression / AST node to interpret.
    - Polymorphic evaluation of grammar language sentences and domain rules.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.INTERPRETER

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Multimethod AST / Expression Interpreters
        for ns in model.namespaces.values():
            for mm_name, methods in ns.multimethods.items():
                name_lower = mm_name.lower()
                is_interp_named = any(k in name_lower for k in ("eval", "interpret", "evaluate", "exec-expr", "eval-ast"))

                if is_interp_named:
                    evidences: list[Evidence] = []
                    related_locs: list[SourceLocation] = []

                    primary_fn = methods[0] if methods else None
                    loc = primary_fn.location if primary_fn else SourceLocation(file_path=ns.file_path, line=1)

                    evidences.append(
                        self.evidence(
                            description=f"Interpreter multimethod '{mm_name}' evaluates domain grammar expressions",
                            weight=0.60,
                            location=loc,
                            code_suffix="INTERPRETER_MULTIMETHOD",
                        )
                    )

                    branches = [m.dispatch_val for m in methods if m.dispatch_val]
                    if len(branches) >= 2:
                        evidences.append(
                            self.evidence(
                                description=f"Defines evaluation rules for {len(branches)} grammar expression terms: {', '.join(branches[:5])}",
                                weight=min(0.50, 0.25 + 0.08 * len(branches)),
                                location=loc,
                                code_suffix="GRAMMAR_TERMS",
                            )
                        )
                        for m in methods:
                            related_locs.append(m.location)

                    detections.append(
                        self.create_detection(
                            target_name=mm_name,
                            target_kind="expression_interpreter",
                            evidences=evidences,
                            primary_location=loc,
                            related_locations=related_locs,
                            summary=f"Interpreter pattern: multimethod '{mm_name}' evaluates domain grammar sentences with {len(branches)} expression rules",
                            base_score=0.30,
                        )
                    )

        # 2. Pure Recursive Evaluator Functions
        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue
            name_lower = fn.name.lower()
            if name_lower in ("eval-expr", "evaluate-expression", "interpret-ast", "eval-rule", "evaluate-rule"):
                params = [p.lower() for plist in fn.parameter_lists for p in plist]
                has_env_or_expr = any("expr" in p or "ast" in p or "env" in p or "ctx" in p for p in params)
                if has_env_or_expr:
                    evidences = [
                        self.evidence(
                            description=f"Function '{fn.name}' acts as recursive sentence interpreter over domain expressions",
                            weight=0.65,
                            location=fn.location,
                            code_suffix="RECURSIVE_EVAL_FN",
                        ),
                    ]
                    detections.append(
                        self.create_detection(
                            target_name=fn.name,
                            target_kind="recursive_interpreter_fn",
                            evidences=evidences,
                            primary_location=fn.location,
                            related_locations=[],
                            summary=f"Interpreter pattern: '{fn.name}' recursively evaluates domain grammar expressions in given context",
                            base_score=0.30,
                        )
                    )

        return detections

"""Builder Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class BuilderPatternRule(BasePatternRule):
    """Detects Builder / Fluent Configuration pattern instances in Clojure.

    Indicators:
    - Sets of functions with prefixes like `with-*`, `set-*`, `add-*` that take a builder/config
      map or record as first parameter and return the updated instance (fluent chaining).
    - Functions named `build-*`, `create-builder`, `new-builder`, or records named `*Builder`, `*Config`.
    - Functions assembling complex entities step-by-step through `assoc`/`update`/`merge`.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.BUILDER

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for ns in model.namespaces.values():
            # Group builder step functions in the namespace
            step_fns = []
            terminal_build_fns = []

            for fn in ns.functions.values():
                name_lower = fn.name.lower()
                if fn.is_multimethod or fn.parent_multimethod:
                    continue

                # Check if it is a terminal build step (e.g. build, build-*, to-*)
                if name_lower.startswith(("build-", "build_")) or name_lower in ("build", "finish-build"):
                    terminal_build_fns.append(fn)

                # Check if it is a builder step function (e.g. with-*, set-*, add-*)
                elif name_lower.startswith(("with-", "set-", "add-", "use-")) and not name_lower.startswith(("with-open", "with-lock", "with-transaction")):
                    # Check if body modifies map/record (assoc, update, merge)
                    has_assoc = any(k in fn.body_text for k in ("assoc", "update", "merge", "assoc-in", "update-in"))
                    params = [p.lower() for plist in fn.parameter_lists for p in plist]
                    has_builder_param = any("builder" in p or "config" in p or "opts" in p or "ctx" in p or p in ("b", "c", "m", "this") for p in params)

                    if has_assoc or has_builder_param:
                        step_fns.append(fn)

            if len(step_fns) >= 2 or (len(step_fns) >= 1 and len(terminal_build_fns) >= 1):
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                evidences.append(
                    self.evidence(
                        description=f"Namespace '{ns.name}' defines {len(step_fns)} fluent configuration step functions: {', '.join(f.name for f in step_fns[:5])}",
                        weight=min(0.60, 0.30 + 0.10 * len(step_fns)),
                        location=step_fns[0].location if step_fns else next(iter(ns.functions.values())).location,
                        code_suffix="BUILDER_STEP_FUNCTIONS",
                    )
                )

                if terminal_build_fns:
                    evidences.append(
                        self.evidence(
                            description=f"Provides terminal build / instantiation function(s): {', '.join(f.name for f in terminal_build_fns)}",
                            weight=0.35,
                            location=terminal_build_fns[0].location,
                            code_suffix="TERMINAL_BUILD_FN",
                        )
                    )
                    for f in terminal_build_fns:
                        related_locs.append(f.location)

                for f in step_fns:
                    related_locs.append(f.location)

                target_name = terminal_build_fns[0].name if terminal_build_fns else step_fns[0].name
                primary_loc = step_fns[0].location if step_fns else terminal_build_fns[0].location

                detections.append(
                    self.create_detection(
                        target_name=target_name,
                        target_kind="builder_dsl",
                        evidences=evidences,
                        primary_location=primary_loc,
                        related_locations=related_locs,
                        summary=f"Builder pattern: fluent builder DSL in namespace '{ns.name}' with {len(step_fns)} configuration steps",
                        base_score=0.30,
                    )
                )

        return detections

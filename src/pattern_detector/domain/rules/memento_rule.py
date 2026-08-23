"""Memento Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class MementoPatternRule(BasePatternRule):
    """Detects Memento / State Snapshot & History pattern instances in Clojure.

    Indicators:
    - Functions named `save-snapshot`, `restore-snapshot`, `create-memento`, `restore-memento`, `checkpoint`, `undo`, `redo`.
    - History atoms or records tracking historical state snapshots.
    - Protocols defining state capture and rollback capabilities.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.MEMENTO

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        for ns in model.namespaces.values():
            memento_fns = []
            for fn in ns.functions.values():
                name_lower = fn.name.lower()
                if any(k in name_lower for k in ("snapshot", "memento", "checkpoint", "undo", "redo", "save-state", "restore-state")):
                    memento_fns.append(fn)

            if len(memento_fns) >= 2 or any("memento" in f.name.lower() or "snapshot" in f.name.lower() for f in memento_fns):
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                evidences.append(
                    self.evidence(
                        description=f"Namespace '{ns.name}' defines {len(memento_fns)} state snapshot/restore functions: {', '.join(f.name for f in memento_fns)}",
                        weight=min(0.65, 0.40 + 0.10 * len(memento_fns)),
                        location=memento_fns[0].location,
                        code_suffix="MEMENTO_SNAPSHOT_FNS",
                    )
                )
                for f in memento_fns:
                    related_locs.append(f.location)

                detections.append(
                    self.create_detection(
                        target_name=memento_fns[0].name,
                        target_kind="memento_history_manager",
                        evidences=evidences,
                        primary_location=memento_fns[0].location,
                        related_locations=related_locs,
                        summary=f"Memento pattern: snapshot & history management in namespace '{ns.name}' ({len(memento_fns)} functions)",
                        base_score=0.30,
                    )
                )

        return detections

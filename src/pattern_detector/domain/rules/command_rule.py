"""Command / CQRS Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType, SourceLocation


class CommandPatternRule(BasePatternRule):
    """Detects Command / CQRS Message Handler pattern instances.

    Indicators:
    - Multimethods dispatching on command/event message keys (:command, :type, :op, :action, :event).
    - Functions named handle-command, execute-command, dispatch-event, process-command.
    - Protocols defining execute / handle with multiple command record implementations.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.COMMAND

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Multimethod Command Handlers
        for ns in model.namespaces.values():
            for mm_name, methods in ns.multimethods.items():
                evidences: list[Evidence] = []
                related_locs: list[SourceLocation] = []

                name_lower = mm_name.lower()
                is_command_named = any(k in name_lower for k in ("command", "cmd", "event", "action", "msg", "message", "dispatch", "handle-"))

                if is_command_named:
                    evidences.append(
                        self.evidence(
                            description=f"Multimethod '{mm_name}' follows command/event dispatcher naming",
                            weight=0.45,
                            location=methods[0].location if methods else SourceLocation(file_path=ns.file_path, line=1),
                            code_suffix="COMMAND_DISPATCHER_NAMING",
                        )
                    )

                # Check dispatch function for keywords like :type, :command, :action, :op
                if methods:
                    primary_fn = methods[0]
                    dispatch_str = primary_fn.dispatch_fn or ""
                    if any(k in dispatch_str for k in (":type", ":command", ":cmd", ":action", ":op", ":event")):
                        evidences.append(
                            self.evidence(
                                description=f"Dispatches command execution based on message discriminant key '{dispatch_str}'",
                                weight=0.55,
                                location=primary_fn.location,
                                code_suffix="COMMAND_DISCRIMINANT_KEY",
                            )
                        )

                    branches = [m.dispatch_val for m in methods if m.dispatch_val]
                    if len(branches) >= 2:
                        evidences.append(
                            self.evidence(
                                description=f"Implements {len(branches)} distinct command handler branches: {', '.join(branches[:5])}",
                                weight=min(0.50, 0.25 + 0.08 * len(branches)),
                                location=primary_fn.location,
                                code_suffix="COMMAND_BRANCHES",
                            )
                        )
                        for m in methods:
                            related_locs.append(m.location)

                if (is_command_named and len(methods) >= 1) or len(evidences) >= 2:
                    primary_loc = methods[0].location if methods else SourceLocation(file_path=ns.file_path, line=1)
                    detections.append(
                        self.create_detection(
                            target_name=mm_name,
                            target_kind="command_handler",
                            evidences=evidences,
                            primary_location=primary_loc,
                            related_locations=related_locs,
                            summary=f"Command / CQRS pattern: multimethod '{mm_name}' handles polymorphic command messages",
                            base_score=0.25,
                        )
                    )

        # 2. Command Protocol Handlers (e.g. protocol with 'execute' / 'handle' and command records)
        for proto in model.all_protocols():
            name_lower = proto.name.lower()
            if any(k in name_lower for k in ("command", "cmd", "action", "executable", "operation")):
                rec_impls = model.find_records_implementing(proto.name)
                if rec_impls:
                    evidences = [
                        self.evidence(
                            description=f"Protocol '{proto.name}' defines Command interface with methods: {', '.join(m.name for m in proto.methods)}",
                            weight=0.50,
                            location=proto.location,
                            code_suffix="COMMAND_PROTOCOL",
                        ),
                    ]
                    for rec in rec_impls:
                        evidences.append(
                            self.evidence(
                                description=f"Record '{rec.name}' encapsulates executable command parameters and behavior",
                                weight=0.30,
                                location=rec.location,
                                code_suffix="COMMAND_RECORD",
                            )
                        )
                    detections.append(
                        self.create_detection(
                            target_name=proto.name,
                            target_kind="command_protocol",
                            evidences=evidences,
                            primary_location=proto.location,
                            related_locations=[r.location for r in rec_impls],
                            summary=f"Command pattern: protocol '{proto.name}' implemented by {len(rec_impls)} command records",
                            base_score=0.30,
                        )
                    )

        return detections

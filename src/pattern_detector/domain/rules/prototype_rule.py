"""Prototype Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import PatternType, SourceLocation


class PrototypePatternRule(BasePatternRule):
    """Detects Prototype / Cloneable Variant pattern instances in Clojure.

    Indicators:
    - Protocols defining `clone`, `copy-with`, `prototype`, `derive-from`.
    - Functions named `clone-*`, `derive-*`, `copy-with-*` copying a prototype instance with override maps.
    - Records implementing prototype/cloning protocols.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.PROTOTYPE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Prototype Protocols
        for proto in model.all_protocols():
            name_lower = proto.name.lower()
            is_proto_named = any(k in name_lower for k in ("prototype", "cloneable", "copiable", "derive"))
            clone_methods = [m for m in proto.methods if m.name.lower() in ("clone", "copy-with", "derive", "duplicate")]

            if is_proto_named or clone_methods:
                evidences = [
                    self.evidence(
                        description=f"Protocol '{proto.name}' defines prototype cloning methods: {', '.join(m.name for m in proto.methods)}",
                        weight=0.55,
                        location=proto.location,
                        code_suffix="PROTOTYPE_PROTOCOL",
                    ),
                ]
                rec_impls = model.find_records_implementing(proto.name)
                related_locs: list[SourceLocation] = []
                if rec_impls:
                    evidences.append(
                        self.evidence(
                            description=f"Implemented by {len(rec_impls)} prototype records: {', '.join(r.name for r in rec_impls)}",
                            weight=0.35,
                            location=rec_impls[0].location,
                            code_suffix="CONCRETE_PROTOTYPES",
                        )
                    )
                    related_locs.extend(r.location for r in rec_impls)

                detections.append(
                    self.create_detection(
                        target_name=proto.name,
                        target_kind="prototype_protocol",
                        evidences=evidences,
                        primary_location=proto.location,
                        related_locations=related_locs,
                        summary=f"Prototype pattern: protocol '{proto.name}' defines instance cloning and derivation interface",
                        base_score=0.30,
                    )
                )

        # 2. Prototype Derivation Functions
        for fn in model.all_functions():
            if fn.is_multimethod or fn.parent_multimethod:
                continue
            name_lower = fn.name.lower()
            if name_lower.startswith(("clone-", "derive-", "copy-with-", "duplicate-")):
                params = [p.lower() for plist in fn.parameter_lists for p in plist]
                has_proto_param = any("proto" in p or "orig" in p or "base" in p or "template" in p or "inst" in p for p in params)
                has_merge = any(k in fn.body_text for k in ("merge", "assoc", "update", "into"))

                if has_proto_param or has_merge:
                    evidences = [
                        self.evidence(
                            description=f"Function '{fn.name}' copies prototype instance applying override parameters",
                            weight=0.60,
                            location=fn.location,
                            code_suffix="PROTOTYPE_DERIVE_FN",
                        ),
                    ]
                    detections.append(
                        self.create_detection(
                            target_name=fn.name,
                            target_kind="prototype_clone_fn",
                            evidences=evidences,
                            primary_location=fn.location,
                            related_locations=[],
                            summary=f"Prototype pattern: '{fn.name}' creates modified variants from prototype templates",
                            base_score=0.25,
                        )
                    )

        return detections

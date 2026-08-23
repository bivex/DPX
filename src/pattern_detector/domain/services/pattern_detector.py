"""Domain Service for coordinating pattern detection rules on a CodeModel."""

from __future__ import annotations

import time
from collections.abc import Sequence

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.rules.base import PatternRule


class PatternDetectorService:
    """Domain service that applies configured pattern rules to a CodeModel."""

    def __init__(self, rules: Sequence[PatternRule] | None = None) -> None:
        self._rules: list[PatternRule] = list(rules) if rules is not None else get_default_rules()

    @property
    def rules(self) -> list[PatternRule]:
        return list(self._rules)

    def add_rule(self, rule: PatternRule) -> None:
        self._rules.append(rule)

    def detect_all(self, model: CodeModel, project_path: str = "") -> DetectionReport:
        """Run all configured detection rules against the CodeModel and build a DetectionReport."""
        start_time = time.perf_counter()
        all_detections: list[Detection] = []

        for rule in self._rules:
            rule_detections = rule.detect(model)
            all_detections.extend(rule_detections)

        elapsed = time.perf_counter() - start_time

        # Sort detections by confidence score descending
        all_detections.sort(key=lambda d: d.confidence.score, reverse=True)

        scanned_files_count = len(model.namespaces)

        return DetectionReport(
            project_path=project_path,
            scanned_files_count=scanned_files_count,
            detections=all_detections,
            elapsed_seconds=elapsed,
        )

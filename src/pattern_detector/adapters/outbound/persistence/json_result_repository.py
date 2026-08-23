"""JSON Persistence Outbound Adapter implementing ResultRepositoryPort."""

from __future__ import annotations

import json
from pathlib import Path

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.ports.outbound import ResultRepositoryPort


class JsonResultRepository(ResultRepositoryPort):
    """Saves detection reports as formatted JSON files."""

    def save(self, report: DetectionReport, destination_path: str) -> None:
        path = Path(destination_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = report.to_dict()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

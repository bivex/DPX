"""Integration tests for ScanningService and Dependency Injection Container."""

import json
import tempfile
from pathlib import Path

from pattern_detector.bootstrap.container import create_container
from pattern_detector.ports.inbound import ScanOptions


def test_scanning_service_end_to_end_on_examples() -> None:
    container = create_container()
    scanner = container.get_scanner()

    examples_dir = str(Path(__file__).parent.parent / "examples" / "clojure_samples")

    with tempfile.TemporaryDirectory() as tmpdir:
        json_out = str(Path(tmpdir) / "report.json")

        options = ScanOptions(
            min_confidence=0.5,
            output_json_path=json_out,
        )

        report = scanner.scan_path(examples_dir, options=options)

        assert report.scanned_files_count >= 4
        assert report.total_detections_count >= 5

        # Check JSON output persistence
        assert Path(json_out).exists()
        with open(json_out, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data["scanned_files_count"] >= 4
            assert len(data["detections"]) >= 5


def test_scanning_service_filter_by_pattern_type() -> None:
    container = create_container()
    scanner = container.get_scanner()

    examples_dir = str(Path(__file__).parent.parent / "examples" / "clojure_samples")

    options = ScanOptions(
        enabled_patterns=["strategy"],
    )

    report = scanner.scan_path(examples_dir, options=options)
    assert all(d.pattern_type.value == "strategy" for d in report.detections)
    assert report.total_detections_count >= 1

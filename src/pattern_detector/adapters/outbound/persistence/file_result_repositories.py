"""File persistence adapters for HTML and Markdown reports."""

from __future__ import annotations

from pathlib import Path

from pattern_detector.adapters.outbound.persistence.html_report_formatter import HtmlReportFormatter
from pattern_detector.adapters.outbound.persistence.markdown_report_formatter import MarkdownReportFormatter
from pattern_detector.domain.detection import DetectionReport
from pattern_detector.ports.outbound import ResultRepositoryPort


class HtmlResultRepository(ResultRepositoryPort):
    """Saves detection reports as interactive HTML dashboard files."""

    def __init__(self, formatter: HtmlReportFormatter | None = None) -> None:
        self._formatter = formatter or HtmlReportFormatter()

    def save(self, report: DetectionReport, destination_path: str) -> None:
        path = Path(destination_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        content = self._formatter.format(report)
        path.write_text(content, encoding="utf-8")


class MarkdownResultRepository(ResultRepositoryPort):
    """Saves detection reports as Markdown documents."""

    def __init__(self, formatter: MarkdownReportFormatter | None = None) -> None:
        self._formatter = formatter or MarkdownReportFormatter()

    def save(self, report: DetectionReport, destination_path: str) -> None:
        path = Path(destination_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        content = self._formatter.format(report)
        path.write_text(content, encoding="utf-8")

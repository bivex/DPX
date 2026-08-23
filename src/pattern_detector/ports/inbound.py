"""Inbound ports defining how driving adapters (CLI, API) interact with the application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection, DetectionReport


@dataclass
class ScanOptions:
    """Configuration options for a scanning session."""

    min_confidence: float = 0.0
    enabled_patterns: list[str] = field(default_factory=list)
    file_extensions: list[str] = field(default_factory=lambda: [".clj", ".cljs", ".cljc", ".edn"])
    output_json_path: str | None = None
    output_html_path: str | None = None
    output_markdown_path: str | None = None
    verbose: bool = False


class ScannerPort(Protocol):
    """Inbound port for scanning a target path or repository."""

    def scan_path(self, target_path: str, options: ScanOptions | None = None) -> DetectionReport:
        """Scan a path (directory or single file) and return detection report."""
        ...


class DetectorPort(Protocol):
    """Inbound port for detecting patterns directly in an in-memory CodeModel."""

    def detect(self, model: CodeModel) -> list[Detection]:
        """Detect patterns in CodeModel."""
        ...

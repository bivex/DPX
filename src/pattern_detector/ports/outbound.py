"""Outbound ports (Driven Ports) defining external interfaces for Parser, FileSystem, and Persistence."""

from __future__ import annotations

from typing import Protocol

from pattern_detector.domain.code_model import CodeModel, NamespaceModel
from pattern_detector.domain.detection import DetectionReport


class ParserPort(Protocol):
    """Port for converting raw source code text into an agnostic domain CodeModel."""

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        """Parse a single source code file into a NamespaceModel."""
        ...

    def parse_sources(self, sources: dict[str, str]) -> CodeModel:
        """Parse multiple source files into a complete aggregate CodeModel."""
        ...


class SourceProviderPort(Protocol):
    """Port for fetching source code files from a storage medium (filesystem, git, zip, memory)."""

    def get_sources(self, path: str, extensions: list[str] | None = None) -> dict[str, str]:
        """Read and return map of file_path -> source_content."""
        ...


class ResultRepositoryPort(Protocol):
    """Port for persisting detection reports to storage (JSON file, SQLite, database)."""

    def save(self, report: DetectionReport, destination_path: str) -> None:
        """Persist report to destination."""
        ...


class ReportFormatterPort(Protocol):
    """Port for rendering detection reports into visual/textual formats (Console, Markdown, HTML)."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        """Render report to string."""
        ...

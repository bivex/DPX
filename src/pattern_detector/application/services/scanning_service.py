"""Application service coordinating the scanning pipeline."""

from __future__ import annotations

import time

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.ports.inbound import DetectorPort, ScannerPort, ScanOptions
from pattern_detector.ports.outbound import (
    ParserPort,
    ResultRepositoryPort,
    SourceProviderPort,
)


class ScanningService(ScannerPort, DetectorPort):
    """Application Service implementing ScannerPort and DetectorPort.

    Coordinates source fetching, AST/Clojure parsing into CodeModel,
    pattern rule execution, filtering, and persisting results.
    """

    def __init__(
        self,
        source_provider: SourceProviderPort,
        parser: ParserPort,
        detector_service: PatternDetectorService,
        json_repository: ResultRepositoryPort | None = None,
        html_repository: ResultRepositoryPort | None = None,
        markdown_repository: ResultRepositoryPort | None = None,
    ) -> None:
        self._source_provider = source_provider
        self._parser = parser
        self._detector_service = detector_service
        self._json_repository = json_repository
        self._html_repository = html_repository
        self._markdown_repository = markdown_repository

    def detect(self, model: CodeModel) -> list[Detection]:
        """Directly detect patterns in an already constructed CodeModel."""
        report = self._detector_service.detect_all(model)
        return report.detections

    def scan_path(self, target_path: str, options: ScanOptions | None = None) -> DetectionReport:
        """Execute full scan pipeline on given path."""
        start_time = time.perf_counter()
        opts = options or ScanOptions()

        # 1. Fetch sources via Outbound Port
        sources = self._source_provider.get_sources(target_path, extensions=opts.file_extensions)
        if not sources:
            return DetectionReport(
                project_path=target_path,
                scanned_files_count=0,
                detections=[],
                elapsed_seconds=round(time.perf_counter() - start_time, 4),
            )

        # 2. Parse sources into agnostic domain CodeModel via Outbound Port
        code_model = self._parser.parse_sources(sources)

        # 3. Execute domain detection rules
        report = self._detector_service.detect_all(code_model, project_path=target_path)
        total_elapsed = time.perf_counter() - start_time
        report.elapsed_seconds = total_elapsed

        # 4. Filter by confidence or pattern type if requested
        if opts.min_confidence > 0.0 or opts.enabled_patterns:
            filtered: list[Detection] = []
            for d in report.detections:
                if d.confidence.score < opts.min_confidence:
                    continue
                if opts.enabled_patterns and d.pattern_type.value not in opts.enabled_patterns:
                    continue
                filtered.append(d)
            report.detections = filtered

        # 5. Persist to outputs if requested
        if opts.output_json_path and self._json_repository:
            self._json_repository.save(report, opts.output_json_path)

        if opts.output_html_path and self._html_repository:
            self._html_repository.save(report, opts.output_html_path)

        if opts.output_markdown_path and self._markdown_repository:
            self._markdown_repository.save(report, opts.output_markdown_path)

        return report

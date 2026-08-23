"""Bootstrap DI Container / Composition Root."""

from __future__ import annotations

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.adapters.outbound.filesystem import FileSourceProvider
from pattern_detector.adapters.outbound.persistence import (
    ConsoleReportFormatter,
    HtmlReportFormatter,
    HtmlResultRepository,
    JsonResultRepository,
    MarkdownReportFormatter,
    MarkdownResultRepository,
)
from pattern_detector.application.services.scanning_service import ScanningService
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.ports.inbound import ScannerPort
from pattern_detector.ports.outbound import (
    ParserPort,
    ReportFormatterPort,
    ResultRepositoryPort,
    SourceProviderPort,
)


class Container:
    """Dependency Injection Container and Composition Root.

    Instantiates and wires domain services, driven outbound adapters,
    and application use cases adhering to Hexagonal Architecture.
    """

    def __init__(
        self,
        source_provider: SourceProviderPort | None = None,
        parser: ParserPort | None = None,
        json_repository: ResultRepositoryPort | None = None,
        html_repository: ResultRepositoryPort | None = None,
        markdown_repository: ResultRepositoryPort | None = None,
        report_formatter: ReportFormatterPort | None = None,
        html_formatter: ReportFormatterPort | None = None,
        markdown_formatter: ReportFormatterPort | None = None,
        detector_service: PatternDetectorService | None = None,
    ) -> None:
        # Outbound Driven Adapters
        self.source_provider: SourceProviderPort = source_provider or FileSourceProvider()
        self.parser: ParserPort = parser or ClojureAntlrParserAdapter()

        self.html_formatter: ReportFormatterPort = html_formatter or HtmlReportFormatter()
        self.markdown_formatter: ReportFormatterPort = markdown_formatter or MarkdownReportFormatter()
        self.report_formatter: ReportFormatterPort = report_formatter or ConsoleReportFormatter()

        self.json_repository: ResultRepositoryPort = json_repository or JsonResultRepository()
        self.html_repository: ResultRepositoryPort = html_repository or HtmlResultRepository(formatter=self.html_formatter)  # type: ignore[arg-type]
        self.markdown_repository: ResultRepositoryPort = markdown_repository or MarkdownResultRepository(formatter=self.markdown_formatter)  # type: ignore[arg-type]

        # Domain Service & Rules
        self.detector_service: PatternDetectorService = detector_service or PatternDetectorService(rules=get_default_rules())

        # Application Service (Inbound Port implementation)
        self.scanning_service: ScanningService = ScanningService(
            source_provider=self.source_provider,
            parser=self.parser,
            detector_service=self.detector_service,
            json_repository=self.json_repository,
            html_repository=self.html_repository,
            markdown_repository=self.markdown_repository,
        )

    def get_scanner(self) -> ScannerPort:
        return self.scanning_service

    def get_formatter(self) -> ReportFormatterPort:
        return self.report_formatter


def create_container() -> Container:
    """Create a default production container."""
    return Container()

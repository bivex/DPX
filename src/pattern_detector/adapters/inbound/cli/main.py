"""Inbound Driving Adapter: CLI interface using Typer and Rich."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from pattern_detector.bootstrap.container import create_container
from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.ports.inbound import ScanOptions

app = typer.Typer(
    name="pattern-detector",
    help="Hexagonal DDD Pattern Scanner & Detector for Clojure / Functional & OOP code.",
    add_completion=False,
)
console = Console()


@app.command(name="scan")
def scan(
    path: Annotated[
        str,
        typer.Argument(
            help="File or directory path to scan for design patterns.",
        ),
    ] = ".",
    min_confidence: Annotated[
        float,
        typer.Option(
            "--min-confidence",
            "-c",
            help="Minimum confidence threshold (0.0 - 1.0).",
        ),
    ] = 0.0,
    pattern: Annotated[
        list[str] | None,
        typer.Option(
            "--pattern",
            "-p",
            help="Specific pattern types to look for (can be specified multiple times).",
        ),
    ] = None,
    json_output: Annotated[
        str | None,
        typer.Option(
            "--json",
            "-j",
            help="Export results to a JSON file destination.",
        ),
    ] = None,
    html_output: Annotated[
        str | None,
        typer.Option(
            "--html",
            "-H",
            help="Export results to an interactive HTML report dashboard.",
        ),
    ] = None,
    markdown_output: Annotated[
        str | None,
        typer.Option(
            "--markdown",
            "-m",
            help="Export results to a Markdown report file.",
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            "-v",
            help="Enable verbose output.",
        ),
    ] = False,
) -> None:
    """Scan a Clojure source code file or directory for software design patterns."""
    target_path = str(Path(path).resolve())

    container = create_container()
    scanner = container.get_scanner()

    options = ScanOptions(
        min_confidence=min_confidence,
        enabled_patterns=pattern or [],
        output_json_path=json_output,
        output_html_path=html_output,
        output_markdown_path=markdown_output,
        verbose=verbose,
    )

    with console.status(f"[cyan]Scanning [bold]{path}[/bold] using ANTLR parser & Domain Rules...[/cyan]"):
        report = scanner.scan_path(target_path, options=options)

    # Render formatted report to terminal
    container.report_formatter.render_to_console(report, console, verbose=verbose)  # type: ignore[attr-defined]

    if json_output:
        console.print(f"[bold green]✔[/bold green] Full JSON detection report exported to: [underline]{json_output}[/underline]")
    if html_output:
        console.print(f"[bold green]✔[/bold green] Interactive HTML dashboard exported to: [underline]{html_output}[/underline]")
    if markdown_output:
        console.print(f"[bold green]✔[/bold green] Markdown report exported to: [underline]{markdown_output}[/underline]")
    if json_output or html_output or markdown_output:
        console.print()


@app.command(name="rules")
def list_rules() -> None:
    """Display catalog of all registered pattern detection rules and heuristics."""
    table = Table(title="📐 Registered Design Pattern Rules & Heuristics", border_style="bright_blue", show_header=True)
    table.add_column("Pattern Type", style="bold cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Intent & Detection Strategy", style="white")
    table.add_column("Tags", style="dim")

    for p_type, p_def in PATTERN_CATALOG.items():
        tags_str = ", ".join(p_def.tags)
        desc = f"[bold]{p_def.name}[/bold]\n{p_def.description}\n[dim]Intent: {p_def.intent}[/dim]"
        table.add_row(p_type.value, p_def.category.value.upper(), desc, tags_str)

    console.print(table)


@app.command(name="info")
def info() -> None:
    """Display architecture info and supported grammar configurations."""
    info_text = (
        "[bold magenta]Pattern Scanner & Detector (Hexagonal DDD Architecture)[/bold magenta]\n\n"
        "• [bold cyan]Core Domain:[/bold cyan] Agnostic CodeModel, Evidence & Confidence Score Engine, Specification Rules\n"
        "• [bold cyan]Inbound Ports:[/bold cyan] ScannerPort, DetectorPort\n"
        "• [bold cyan]Outbound Ports:[/bold cyan] ParserPort, SourceProviderPort, ResultRepositoryPort, ReportFormatterPort\n"
        "• [bold cyan]Active Grammar Adapter:[/bold cyan] ANTLR 4.13.2 Clojure Grammar (Clojure.g4)\n"
        "• [bold cyan]Supported Extensions:[/bold cyan] .clj, .cljs, .cljc, .edn\n"
    )
    console.print(Panel(info_text, title="ℹ System Info", border_style="cyan"))


def main() -> None:
    app()


if __name__ == "__main__":
    main()

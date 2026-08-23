"""Console Report Formatter implementing ReportFormatterPort with Rich."""

from __future__ import annotations

import io

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.value_objects import ConfidenceLevel
from pattern_detector.ports.outbound import ReportFormatterPort


class ConsoleReportFormatter(ReportFormatterPort):
    """Renders DetectionReport to beautiful terminal output via Rich."""

    def __init__(self) -> None:
        pass

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        string_io = io.StringIO()
        console = Console(file=string_io, force_terminal=True, width=110)
        self.render_to_console(report, console, verbose=verbose)
        return string_io.getvalue()

    def render_to_console(self, report: DetectionReport, console: Console, verbose: bool = False) -> None:
        """Render report directly to rich console."""
        header = Text()
        header.append("🔍 Pattern Scanner & Detector ", style="bold magenta")
        header.append("• Hexagonal DDD Architecture\n", style="italic cyan")
        header.append(f"Scanned: {report.scanned_files_count} file(s) in {report.elapsed_seconds:.3f}s | Found: {report.total_detections_count} pattern instance(s)", style="dim")
        console.print(Panel(header, border_style="bright_blue"))

        if not report.detections:
            console.print("\n[yellow]No design pattern instances detected in the provided source files.[/yellow]\n")
            return

        # 1. Summary Statistics Table
        summary_table = Table(title="📊 Detection Summary by Category", border_style="cyan", show_header=True)
        summary_table.add_column("Pattern Category", style="bold")
        summary_table.add_column("Detections", justify="right", style="cyan")
        summary_table.add_column("Confidence Breakdown", style="dim")

        for cat, count in report.summary_by_category.items():
            if count > 0:
                cat_dets = [d for d in report.detections if d.pattern_category.value == cat]
                vh = sum(1 for d in cat_dets if d.level == ConfidenceLevel.VERY_HIGH)
                h = sum(1 for d in cat_dets if d.level == ConfidenceLevel.HIGH)
                m = sum(1 for d in cat_dets if d.level == ConfidenceLevel.MEDIUM)
                l = sum(1 for d in cat_dets if d.level == ConfidenceLevel.LOW)
                breakdown = f"[green]{vh} VERY HIGH[/], [cyan]{h} HIGH[/], [yellow]{m} MED[/], [red]{l} LOW[/]"
                summary_table.add_row(cat.upper(), str(count), breakdown)

        console.print(summary_table)
        console.print()

        # 2. Detailed Detections Listing
        console.print("[bold underline]📋 Identified Design Patterns:[/bold underline]\n")

        for idx, det in enumerate(report.detections, 1):
            # Badge style based on level
            badge_color = {
                ConfidenceLevel.VERY_HIGH: "bold green",
                ConfidenceLevel.HIGH: "bold cyan",
                ConfidenceLevel.MEDIUM: "bold yellow",
                ConfidenceLevel.LOW: "bold red",
            }.get(det.level, "white")

            conf_str = f"[{badge_color}]{det.confidence.percentage_str} [{det.level.value}][/{badge_color}]"

            title_text = Text()
            title_text.append(f"#{idx} ", style="bold dim")
            title_text.append(f"{det.pattern_type.value.upper()} ", style="bold bright_cyan")
            title_text.append(f"on {det.target_kind} ", style="italic")
            title_text.append(f"'{det.target_name}'", style="bold white")

            tree = Tree(title_text)
            tree.add(f"📍 [bold]Location:[/bold] [underline cyan]{det.primary_location}[/underline cyan]")
            tree.add(f"🎯 [bold]Confidence:[/bold] {conf_str}")
            tree.add(f"📝 [bold]Summary:[/bold] {det.summary}")

            if det.evidences:
                ev_branch = tree.add(f"🔎 [bold]Evidence Trail ({len(det.evidences)} heuristics):[/bold]")
                for ev in det.evidences:
                    weight_pct = int(ev.weight * 100)
                    ev_text = f"[bold green]+{weight_pct}%[/bold green] [dim]({ev.rule_code})[/dim] {ev.description}"
                    if ev.location:
                        ev_text += f" → [cyan]{ev.location}[/cyan]"
                    ev_branch.add(ev_text)

            if det.related_locations:
                rel_branch = tree.add("🔗 [bold]Related Locations:[/bold]")
                for r_loc in det.related_locations:
                    rel_branch.add(f"[underline]{r_loc}[/underline]")

            console.print(tree)
            console.print()

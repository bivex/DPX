"""Markdown Report Formatter implementing ReportFormatterPort."""

from __future__ import annotations

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.value_objects import ConfidenceLevel
from pattern_detector.ports.outbound import ReportFormatterPort


class MarkdownReportFormatter(ReportFormatterPort):
    """Renders DetectionReport to structured GitHub-Flavored Markdown."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        lines: list[str] = [
            "# 🔍 Software Design Pattern Detection Report",
            "",
            f"> **Project:** `{report.project_path or 'Scanned Project'}`  ",
            f"> **Scanned Files:** {report.scanned_files_count}  ",
            f"> **Total Detections:** {report.total_detections_count}  ",
            f"> **Duration:** {report.elapsed_seconds:.3f}s  ",
            "",
            "---",
            "",
            "## 📊 Summary by Category",
            "",
            "| Category | Detections Count |",
            "| :--- | :---: |",
        ]

        for cat, count in report.summary_by_category.items():
            if count > 0:
                lines.append(f"| **{cat.upper()}** | {count} |")

        lines.extend([
            "",
            "---",
            "",
            "## 📋 Identified Design Patterns",
            "",
        ])

        for idx, det in enumerate(report.detections, 1):
            badge = {
                ConfidenceLevel.VERY_HIGH: "🟢 `VERY_HIGH`",
                ConfidenceLevel.HIGH: "🔵 `HIGH`",
                ConfidenceLevel.MEDIUM: "🟡 `MEDIUM`",
                ConfidenceLevel.LOW: "🔴 `LOW`",
            }.get(det.level, "⚪ `UNKNOWN`")

            lines.append(f"### #{idx} {det.pattern_type.value.upper()} on {det.target_kind} `{det.target_name}`")
            lines.append(f"- **Confidence:** {det.confidence.percentage_str} ({badge})")
            lines.append(f"- **Primary Location:** [`{det.primary_location}`]({det.primary_location.file_path})")
            lines.append(f"- **Summary:** {det.summary}")
            lines.append("")
            lines.append("#### 🔎 Evidence Trail:")
            for ev in det.evidences:
                weight_pct = int(ev.weight * 100)
                loc_text = f" _(at `{ev.location}`)_" if ev.location else ""
                lines.append(f"- **+{weight_pct}%** `[{ev.rule_code}]` {ev.description}{loc_text}")

            if det.related_locations:
                lines.append("")
                lines.append("**Related Locations:**")
                for r_loc in det.related_locations:
                    lines.append(f"- [`{r_loc}`]({r_loc.file_path})")

            lines.append("")
            lines.append("---")
            lines.append("")

        return "\n".join(lines)

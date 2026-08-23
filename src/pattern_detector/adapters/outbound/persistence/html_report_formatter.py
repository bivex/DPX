"""HTML Report Formatter implementing ReportFormatterPort."""

from __future__ import annotations

import html

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.value_objects import ConfidenceLevel
from pattern_detector.ports.outbound import ReportFormatterPort


class HtmlReportFormatter(ReportFormatterPort):
    """Renders a standalone, responsive, interactive HTML dashboard for DetectionReport."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        vh_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.VERY_HIGH)
        h_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.HIGH)
        m_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.MEDIUM)
        l_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.LOW)

        cards_html: list[str] = []
        for idx, det in enumerate(report.detections, 1):
            badge_class = {
                ConfidenceLevel.VERY_HIGH: "badge-vh",
                ConfidenceLevel.HIGH: "badge-h",
                ConfidenceLevel.MEDIUM: "badge-m",
                ConfidenceLevel.LOW: "badge-l",
            }.get(det.level, "badge-vh")

            evidences_html: list[str] = []
            for ev in det.evidences:
                pct = int(ev.weight * 100)
                loc_str = f'<span class="location-tag">📍 {html.escape(str(ev.location))}</span>' if ev.location else ""
                evidences_html.append(
                    f'<li class="evidence-item">'
                    f'<span class="weight-tag">+{pct}%</span> '
                    f'<span class="rule-code">[{html.escape(ev.rule_code)}]</span> '
                    f'{html.escape(ev.description)} {loc_str}'
                    f"</li>"
                )

            related_html = ""
            if det.related_locations:
                rel_items = "".join(f"<li><code>{html.escape(str(loc))}</code></li>" for loc in det.related_locations)
                related_html = f'<div class="related-locs"><strong>Related Locations:</strong><ul>{rel_items}</ul></div>'

            cards_html.append(
                f"""
                <div class="pattern-card" data-pattern="{html.escape(det.pattern_type.value)}" data-category="{html.escape(det.pattern_category.value)}" data-target="{html.escape(det.target_name)}">
                    <div class="card-header">
                        <div class="header-left">
                            <span class="card-index">#{idx}</span>
                            <span class="pattern-badge">{html.escape(det.pattern_type.value.upper())}</span>
                            <span class="target-name">{html.escape(det.target_kind)}: <strong>{html.escape(det.target_name)}</strong></span>
                        </div>
                        <span class="confidence-badge {badge_class}">{det.confidence.percentage_str} [{det.level.value}]</span>
                    </div>
                    <div class="card-body">
                        <p class="summary-text"><strong>Summary:</strong> {html.escape(det.summary)}</p>
                        <p class="primary-loc"><strong>Primary Location:</strong> <code>{html.escape(str(det.primary_location))}</code></p>
                        <div class="evidence-section">
                            <strong>Evidence Trail ({len(det.evidences)} heuristics):</strong>
                            <ul class="evidence-list">
                                {"".join(evidences_html)}
                            </ul>
                        </div>
                        {related_html}
                    </div>
                </div>
                """
            )

        category_rows = "".join(
            f"<tr><td><strong>{html.escape(cat.upper())}</strong></td><td>{count}</td></tr>"
            for cat, count in report.summary_by_category.items()
            if count > 0
        )

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pattern Scanner Report - {html.escape(report.project_path or "Codebase")}</title>
    <style>
        :root {{
            --bg: #0d1117;
            --card-bg: #161b22;
            --border: #30363d;
            --text: #c9d1d9;
            --heading: #f0f6fc;
            --accent: #58a6ff;
            --green: #2ea043;
            --cyan: #388bfd;
            --yellow: #d29922;
            --red: #f85149;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace, sans-serif; }}
        body {{ background: var(--bg); color: var(--text); padding: 30px 20px; line-height: 1.5; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        header {{ border-bottom: 1px solid var(--border); padding-bottom: 20px; margin-bottom: 25px; }}
        h1 {{ color: var(--heading); font-size: 26px; display: flex; align-items: center; gap: 10px; }}
        .subtitle {{ color: #8b949e; font-size: 14px; margin-top: 5px; }}
        
        .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 25px; }}
        .kpi-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; padding: 18px; }}
        .kpi-title {{ font-size: 12px; text-transform: uppercase; color: #8b949e; font-weight: 600; }}
        .kpi-value {{ font-size: 28px; font-weight: 700; color: var(--heading); margin-top: 5px; }}

        .search-bar {{ width: 100%; padding: 12px 16px; background: var(--card-bg); border: 1px solid var(--border); border-radius: 6px; color: var(--heading); font-size: 14px; margin-bottom: 20px; outline: none; }}
        .search-bar:focus {{ border-color: var(--accent); }}

        .summary-table {{ width: 100%; border-collapse: collapse; background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 30px; overflow: hidden; }}
        .summary-table th, .summary-table td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border); font-size: 14px; }}
        .summary-table th {{ background: #21262d; color: var(--heading); }}

        .pattern-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 15px; overflow: hidden; transition: border-color 0.2s; }}
        .pattern-card:hover {{ border-color: var(--accent); }}
        .card-header {{ background: #21262d; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid var(--border); }}
        .header-left {{ display: flex; align-items: center; gap: 10px; }}
        .card-index {{ color: #8b949e; font-weight: 700; font-size: 14px; }}
        .pattern-badge {{ background: #1f6feb22; color: #58a6ff; border: 1px solid #1f6feb44; padding: 3px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; }}
        .target-name {{ color: var(--heading); font-size: 14px; }}
        
        .confidence-badge {{ font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; }}
        .badge-vh {{ background: #23863633; color: #3fb950; border: 1px solid #238636; }}
        .badge-h {{ background: #1f6feb33; color: #58a6ff; border: 1px solid #1f6feb; }}
        .badge-m {{ background: #d2992233; color: #e3b341; border: 1px solid #d29922; }}
        .badge-l {{ background: #da363333; color: #f85149; border: 1px solid #da3633; }}

        .card-body {{ padding: 16px 18px; font-size: 13px; }}
        .summary-text {{ margin-bottom: 10px; color: #e6edf3; }}
        .primary-loc {{ margin-bottom: 12px; color: #8b949e; }}
        code {{ background: #111418; padding: 2px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; color: #79c0ff; }}

        .evidence-section {{ margin-top: 12px; }}
        .evidence-list {{ list-style: none; margin-top: 8px; }}
        .evidence-item {{ margin-bottom: 6px; padding-left: 10px; border-left: 2px solid var(--border); }}
        .weight-tag {{ color: #3fb950; font-weight: 700; font-family: monospace; }}
        .rule-code {{ color: #8b949e; font-size: 11px; font-family: monospace; }}
        .location-tag {{ color: #a5d6ff; font-size: 11px; margin-left: 6px; }}
        .related-locs {{ margin-top: 12px; color: #8b949e; }}
        .related-locs ul {{ margin-left: 20px; margin-top: 4px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔍 Software Design Pattern Detection Report</h1>
            <div class="subtitle">Hexagonal DDD Pattern Scanner • Project: <code>{html.escape(report.project_path or "Target Repository")}</code></div>
        </header>

        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-title">Total Detections</div>
                <div class="kpi-value">{report.total_detections_count}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">High Confidence (≥70%)</div>
                <div class="kpi-value" style="color: #3fb950;">{vh_count + h_count}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Med / Low (<70%)</div>
                <div class="kpi-value" style="color: #e3b341;">{m_count + l_count}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Files Scanned</div>
                <div class="kpi-value">{report.scanned_files_count}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Scan Duration</div>
                <div class="kpi-value">{report.elapsed_seconds:.3f}s</div>
            </div>
        </div>

        <input type="text" id="searchInput" class="search-bar" placeholder="🔎 Filter patterns by name, type, target, or keyword (e.g. strategy, middleware, wrap-routes)...">

        <table class="summary-table">
            <thead>
                <tr>
                    <th>Pattern Category</th>
                    <th>Count</th>
                </tr>
            </thead>
            <tbody>
                {category_rows}
            </tbody>
        </table>

        <div id="cardsContainer">
            {"".join(cards_html)}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.pattern-card');

        searchInput.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            cards.forEach(card => {{
                const text = card.textContent.toLowerCase();
                const pattern = card.dataset.pattern || '';
                const category = card.dataset.category || '';
                const target = card.dataset.target || '';
                if (text.includes(query) || pattern.includes(query) || category.includes(query) || target.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>
"""

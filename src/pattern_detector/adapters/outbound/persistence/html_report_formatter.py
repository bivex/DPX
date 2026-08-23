"""HTML Report Formatter implementing ReportFormatterPort."""

from __future__ import annotations

import html

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternCategory, PatternType
from pattern_detector.ports.outbound import ReportFormatterPort

CATEGORY_COLORS: dict[PatternCategory, dict[str, str]] = {
    PatternCategory.CREATIONAL: {
        "text": "#34d399",
        "bg": "#064e3b44",
        "border": "#059669",
        "accent": "#10b981",
        "name": "Creational",
    },
    PatternCategory.STRUCTURAL: {
        "text": "#38bdf8",
        "bg": "#0c4a6e44",
        "border": "#0284c7",
        "accent": "#0ea5e9",
        "name": "Structural",
    },
    PatternCategory.BEHAVIORAL: {
        "text": "#c084fc",
        "bg": "#581c8744",
        "border": "#9333ea",
        "accent": "#a855f7",
        "name": "Behavioral",
    },
    PatternCategory.ARCHITECTURAL: {
        "text": "#fbbf24",
        "bg": "#78350f44",
        "border": "#d97706",
        "accent": "#f59e0b",
        "name": "Architectural",
    },
    PatternCategory.CONCURRENCY: {
        "text": "#fb7185",
        "bg": "#88133744",
        "border": "#e11d48",
        "accent": "#f43f5e",
        "name": "Concurrency",
    },
}

PATTERN_TYPE_COLORS: dict[PatternType, dict[str, str]] = {
    PatternType.OBSERVER: {"text": "#f472b6", "bg": "#83184344", "border": "#db2777"},
    PatternType.STRATEGY: {"text": "#a78bfa", "bg": "#4c1d9544", "border": "#7c3aed"},
    PatternType.DECORATOR: {"text": "#38bdf8", "bg": "#0c4a6e44", "border": "#0284c7"},
    PatternType.CHAIN_OF_RESPONSIBILITY: {"text": "#818cf8", "bg": "#312e8144", "border": "#4f46e5"},
    PatternType.TEMPLATE_METHOD: {"text": "#60a5fa", "bg": "#1e3a8a44", "border": "#2563eb"},
    PatternType.COMMAND: {"text": "#fb923c", "bg": "#7c2d1244", "border": "#ea580c"},
    PatternType.STATE: {"text": "#e879f9", "bg": "#701a7544", "border": "#c026d3"},
    PatternType.SINGLETON: {"text": "#4ade80", "bg": "#14532d44", "border": "#16a34a"},
    PatternType.FACTORY_METHOD: {"text": "#2dd4bf", "bg": "#134e4a44", "border": "#0d9488"},
    PatternType.ABSTRACT_FACTORY: {"text": "#a3e635", "bg": "#36531444", "border": "#65a30d"},
    PatternType.BUILDER: {"text": "#86efac", "bg": "#14532d44", "border": "#22c55e"},
    PatternType.ADAPTER: {"text": "#67e8f9", "bg": "#164e6344", "border": "#0891b2"},
    PatternType.FACADE: {"text": "#22d3ee", "bg": "#155e7544", "border": "#06b6d4"},
    PatternType.PROXY: {"text": "#93c5fd", "bg": "#1e3a8a44", "border": "#3b82f6"},
    PatternType.FLYWEIGHT: {"text": "#5eead4", "bg": "#134e4a44", "border": "#14b8a6"},
    PatternType.LIFECYCLE_COMPONENT: {"text": "#fcd34d", "bg": "#78350f44", "border": "#d97706"},
    PatternType.CIRCULAR_DEPENDENCY: {"text": "#f87171", "bg": "#7f1d1d44", "border": "#dc2626"},
    PatternType.PROTOTYPE: {"text": "#86efac", "bg": "#14532d44", "border": "#22c55e"},
    PatternType.COMPOSITE: {"text": "#38bdf8", "bg": "#0c4a6e44", "border": "#0284c7"},
    PatternType.BRIDGE: {"text": "#67e8f9", "bg": "#164e6344", "border": "#0891b2"},
    PatternType.ITERATOR: {"text": "#a78bfa", "bg": "#4c1d9544", "border": "#7c3aed"},
    PatternType.MEDIATOR: {"text": "#fb923c", "bg": "#7c2d1244", "border": "#ea580c"},
    PatternType.MEMENTO: {"text": "#e879f9", "bg": "#701a7544", "border": "#c026d3"},
    PatternType.VISITOR: {"text": "#f472b6", "bg": "#83184344", "border": "#db2777"},
    PatternType.INTERPRETER: {"text": "#60a5fa", "bg": "#1e3a8a44", "border": "#2563eb"},
}


class HtmlReportFormatter(ReportFormatterPort):
    """Renders a standalone, responsive, interactive HTML dashboard for DetectionReport."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        vh_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.VERY_HIGH)
        h_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.HIGH)
        m_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.MEDIUM)
        l_count = sum(1 for d in report.detections if d.level == ConfidenceLevel.LOW)

        cards_html: list[str] = []
        for idx, det in enumerate(report.detections, 1):
            cat_style = CATEGORY_COLORS.get(
                det.pattern_category,
                {"text": "#94a3b8", "bg": "#1e293b44", "border": "#475569", "accent": "#64748b", "name": "Other"},
            )
            pat_style = PATTERN_TYPE_COLORS.get(
                det.pattern_type,
                {"text": "#38bdf8", "bg": "#0c4a6e44", "border": "#0284c7"},
            )

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
                    f'<li class="evidence-item" style="border-left-color: {cat_style["accent"]};">'
                    f'<span class="weight-tag" style="color: {cat_style["text"]};">+{pct}%</span> '
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
                <div class="pattern-card" data-pattern="{html.escape(det.pattern_type.value)}" data-category="{html.escape(det.pattern_category.value)}" data-target="{html.escape(det.target_name)}" style="border-left: 4px solid {cat_style["accent"]};">
                    <div class="card-header">
                        <div class="header-left">
                            <span class="card-index">#{idx}</span>
                            <span class="category-badge" style="color: {cat_style["text"]}; background: {cat_style["bg"]}; border: 1px solid {cat_style["border"]};">
                                {html.escape(cat_style["name"].upper())}
                            </span>
                            <span class="pattern-badge" style="color: {pat_style["text"]}; background: {pat_style["bg"]}; border: 1px solid {pat_style["border"]};">
                                {html.escape(det.pattern_type.value.upper())}
                            </span>
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

        category_cards = []
        for cat_enum, style in CATEGORY_COLORS.items():
            count = report.summary_by_category.get(cat_enum.value, 0)
            if count > 0:
                category_cards.append(
                    f"""
                    <button class="cat-filter-btn" data-filter="{cat_enum.value}" style="border-color: {style['border']}; background: {style['bg']}; color: {style['text']};">
                        <span class="cat-dot" style="background: {style['accent']};"></span>
                        <strong>{style['name']}</strong>: {count}
                    </button>
                    """
                )

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pattern Scanner Report - {html.escape(report.project_path or "Codebase")}</title>
    <style>
        :root {{
            --bg: #090d13;
            --card-bg: #121822;
            --border: #232d3d;
            --text: #cbd5e1;
            --heading: #f8fafc;
            --accent: #38bdf8;
            --green: #22c55e;
            --cyan: #0ea5e9;
            --yellow: #f59e0b;
            --red: #ef4444;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace, sans-serif; }}
        body {{ background: var(--bg); color: var(--text); padding: 30px 20px; line-height: 1.5; }}
        .container {{ max-width: 1240px; margin: 0 auto; }}
        header {{ border-bottom: 1px solid var(--border); padding-bottom: 20px; margin-bottom: 25px; }}
        h1 {{ color: var(--heading); font-size: 26px; display: flex; align-items: center; gap: 10px; }}
        .subtitle {{ color: #94a3b8; font-size: 14px; margin-top: 5px; }}
        
        .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 25px; }}
        .kpi-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; padding: 18px; }}
        .kpi-title {{ font-size: 12px; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.5px; }}
        .kpi-value {{ font-size: 28px; font-weight: 700; color: var(--heading); margin-top: 5px; }}

        .category-filters {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; align-items: center; }}
        .cat-filter-btn {{ padding: 8px 14px; border-radius: 20px; border: 1px solid var(--border); background: var(--card-bg); color: var(--heading); font-size: 13px; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: transform 0.1s, opacity 0.2s; }}
        .cat-filter-btn:hover {{ transform: translateY(-1px); opacity: 0.9; }}
        .cat-filter-btn.active {{ ring: 2px solid #38bdf8; }}
        .cat-dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}
        .btn-all {{ background: #1e293b; color: #f8fafc; border-color: #475569; }}

        .search-bar {{ width: 100%; padding: 14px 18px; background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; color: var(--heading); font-size: 14px; margin-bottom: 25px; outline: none; transition: border-color 0.2s; }}
        .search-bar:focus {{ border-color: var(--accent); }}

        .pattern-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 15px; overflow: hidden; transition: border-color 0.2s, box-shadow 0.2s; }}
        .pattern-card:hover {{ border-color: #38bdf888; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }}
        .card-header {{ background: #17202e; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid var(--border); }}
        .header-left {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
        .card-index {{ color: #64748b; font-weight: 700; font-size: 13px; }}
        
        .category-badge {{ padding: 3px 8px; border-radius: 4px; font-weight: 700; font-size: 11px; letter-spacing: 0.5px; }}
        .pattern-badge {{ padding: 3px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; }}
        .target-name {{ color: var(--heading); font-size: 14px; }}
        
        .confidence-badge {{ font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; }}
        .badge-vh {{ background: #14532d55; color: #4ade80; border: 1px solid #22c55e; }}
        .badge-h {{ background: #0c4a6e55; color: #38bdf8; border: 1px solid #0284c7; }}
        .badge-m {{ background: #78350f55; color: #fbbf24; border: 1px solid #d97706; }}
        .badge-l {{ background: #7f1d1d55; color: #f87171; border: 1px solid #dc2626; }}

        .card-body {{ padding: 16px 18px; font-size: 13px; }}
        .summary-text {{ margin-bottom: 10px; color: #e2e8f0; font-size: 14px; }}
        .primary-loc {{ margin-bottom: 12px; color: #94a3b8; }}
        code {{ background: #0b0f17; padding: 3px 6px; border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; color: #7dd3fc; border: 1px solid #1e293b; }}

        .evidence-section {{ margin-top: 14px; }}
        .evidence-list {{ list-style: none; margin-top: 8px; }}
        .evidence-item {{ margin-bottom: 7px; padding-left: 12px; border-left: 3px solid; }}
        .weight-tag {{ font-weight: 700; font-family: monospace; font-size: 13px; }}
        .rule-code {{ color: #94a3b8; font-size: 11px; font-family: monospace; }}
        .location-tag {{ color: #7dd3fc; font-size: 11px; margin-left: 6px; }}
        .related-locs {{ margin-top: 12px; color: #94a3b8; }}
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
                <div class="kpi-value" style="color: #4ade80;">{vh_count + h_count}</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">Med / Low (<70%)</div>
                <div class="kpi-value" style="color: #fbbf24;">{m_count + l_count}</div>
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

        <div class="category-filters">
            <button class="cat-filter-btn btn-all" data-filter="all"><strong>All Categories</strong>: {report.total_detections_count}</button>
            {"".join(category_cards)}
        </div>

        <input type="text" id="searchInput" class="search-bar" placeholder="🔎 Instant search by pattern name, category, target function, or rule (e.g. observer, adapter, wrap-routes, with-db)...">

        <div id="cardsContainer">
            {"".join(cards_html)}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.pattern-card');
        const filterBtns = document.querySelectorAll('.cat-filter-btn');
        let selectedCategory = 'all';

        function filterCards() {{
            const query = searchInput.value.toLowerCase();
            cards.forEach(card => {{
                const text = card.textContent.toLowerCase();
                const pattern = card.dataset.pattern || '';
                const category = card.dataset.category || '';
                const target = card.dataset.target || '';

                const matchesCategory = (selectedCategory === 'all' || category === selectedCategory);
                const matchesSearch = (text.includes(query) || pattern.includes(query) || category.includes(query) || target.includes(query));

                if (matchesCategory && matchesSearch) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        searchInput.addEventListener('input', filterCards);

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                selectedCategory = btn.dataset.filter;
                filterBtns.forEach(b => b.style.outline = 'none');
                btn.style.outline = '2px solid #38bdf8';
                filterCards();
            }});
        }});
    </script>
</body>
</html>
"""

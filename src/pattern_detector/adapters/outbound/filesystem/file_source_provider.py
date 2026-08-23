"""Filesystem Outbound Adapter implementing SourceProviderPort."""

from __future__ import annotations

from pathlib import Path

from pattern_detector.ports.outbound import SourceProviderPort


class FileSourceProvider(SourceProviderPort):
    """Fetches source code files from the local filesystem."""

    def get_sources(self, path: str, extensions: list[str] | None = None) -> dict[str, str]:
        target = Path(path)
        valid_exts = set(extensions) if extensions else {".clj", ".cljs", ".cljc", ".edn"}
        sources: dict[str, str] = {}

        if not target.exists():
            return sources

        if target.is_file():
            try:
                content = target.read_text(encoding="utf-8", errors="replace")
                sources[str(target)] = content
            except (OSError, UnicodeDecodeError):
                pass
            return sources

        for file_path in target.rglob("*"):
            if file_path.is_file() and file_path.suffix in valid_exts:
                try:
                    rel_parts = file_path.relative_to(target).parts
                except ValueError:
                    rel_parts = file_path.parts
                # Skip hidden files/directories relative to root target
                if any(part.startswith(".") and part not in (".", "..") for part in rel_parts):
                    continue
                try:
                    content = file_path.read_text(encoding="utf-8", errors="replace")
                    sources[str(file_path)] = content
                except (OSError, UnicodeDecodeError):
                    continue

        return sources

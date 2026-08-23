"""Domain entities for pattern detections and analysis reports."""

from __future__ import annotations

from dataclasses import dataclass, field

from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.domain.value_objects import (
    Confidence,
    ConfidenceLevel,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


@dataclass
class Detection:
    """Represents an identified pattern instance in the target code."""

    pattern_type: PatternType
    pattern_category: PatternCategory
    target_name: str
    target_kind: str  # e.g., "function", "multimethod", "protocol", "record", "state", "extension"
    confidence: Confidence
    primary_location: SourceLocation
    related_locations: list[SourceLocation] = field(default_factory=list)
    summary: str = ""
    evidences: list[Evidence] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.summary:
            cat_name = PATTERN_CATALOG.get(self.pattern_type)
            pname = cat_name.name if cat_name else self.pattern_type.value
            self.summary = f"Detected {pname} on {self.target_kind} '{self.target_name}' ({self.confidence.percentage_str} confidence)"
        if not self.evidences and self.confidence.evidences:
            self.evidences = list(self.confidence.evidences)

    @property
    def level(self) -> ConfidenceLevel:
        return self.confidence.level

    def to_dict(self) -> dict[str, object]:
        return {
            "pattern_type": self.pattern_type.value,
            "pattern_category": self.pattern_category.value,
            "target_name": self.target_name,
            "target_kind": self.target_kind,
            "confidence": self.confidence.to_dict(),
            "primary_location": self.primary_location.to_dict(),
            "related_locations": [loc.to_dict() for loc in self.related_locations],
            "summary": self.summary,
            "evidences": [e.to_dict() for e in self.evidences],
        }


@dataclass
class DetectionReport:
    """Complete report produced after scanning a codebase."""

    project_path: str
    scanned_files_count: int
    detections: list[Detection] = field(default_factory=list)
    elapsed_seconds: float = 0.0

    @property
    def total_detections_count(self) -> int:
        return len(self.detections)

    @property
    def summary_by_category(self) -> dict[str, int]:
        counts: dict[str, int] = {c.value: 0 for c in PatternCategory}
        for d in self.detections:
            counts[d.pattern_category.value] = counts.get(d.pattern_category.value, 0) + 1
        return counts

    @property
    def summary_by_type(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for d in self.detections:
            counts[d.pattern_type.value] = counts.get(d.pattern_type.value, 0) + 1
        return counts

    @property
    def summary_by_confidence_level(self) -> dict[str, int]:
        counts: dict[str, int] = {level.value: 0 for level in ConfidenceLevel}
        for d in self.detections:
            counts[d.level.value] = counts.get(d.level.value, 0) + 1
        return counts

    def filter_by_min_confidence(self, min_score: float) -> list[Detection]:
        return [d for d in self.detections if d.confidence.score >= min_score]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_path": self.project_path,
            "scanned_files_count": self.scanned_files_count,
            "total_detections": self.total_detections_count,
            "elapsed_seconds": round(self.elapsed_seconds, 4),
            "summary_by_category": self.summary_by_category,
            "summary_by_type": self.summary_by_type,
            "summary_by_confidence_level": self.summary_by_confidence_level,
            "detections": [d.to_dict() for d in sorted(self.detections, key=lambda x: x.confidence.score, reverse=True)],
        }

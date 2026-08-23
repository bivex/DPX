"""Base abstractions and protocol for pattern detection rules."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


@runtime_checkable
class PatternRule(Protocol):
    """Rule protocol that every pattern detection rule must satisfy."""

    @property
    def pattern_type(self) -> PatternType:
        """The pattern type this rule detects."""
        ...

    @property
    def pattern_category(self) -> PatternCategory:
        """The category of the detected pattern."""
        ...

    @property
    def name(self) -> str:
        """Human-readable rule name."""
        ...

    @property
    def description(self) -> str:
        """Description of what this rule inspects."""
        ...

    def detect(self, model: CodeModel) -> list[Detection]:
        """Analyze the domain code model and return all matched pattern instances."""
        ...


class BasePatternRule(ABC):
    """Convenient base class for pattern rules with helper utilities."""

    @property
    @abstractmethod
    def pattern_type(self) -> PatternType:
        """Target pattern type."""
        ...

    @property
    def pattern_category(self) -> PatternCategory:
        catalog_entry = PATTERN_CATALOG.get(self.pattern_type)
        if catalog_entry:
            return catalog_entry.category
        return PatternCategory.BEHAVIORAL

    @property
    def name(self) -> str:
        catalog_entry = PATTERN_CATALOG.get(self.pattern_type)
        return catalog_entry.name if catalog_entry else self.pattern_type.value

    @property
    def description(self) -> str:
        catalog_entry = PATTERN_CATALOG.get(self.pattern_type)
        return catalog_entry.description if catalog_entry else ""

    def evidence(
        self,
        description: str,
        weight: float,
        location: SourceLocation | None = None,
        snippet: str | None = None,
        code_suffix: str = "",
    ) -> Evidence:
        rule_code = f"{self.pattern_type.value.upper()}_{code_suffix}" if code_suffix else self.pattern_type.value.upper()
        return Evidence(
            description=description,
            weight=weight,
            rule_code=rule_code,
            location=location,
            snippet=snippet,
        )

    def create_detection(
        self,
        target_name: str,
        target_kind: str,
        evidences: list[Evidence],
        primary_location: SourceLocation,
        related_locations: list[SourceLocation] | None = None,
        summary: str = "",
        base_score: float = 0.0,
    ) -> Detection:
        confidence = Confidence.from_evidences(evidences, base_score=base_score)
        return Detection(
            pattern_type=self.pattern_type,
            pattern_category=self.pattern_category,
            target_name=target_name,
            target_kind=target_kind,
            confidence=confidence,
            primary_location=primary_location,
            related_locations=related_locations or [],
            summary=summary,
            evidences=evidences,
        )

    @abstractmethod
    def detect(self, model: CodeModel) -> list[Detection]:
        """Execute detection logic against CodeModel."""
        ...

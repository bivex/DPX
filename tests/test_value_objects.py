"""Tests for Domain Value Objects."""

import pytest

from pattern_detector.domain.value_objects import (
    Confidence,
    ConfidenceLevel,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


def test_source_location_formatting() -> None:
    loc1 = SourceLocation(file_path="src/core.clj", line=10, column=5)
    assert str(loc1) == "src/core.clj:10:5"
    assert loc1.to_dict()["formatted"] == "src/core.clj:10:5"

    loc2 = SourceLocation(file_path="src/core.clj", line=10, column=5, end_line=15, end_column=20)
    assert str(loc2) == "src/core.clj:10:5-15:20"


def test_evidence_validation() -> None:
    ev = Evidence(
        description="Private constructor found",
        weight=0.5,
        rule_code="SINGLETON_PRIVATE_CTOR",
    )
    assert ev.weight == 0.5
    assert ev.rule_code == "SINGLETON_PRIVATE_CTOR"

    with pytest.raises(ValueError):
        Evidence(description="Invalid weight", weight=1.5, rule_code="TEST")


def test_confidence_calculation_and_levels() -> None:
    ev1 = Evidence(description="Indicator A", weight=0.4, rule_code="A")
    ev2 = Evidence(description="Indicator B", weight=0.5, rule_code="B")

    # Combined = 0.4 + 0.5 * (1 - 0.4) = 0.4 + 0.3 = 0.70
    conf = Confidence.from_evidences([ev1, ev2])
    assert conf.score == 0.70
    assert conf.level == ConfidenceLevel.HIGH
    assert conf.percentage_str == "70%"

    high_ev = Evidence(description="Strong indicator", weight=0.9, rule_code="C")
    conf_very_high = Confidence.from_evidences([ev1, ev2, high_ev])
    assert conf_very_high.level == ConfidenceLevel.VERY_HIGH

    low_conf = Confidence(score=0.35)
    assert low_conf.level == ConfidenceLevel.LOW


def test_pattern_types_and_categories() -> None:
    assert PatternCategory.BEHAVIORAL == "behavioral"
    assert PatternType.OBSERVER == "observer"
    assert PatternType.STRATEGY == "strategy"
    assert PatternType.SINGLETON == "singleton"

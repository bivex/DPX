"""Domain value objects for the Pattern Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class PatternCategory(str, Enum):
    """Broad classification of design patterns."""

    CREATIONAL = "creational"
    STRUCTURAL = "structural"
    BEHAVIORAL = "behavioral"
    ARCHITECTURAL = "architectural"
    CONCURRENCY = "concurrency"


class PatternType(str, Enum):
    """Specific design pattern identifiers."""

    # Creational
    SINGLETON = "singleton"
    FACTORY_METHOD = "factory_method"
    ABSTRACT_FACTORY = "abstract_factory"
    BUILDER = "builder"
    PROTOTYPE = "prototype"

    # Structural
    ADAPTER = "adapter"
    DECORATOR = "decorator"
    FACADE = "facade"
    COMPOSITE = "composite"
    PROXY = "proxy"
    BRIDGE = "bridge"
    FLYWEIGHT = "flyweight"

    # Behavioral
    OBSERVER = "observer"
    STRATEGY = "strategy"
    COMMAND = "command"
    TEMPLATE_METHOD = "template_method"
    CHAIN_OF_RESPONSIBILITY = "chain_of_responsibility"
    STATE = "state"
    ITERATOR = "iterator"
    MEDIATOR = "mediator"
    MEMENTO = "memento"
    VISITOR = "visitor"
    INTERPRETER = "interpreter"

    # Idiomatic & Functional Architecture
    LIFECYCLE_COMPONENT = "lifecycle_component"
    MIDDLEWARE_PIPELINE = "middleware_pipeline"
    MULTIMETHOD_DISPATCH = "multimethod_dispatch"
    CIRCULAR_DEPENDENCY = "circular_dependency"


class ConfidenceLevel(str, Enum):
    """Confidence grade based on score."""

    VERY_HIGH = "VERY_HIGH"  # >= 0.85
    HIGH = "HIGH"            # >= 0.70
    MEDIUM = "MEDIUM"        # >= 0.50
    LOW = "LOW"              # < 0.50


@dataclass(frozen=True)
class SourceLocation:
    """Represents a location in a source code file."""

    file_path: str
    line: int
    column: int = 1
    end_line: int | None = None
    end_column: int | None = None

    def __str__(self) -> str:
        if self.end_line and self.end_line != self.line:
            return f"{self.file_path}:{self.line}:{self.column}-{self.end_line}:{self.end_column or 1}"
        return f"{self.file_path}:{self.line}:{self.column}"

    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "file_path": self.file_path,
            "line": self.line,
            "column": self.column,
            "end_line": self.end_line,
            "end_column": self.end_column,
            "formatted": str(self),
        }


@dataclass(frozen=True)
class Evidence:
    """A piece of heuristic evidence contributing to pattern detection."""

    description: str
    weight: float
    rule_code: str
    location: SourceLocation | None = None
    snippet: str | None = None

    def __post_init__(self) -> None:
        if not (0.0 <= self.weight <= 1.0):
            raise ValueError(f"Evidence weight must be between 0.0 and 1.0, got {self.weight}")

    def to_dict(self) -> dict[str, object]:
        return {
            "description": self.description,
            "weight": self.weight,
            "rule_code": self.rule_code,
            "location": self.location.to_dict() if self.location else None,
            "snippet": self.snippet,
        }


@dataclass(frozen=True)
class Confidence:
    """Confidence score calculated from combined evidence."""

    score: float
    evidences: list[Evidence] = field(default_factory=list)

    def __post_init__(self) -> None:
        clamped = max(0.0, min(1.0, float(self.score)))
        object.__setattr__(self, "score", round(clamped, 2))

    @property
    def level(self) -> ConfidenceLevel:
        if self.score >= 0.85:
            return ConfidenceLevel.VERY_HIGH
        if self.score >= 0.70:
            return ConfidenceLevel.HIGH
        if self.score >= 0.50:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    @property
    def percentage_str(self) -> str:
        return f"{int(self.score * 100)}%"

    @classmethod
    def from_evidences(cls, evidences: list[Evidence], base_score: float = 0.0) -> Confidence:
        """Calculate combined confidence score using asymptotic saturation.

        Score increases with each evidence: total = 1 - (1 - current) * (1 - weight)
        """
        if not evidences:
            return cls(score=base_score, evidences=[])

        combined = base_score
        for ev in evidences:
            combined = combined + ev.weight * (1.0 - combined)

        return cls(score=combined, evidences=list(evidences))

    def to_dict(self) -> dict[str, object]:
        return {
            "score": self.score,
            "level": self.level.value,
            "percentage": self.percentage_str,
            "evidences": [e.to_dict() for e in self.evidences],
        }

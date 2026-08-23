"""Domain Layer exports."""

from pattern_detector.domain.code_model import (
    CodeModel,
    FunctionInvocation,
    FunctionModel,
    MethodSignature,
    NamespaceModel,
    ProtocolExtensionModel,
    ProtocolModel,
    RecordModel,
    StateModel,
    WatchModel,
)
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.domain.pattern import PATTERN_CATALOG, PatternDefinition
from pattern_detector.domain.value_objects import (
    Confidence,
    ConfidenceLevel,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)

__all__ = [
    "PATTERN_CATALOG",
    "CodeModel",
    "Confidence",
    "ConfidenceLevel",
    "Detection",
    "DetectionReport",
    "Evidence",
    "FunctionInvocation",
    "FunctionModel",
    "MethodSignature",
    "NamespaceModel",
    "PatternCategory",
    "PatternDefinition",
    "PatternType",
    "ProtocolExtensionModel",
    "ProtocolModel",
    "RecordModel",
    "SourceLocation",
    "StateModel",
    "WatchModel",
]

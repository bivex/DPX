"""Domain entities for Design Patterns metadata."""

from __future__ import annotations

from dataclasses import dataclass, field

from pattern_detector.domain.value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternDefinition:
    """Catalog metadata definition for a known software design pattern."""

    type: PatternType
    name: str
    category: PatternCategory
    description: str
    intent: str
    idiomatic_in_clojure: bool = True
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "type": self.type.value,
            "name": self.name,
            "category": self.category.value,
            "description": self.description,
            "intent": self.intent,
            "idiomatic_in_clojure": self.idiomatic_in_clojure,
            "tags": list(self.tags),
        }


PATTERN_CATALOG: dict[PatternType, PatternDefinition] = {
    PatternType.OBSERVER: PatternDefinition(
        type=PatternType.OBSERVER,
        name="Observer (Watchers / Pub-Sub)",
        category=PatternCategory.BEHAVIORAL,
        description="Defines a subscription mechanism to notify multiple objects about state changes.",
        intent="Keep decoupled components synchronized when state in atoms/refs changes.",
        tags=["state", "concurrency", "events", "watches"],
    ),
    PatternType.STRATEGY: PatternDefinition(
        type=PatternType.STRATEGY,
        name="Strategy / Polymorphic Dispatch",
        category=PatternCategory.BEHAVIORAL,
        description="Defines a family of algorithms, encapsulates each one, and makes them interchangeable.",
        intent="Select algorithm implementation at runtime via multimethods or protocols.",
        tags=["multimethods", "protocols", "polymorphism"],
    ),
    PatternType.DECORATOR: PatternDefinition(
        type=PatternType.DECORATOR,
        name="Decorator / Ring Middleware",
        category=PatternCategory.STRUCTURAL,
        description="Attaches additional responsibilities to an object dynamically.",
        intent="Wrap handler functions with cross-cutting concerns (logging, auth, params parsing).",
        tags=["middleware", "higher-order-functions", "composition"],
    ),
    PatternType.CHAIN_OF_RESPONSIBILITY: PatternDefinition(
        type=PatternType.CHAIN_OF_RESPONSIBILITY,
        name="Chain of Responsibility / Pipeline",
        category=PatternCategory.BEHAVIORAL,
        description="Passes requests along a chain of potential handlers.",
        intent="Allow multiple middleware layers to process or short-circuit a request.",
        tags=["pipeline", "middleware", "threading"],
    ),
    PatternType.SINGLETON: PatternDefinition(
        type=PatternType.SINGLETON,
        name="Singleton / Stateful Instance",
        category=PatternCategory.CREATIONAL,
        description="Ensures a class has only one instance and provides a global access point.",
        intent="Provide a unique shared state container (defonce with atom/ref/component).",
        tags=["defonce", "shared-state", "global"],
    ),
    PatternType.FACTORY_METHOD: PatternDefinition(
        type=PatternType.FACTORY_METHOD,
        name="Factory Method / Constructor Helpers",
        category=PatternCategory.CREATIONAL,
        description="Provides an interface for creating objects, delegating instantiation logic.",
        intent="Encapsulate creation of records/components with defaults, validation, and polymorphism.",
        tags=["constructors", "records", "creation"],
    ),
    PatternType.ADAPTER: PatternDefinition(
        type=PatternType.ADAPTER,
        name="Adapter / Protocol Extension",
        category=PatternCategory.STRUCTURAL,
        description="Allows objects with incompatible interfaces to collaborate.",
        intent="Adapt existing types/classes to new protocols without modifying their source.",
        tags=["extend-type", "extend-protocol", "interop"],
    ),
    PatternType.LIFECYCLE_COMPONENT: PatternDefinition(
        type=PatternType.LIFECYCLE_COMPONENT,
        name="Lifecycle Component (Stuart Sierra Component / Integrant)",
        category=PatternCategory.ARCHITECTURAL,
        description="Manages stateful components and their dependencies through explicit start/stop lifecycles.",
        intent="Compose managed systems with explicit dependency injection and deterministic teardown.",
        tags=["lifecycle", "dependency-injection", "component"],
    ),
    PatternType.TEMPLATE_METHOD: PatternDefinition(
        type=PatternType.TEMPLATE_METHOD,
        name="Template Method / Functional Template",
        category=PatternCategory.BEHAVIORAL,
        description="Defines the skeleton of an algorithm in a method, deferring some steps to callers.",
        intent="Encapsulate invariant resource or bracket logic (e.g. with-open) with customizable step callbacks.",
        tags=["macros", "callbacks", "brackets"],
    ),
    PatternType.CIRCULAR_DEPENDENCY: PatternDefinition(
        type=PatternType.CIRCULAR_DEPENDENCY,
        name="Circular Dependency / Namespace Cycle",
        category=PatternCategory.ARCHITECTURAL,
        description="Identifies mutual recursive dependencies and import cycles between namespaces.",
        intent="Detect architectural coupling smells and circular cross-namespace invocation loops.",
        tags=["architecture", "dependencies", "cycles", "coupling"],
    ),
}

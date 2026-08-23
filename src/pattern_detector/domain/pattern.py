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
    PatternType.COMMAND: PatternDefinition(
        type=PatternType.COMMAND,
        name="Command / CQRS Message Handler",
        category=PatternCategory.BEHAVIORAL,
        description="Encapsulates a request as an object or message, thereby letting you parameterize handlers with different requests.",
        intent="Decouple message/command producers from executors via message dispatch.",
        tags=["cqrs", "events", "messages", "dispatch"],
    ),
    PatternType.BUILDER: PatternDefinition(
        type=PatternType.BUILDER,
        name="Builder / Step Configuration",
        category=PatternCategory.CREATIONAL,
        description="Constructs complex objects step by step through fluent chaining or parameter accumulators.",
        intent="Separate the construction of a complex object from its representation.",
        tags=["dsl", "configuration", "fluent", "assoc"],
    ),
    PatternType.FACADE: PatternDefinition(
        type=PatternType.FACADE,
        name="Facade / API Gateway Module",
        category=PatternCategory.STRUCTURAL,
        description="Provides a unified interface to a set of interfaces in a subsystem.",
        intent="Define a higher-level interface that makes the subsystem easier to use.",
        tags=["api", "gateway", "delegation", "subsystem"],
    ),
    PatternType.PROXY: PatternDefinition(
        type=PatternType.PROXY,
        name="Proxy / Lazy Virtual Proxy",
        category=PatternCategory.STRUCTURAL,
        description="Provides a surrogate or placeholder for another object to control access to it.",
        intent="Control access, delay expensive instantiation, or implement host interop proxies.",
        tags=["proxy", "delay", "future", "interop"],
    ),
    PatternType.STATE: PatternDefinition(
        type=PatternType.STATE,
        name="State / Finite State Machine (FSM)",
        category=PatternCategory.BEHAVIORAL,
        description="Allows an object to alter its behavior when its internal state changes.",
        intent="Model state transitions and transition dispatch as explicit state machine tables/functions.",
        tags=["fsm", "transitions", "state-machine"],
    ),
    PatternType.FLYWEIGHT: PatternDefinition(
        type=PatternType.FLYWEIGHT,
        name="Flyweight / Memoization & Object Cache",
        category=PatternCategory.STRUCTURAL,
        description="Uses sharing to support large numbers of fine-grained objects efficiently.",
        intent="Share immutable state through memoize or interning tables.",
        tags=["memoize", "cache", "intern", "sharing"],
    ),
    PatternType.ABSTRACT_FACTORY: PatternDefinition(
        type=PatternType.ABSTRACT_FACTORY,
        name="Abstract Factory / Service Factory Protocol",
        category=PatternCategory.CREATIONAL,
        description="Provides an interface for creating families of related or dependent objects.",
        intent="Isolate concrete product creation behind a unified factory protocol.",
        tags=["factories", "protocols", "families"],
    ),
    PatternType.PROTOTYPE: PatternDefinition(
        type=PatternType.PROTOTYPE,
        name="Prototype / Cloneable Variant",
        category=PatternCategory.CREATIONAL,
        description="Creates new objects by copying an existing prototype instance with modifications.",
        intent="Derive new configurations or domain records from prototype templates.",
        tags=["prototype", "clone", "derive", "copy"],
    ),
    PatternType.COMPOSITE: PatternDefinition(
        type=PatternType.COMPOSITE,
        name="Composite / Tree Structure",
        category=PatternCategory.STRUCTURAL,
        description="Composes objects into tree structures to represent part-whole hierarchies.",
        intent="Treat individual leaf objects and compositions of objects uniformly via shared protocol.",
        tags=["trees", "hierarchy", "containers", "recursive"],
    ),
    PatternType.BRIDGE: PatternDefinition(
        type=PatternType.BRIDGE,
        name="Bridge / Decoupled Abstraction & Implementation",
        category=PatternCategory.STRUCTURAL,
        description="Decouples an abstraction from its implementation so that the two can vary independently.",
        intent="Separate high-level domain operations from low-level backend platform drivers.",
        tags=["bridge", "drivers", "decoupling", "backends"],
    ),
    PatternType.ITERATOR: PatternDefinition(
        type=PatternType.ITERATOR,
        name="Iterator / Lazy Sequence Generator",
        category=PatternCategory.BEHAVIORAL,
        description="Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.",
        intent="Encapsulate custom traversal or infinite generator streams (lazy-seq).",
        tags=["sequences", "lazy-seq", "iteration", "generators"],
    ),
    PatternType.MEDIATOR: PatternDefinition(
        type=PatternType.MEDIATOR,
        name="Mediator / Event Broker Hub",
        category=PatternCategory.BEHAVIORAL,
        description="Defines an object that encapsulates how a set of objects interact.",
        intent="Promote loose coupling by keeping objects from referring to each other explicitly.",
        tags=["event-bus", "mediator", "channels", "hub"],
    ),
    PatternType.MEMENTO: PatternDefinition(
        type=PatternType.MEMENTO,
        name="Memento / State Snapshot & History",
        category=PatternCategory.BEHAVIORAL,
        description="Without violating encapsulation, captures and externalizes an object's internal state so that the object can be restored to this state later.",
        intent="Support undo/redo, checkpointing, and time-travel debugging.",
        tags=["snapshots", "history", "undo", "checkpoints"],
    ),
    PatternType.VISITOR: PatternDefinition(
        type=PatternType.VISITOR,
        name="Visitor / Tree Traversal Walker",
        category=PatternCategory.BEHAVIORAL,
        description="Represents an operation to be performed on the elements of an object structure.",
        intent="Define a new operation without changing the classes of the elements on which it operates.",
        tags=["walker", "postwalk", "visitor", "ast-traversal"],
    ),
    PatternType.INTERPRETER: PatternDefinition(
        type=PatternType.INTERPRETER,
        name="Interpreter / Domain Expression Evaluator",
        category=PatternCategory.BEHAVIORAL,
        description="Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.",
        intent="Evaluate AST expressions or rule engines via recursive evaluation.",
        tags=["eval", "dsl", "interpreter", "ast-eval"],
    ),
}

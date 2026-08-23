"""Domain pattern rules exports and default registry."""

from pattern_detector.domain.rules.abstract_factory_rule import AbstractFactoryRule
from pattern_detector.domain.rules.adapter_rule import AdapterPatternRule
from pattern_detector.domain.rules.base import BasePatternRule, PatternRule
from pattern_detector.domain.rules.bridge_rule import BridgePatternRule
from pattern_detector.domain.rules.builder_rule import BuilderPatternRule
from pattern_detector.domain.rules.chain_of_responsibility_rule import ChainOfResponsibilityRule
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.rules.command_rule import CommandPatternRule
from pattern_detector.domain.rules.composite_rule import CompositePatternRule
from pattern_detector.domain.rules.decorator_rule import DecoratorPatternRule
from pattern_detector.domain.rules.facade_rule import FacadePatternRule
from pattern_detector.domain.rules.factory_rule import FactoryPatternRule
from pattern_detector.domain.rules.flyweight_rule import FlyweightPatternRule
from pattern_detector.domain.rules.interpreter_rule import InterpreterPatternRule
from pattern_detector.domain.rules.iterator_rule import IteratorPatternRule
from pattern_detector.domain.rules.lifecycle_rule import LifecycleComponentPatternRule
from pattern_detector.domain.rules.mediator_rule import MediatorPatternRule
from pattern_detector.domain.rules.memento_rule import MementoPatternRule
from pattern_detector.domain.rules.observer_rule import ObserverPatternRule
from pattern_detector.domain.rules.prototype_rule import PrototypePatternRule
from pattern_detector.domain.rules.proxy_rule import ProxyPatternRule
from pattern_detector.domain.rules.singleton_rule import SingletonPatternRule
from pattern_detector.domain.rules.state_rule import StatePatternRule
from pattern_detector.domain.rules.strategy_rule import StrategyPatternRule
from pattern_detector.domain.rules.template_method_rule import TemplateMethodRule
from pattern_detector.domain.rules.visitor_rule import VisitorPatternRule


def get_default_rules() -> list[PatternRule]:
    """Return an instantiated list of all built-in pattern detection rules."""
    return [
        ObserverPatternRule(),
        StrategyPatternRule(),
        DecoratorPatternRule(),
        SingletonPatternRule(),
        FactoryPatternRule(),
        AdapterPatternRule(),
        LifecycleComponentPatternRule(),
        ChainOfResponsibilityRule(),
        CircularDependencyRule(),
        TemplateMethodRule(),
        CommandPatternRule(),
        BuilderPatternRule(),
        FacadePatternRule(),
        ProxyPatternRule(),
        StatePatternRule(),
        FlyweightPatternRule(),
        AbstractFactoryRule(),
        PrototypePatternRule(),
        CompositePatternRule(),
        BridgePatternRule(),
        IteratorPatternRule(),
        MediatorPatternRule(),
        MementoPatternRule(),
        VisitorPatternRule(),
        InterpreterPatternRule(),
    ]


__all__ = [
    "AbstractFactoryRule",
    "AdapterPatternRule",
    "BasePatternRule",
    "BridgePatternRule",
    "BuilderPatternRule",
    "ChainOfResponsibilityRule",
    "CircularDependencyRule",
    "CommandPatternRule",
    "CompositePatternRule",
    "DecoratorPatternRule",
    "FacadePatternRule",
    "FactoryPatternRule",
    "FlyweightPatternRule",
    "InterpreterPatternRule",
    "IteratorPatternRule",
    "LifecycleComponentPatternRule",
    "MediatorPatternRule",
    "MementoPatternRule",
    "ObserverPatternRule",
    "PatternRule",
    "PrototypePatternRule",
    "ProxyPatternRule",
    "SingletonPatternRule",
    "StatePatternRule",
    "StrategyPatternRule",
    "TemplateMethodRule",
    "VisitorPatternRule",
    "get_default_rules",
]

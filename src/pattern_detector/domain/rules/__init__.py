"""Domain pattern rules exports and default registry."""

from pattern_detector.domain.rules.abstract_factory_rule import AbstractFactoryRule
from pattern_detector.domain.rules.adapter_rule import AdapterPatternRule
from pattern_detector.domain.rules.base import BasePatternRule, PatternRule
from pattern_detector.domain.rules.builder_rule import BuilderPatternRule
from pattern_detector.domain.rules.chain_of_responsibility_rule import ChainOfResponsibilityRule
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.rules.command_rule import CommandPatternRule
from pattern_detector.domain.rules.decorator_rule import DecoratorPatternRule
from pattern_detector.domain.rules.facade_rule import FacadePatternRule
from pattern_detector.domain.rules.factory_rule import FactoryPatternRule
from pattern_detector.domain.rules.flyweight_rule import FlyweightPatternRule
from pattern_detector.domain.rules.lifecycle_rule import LifecycleComponentPatternRule
from pattern_detector.domain.rules.observer_rule import ObserverPatternRule
from pattern_detector.domain.rules.proxy_rule import ProxyPatternRule
from pattern_detector.domain.rules.singleton_rule import SingletonPatternRule
from pattern_detector.domain.rules.state_rule import StatePatternRule
from pattern_detector.domain.rules.strategy_rule import StrategyPatternRule
from pattern_detector.domain.rules.template_method_rule import TemplateMethodRule


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
    ]


__all__ = [
    "AbstractFactoryRule",
    "AdapterPatternRule",
    "BasePatternRule",
    "BuilderPatternRule",
    "ChainOfResponsibilityRule",
    "CircularDependencyRule",
    "CommandPatternRule",
    "DecoratorPatternRule",
    "FacadePatternRule",
    "FactoryPatternRule",
    "FlyweightPatternRule",
    "LifecycleComponentPatternRule",
    "ObserverPatternRule",
    "PatternRule",
    "ProxyPatternRule",
    "SingletonPatternRule",
    "StatePatternRule",
    "StrategyPatternRule",
    "TemplateMethodRule",
    "get_default_rules",
]

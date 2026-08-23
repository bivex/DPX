"""Domain pattern rules exports and default registry."""

from pattern_detector.domain.rules.adapter_rule import AdapterPatternRule
from pattern_detector.domain.rules.base import BasePatternRule, PatternRule
from pattern_detector.domain.rules.chain_of_responsibility_rule import ChainOfResponsibilityRule
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.rules.decorator_rule import DecoratorPatternRule
from pattern_detector.domain.rules.factory_rule import FactoryPatternRule
from pattern_detector.domain.rules.lifecycle_rule import LifecycleComponentPatternRule
from pattern_detector.domain.rules.observer_rule import ObserverPatternRule
from pattern_detector.domain.rules.singleton_rule import SingletonPatternRule
from pattern_detector.domain.rules.strategy_rule import StrategyPatternRule


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
    ]


__all__ = [
    "AdapterPatternRule",
    "BasePatternRule",
    "ChainOfResponsibilityRule",
    "CircularDependencyRule",
    "DecoratorPatternRule",
    "FactoryPatternRule",
    "LifecycleComponentPatternRule",
    "ObserverPatternRule",
    "PatternRule",
    "SingletonPatternRule",
    "StrategyPatternRule",
    "get_default_rules",
]

"""Tests for Domain Pattern Detection Rules."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.domain.rules import (
    AdapterPatternRule,
    DecoratorPatternRule,
    FactoryPatternRule,
    LifecycleComponentPatternRule,
    ObserverPatternRule,
    SingletonPatternRule,
    StrategyPatternRule,
)
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType


def test_observer_pattern_rule() -> None:
    code = """
    (ns my.events)

    (defonce bus (atom {:count 0}))

    (defn audit-handler [key ref old-state new-state]
      (println "Audit event"))

    (defn init! []
      (add-watch bus :audit audit-handler))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"events.clj": code})

    rule = ObserverPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    obs = next(d for d in detections if d.target_name == "bus")
    assert obs.pattern_type == PatternType.OBSERVER
    assert obs.confidence.score >= 0.70
    assert any("add-watch" in ev.description.lower() for ev in obs.evidences)


def test_strategy_pattern_multimethods() -> None:
    code = """
    (ns my.billing)

    (defmulti charge (fn [tx] (:provider tx)))
    (defmethod charge :stripe [tx] (println "Stripe"))
    (defmethod charge :paypal [tx] (println "PayPal"))
    (defmethod charge :braintree [tx] (println "Braintree"))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"billing.clj": code})

    rule = StrategyPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    strat = next(d for d in detections if d.target_name == "charge")
    assert strat.pattern_type == PatternType.STRATEGY
    assert strat.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)


def test_decorator_pattern_middleware() -> None:
    code = """
    (ns my.middleware)

    (defn wrap-auth [handler]
      (fn [req]
        (if (:user req)
          (handler req)
          {:status 401})))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"middleware.clj": code})

    rule = DecoratorPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    dec = next(d for d in detections if d.target_name == "wrap-auth")
    assert dec.pattern_type == PatternType.DECORATOR
    assert dec.confidence.score >= 0.70


def test_singleton_pattern_defonce() -> None:
    code = """
    (ns my.state)

    (defonce global-cache (atom {}))

    (defn get-cache []
      @global-cache)
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"state.clj": code})

    rule = SingletonPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    sing = next(d for d in detections if d.target_name == "global-cache")
    assert sing.pattern_type == PatternType.SINGLETON
    assert sing.confidence.score >= 0.70


def test_factory_pattern_helpers() -> None:
    code = """
    (ns my.domain)

    (defrecord Order [id items total])

    (defn make-order [items]
      (->Order (random-uuid) items (reduce + (map :price items))))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"domain.clj": code})

    rule = FactoryPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    fact = next(d for d in detections if d.target_name == "make-order")
    assert fact.pattern_type == PatternType.FACTORY_METHOD
    assert fact.confidence.score >= 0.70


def test_adapter_pattern_extend_type() -> None:
    code = """
    (ns my.adapter)

    (defprotocol Formattable
      (format-str [this]))

    (extend-type java.lang.String
      Formattable
      (format-str [this] (.trim this)))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"adapter.clj": code})

    rule = AdapterPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 1
    adapt = next(d for d in detections if "java.lang.String" in d.target_name)
    assert adapt.pattern_type == PatternType.ADAPTER


def test_lifecycle_component_pattern() -> None:
    code = """
    (ns my.system)

    (defprotocol Lifecycle
      (start [this])
      (stop [this]))

    (defrecord WebServer [port server]
      Lifecycle
      (start [this] (assoc this :server "running"))
      (stop [this] (assoc this :server nil)))
    """
    adapter = ClojureAntlrParserAdapter()
    code_model = adapter.parse_sources({"system.clj": code})

    rule = LifecycleComponentPatternRule()
    detections = rule.detect(code_model)

    assert len(detections) >= 2  # Protocol + Record
    rec_det = next(d for d in detections if d.target_name == "WebServer")
    assert rec_det.pattern_type == PatternType.LIFECYCLE_COMPONENT

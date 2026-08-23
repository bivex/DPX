"""Tests for all newly implemented design pattern rules."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.domain.rules.abstract_factory_rule import AbstractFactoryRule
from pattern_detector.domain.rules.builder_rule import BuilderPatternRule
from pattern_detector.domain.rules.command_rule import CommandPatternRule
from pattern_detector.domain.rules.facade_rule import FacadePatternRule
from pattern_detector.domain.rules.flyweight_rule import FlyweightPatternRule
from pattern_detector.domain.rules.proxy_rule import ProxyPatternRule
from pattern_detector.domain.rules.state_rule import StatePatternRule
from pattern_detector.domain.rules.template_method_rule import TemplateMethodRule
from pattern_detector.domain.value_objects import PatternType


def test_template_method_rule() -> None:
    code = """
    (ns my.bracket)

    (defmacro with-db-transaction [[tx db] & body]
      `(let [~tx (start-tx ~db)]
         (try
           ~@body
           (catch Exception e#
             (rollback-tx ~tx)
             (throw e#))
           (finally
             (commit-tx ~tx)))))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"bracket.clj": code})
    detections = TemplateMethodRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.TEMPLATE_METHOD
    assert detections[0].target_name == "with-db-transaction"
    assert detections[0].confidence.score >= 0.70


def test_command_pattern_rule() -> None:
    code = """
    (ns my.cqrs)

    (defmulti handle-command (fn [cmd] (:type cmd)))

    (defmethod handle-command :create-user [cmd]
      {:status :ok :user (:name cmd)})

    (defmethod handle-command :delete-user [cmd]
      {:status :ok :deleted true})
    """
    model = ClojureAntlrParserAdapter().parse_sources({"cqrs.clj": code})
    detections = CommandPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMMAND
    assert detections[0].target_name == "handle-command"
    assert detections[0].confidence.score >= 0.75


def test_builder_pattern_rule() -> None:
    code = """
    (ns my.builder.server)

    (defn make-builder []
      {:host "localhost" :port 8080 :threads 4})

    (defn with-host [builder host]
      (assoc builder :host host))

    (defn with-port [builder port]
      (assoc builder :port port))

    (defn build-server [builder]
      (start-http-server (:host builder) (:port builder)))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"builder.clj": code})
    detections = BuilderPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.BUILDER
    assert detections[0].confidence.score >= 0.65


def test_facade_pattern_rule() -> None:
    code_sub1 = "(ns subsystem.auth (defn authenticate [u p] true))"
    code_sub2 = "(ns subsystem.payment (defn charge [acc amt] true))"
    code_facade = """
    (ns app.ecommerce.api
      (:require [subsystem.auth :as auth]
                [subsystem.payment :as payment]))

    (defn checkout-order [user pass card amount]
      (auth/authenticate user pass)
      (payment/charge card amount))
    """
    model = ClojureAntlrParserAdapter().parse_sources({
        "auth.clj": code_sub1,
        "payment.clj": code_sub2,
        "api.clj": code_facade,
    })
    detections = FacadePatternRule().detect(model)
    assert len(detections) >= 1
    facade_det = next(d for d in detections if d.target_name == "app.ecommerce.api")
    assert facade_det.pattern_type == PatternType.FACADE
    assert facade_det.confidence.score >= 0.60


def test_proxy_pattern_rule() -> None:
    code = """
    (ns my.proxy)

    (defonce lazy-db-connection
      (delay (connect-heavy-database "jdbc://localhost")))

    (defn make-java-runnable [f]
      (proxy [Runnable] []
        (run [] (f))))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"proxy.clj": code})
    detections = ProxyPatternRule().detect(model)
    assert len(detections) >= 2
    types = {d.pattern_type for d in detections}
    assert PatternType.PROXY in types


def test_state_pattern_rule() -> None:
    code = """
    (ns my.fsm)

    (defmulti transition (fn [state event] [(:status state) (:type event)]))

    (defmethod transition [:draft :submit] [state event]
      (assoc state :status :pending-review))

    (defmethod transition [:pending-review :approve] [state event]
      (assoc state :status :published))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"fsm.clj": code})
    detections = StatePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.STATE
    assert detections[0].confidence.score >= 0.70


def test_flyweight_pattern_rule() -> None:
    code = """
    (ns my.flyweight)

    (def get-expensive-font
      (memoize (fn [name size] (load-font-metrics name size))))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"flyweight.clj": code})
    detections = FlyweightPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.FLYWEIGHT
    assert detections[0].confidence.score >= 0.70


def test_abstract_factory_rule() -> None:
    code = """
    (ns my.factory)

    (defprotocol DatabaseFactory
      (create-connection [this config])
      (create-transaction-manager [this conn]))

    (defrecord PostgresFactory []
      DatabaseFactory
      (create-connection [this config] (connect-pg config))
      (create-transaction-manager [this conn] (make-pg-tx conn)))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"factory.clj": code})
    detections = AbstractFactoryRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY
    assert detections[0].confidence.score >= 0.70

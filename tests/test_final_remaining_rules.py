"""Unit tests for the final batch of design pattern rules (Prototype, Composite, Bridge, Iterator, Mediator, Memento, Visitor, Interpreter)."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.domain.rules.bridge_rule import BridgePatternRule
from pattern_detector.domain.rules.composite_rule import CompositePatternRule
from pattern_detector.domain.rules.interpreter_rule import InterpreterPatternRule
from pattern_detector.domain.rules.iterator_rule import IteratorPatternRule
from pattern_detector.domain.rules.mediator_rule import MediatorPatternRule
from pattern_detector.domain.rules.memento_rule import MementoPatternRule
from pattern_detector.domain.rules.prototype_rule import PrototypePatternRule
from pattern_detector.domain.rules.visitor_rule import VisitorPatternRule
from pattern_detector.domain.value_objects import PatternType


def test_prototype_pattern_rule() -> None:
    code = """
    (ns my.prototype)

    (defprotocol Cloneable
      (clone [this overrides]))

    (defrecord ServerConfig [host port ssl]
      Cloneable
      (clone [this overrides]
        (map->ServerConfig (merge this overrides))))

    (defn clone-task-template [proto-task custom-params]
      (merge proto-task custom-params))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"proto.clj": code})
    detections = PrototypePatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.PROTOTYPE for d in detections)


def test_composite_pattern_rule() -> None:
    code = """
    (ns my.composite.ui)

    (defprotocol UiComponent
      (render [this]))

    (defrecord Button [label]
      UiComponent
      (render [this] (str "<button>" label "</button>")))

    (defrecord Panel [children]
      UiComponent
      (render [this]
        (str "<div>" (clojure.string/join (map render children)) "</div>")))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"ui.clj": code})
    detections = CompositePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.COMPOSITE
    assert detections[0].target_name == "UiComponent"
    assert detections[0].confidence.score >= 0.70


def test_bridge_pattern_rule() -> None:
    code = """
    (ns my.bridge.db)

    (defprotocol SqlDriver
      (execute-query [this query-str params]))

    (defrecord DatabaseService [db-driver connection-pool]
      (run-query [this q]
        (execute-query db-driver q [])))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"bridge.clj": code})
    detections = BridgePatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.BRIDGE
    assert detections[0].target_name == "DatabaseService"


def test_iterator_pattern_rule() -> None:
    code = """
    (ns my.iterator.streams)

    (defn fibonacci-seq
      ([] (fibonacci-seq 0 1))
      ([a b]
       (lazy-seq
         (cons a (fibonacci-seq b (+ a b))))))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"iter.clj": code})
    detections = IteratorPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.ITERATOR
    assert detections[0].target_name == "fibonacci-seq"
    assert detections[0].confidence.score >= 0.70


def test_mediator_pattern_rule() -> None:
    code = """
    (ns my.mediator.bus)

    (defprotocol EventBroker
      (publish [this topic message])
      (subscribe [this topic handler]))

    (defrecord CentralEventBus [subscribers-atom]
      EventBroker
      (publish [this topic message]
        (doseq [h (get @subscribers-atom topic)] (h message)))
      (subscribe [this topic handler]
        (swap! subscribers-atom update topic conj handler)))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"bus.clj": code})
    detections = MediatorPatternRule().detect(model)
    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.MEDIATOR for d in detections)


def test_memento_pattern_rule() -> None:
    code = """
    (ns my.memento.history)

    (defn save-snapshot [document-state]
      {:snapshot-id (System/currentTimeMillis)
       :content (:text document-state)
       :cursor-pos (:cursor document-state)})

    (defn restore-snapshot [saved-snapshot]
      {:text (:content saved-snapshot)
       :cursor (:cursor-pos saved-snapshot)})
    """
    model = ClojureAntlrParserAdapter().parse_sources({"history.clj": code})
    detections = MementoPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.MEMENTO


def test_visitor_pattern_rule() -> None:
    code = """
    (ns my.visitor.ast)

    (defmulti visit-ast (fn [node visitor] (:tag node)))

    (defmethod visit-ast :binary-op [node visitor]
      (str "(" (visit-ast (:left node) visitor) " " (:op node) " " (visit-ast (:right node) visitor) ")"))

    (defmethod visit-ast :literal-num [node visitor]
      (str (:val node)))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"ast.clj": code})
    detections = VisitorPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.VISITOR
    assert detections[0].target_name == "visit-ast"
    assert detections[0].confidence.score >= 0.70


def test_interpreter_pattern_rule() -> None:
    code = """
    (ns my.interpreter.eval)

    (defmulti eval-expr (fn [expr env] (:op expr)))

    (defmethod eval-expr :add [expr env]
      (+ (eval-expr (:left expr) env) (eval-expr (:right expr) env)))

    (defmethod eval-expr :mul [expr env]
      (* (eval-expr (:left expr) env) (eval-expr (:right expr) env)))

    (defmethod eval-expr :var [expr env]
      (get env (:name expr)))
    """
    model = ClojureAntlrParserAdapter().parse_sources({"eval.clj": code})
    detections = InterpreterPatternRule().detect(model)
    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.INTERPRETER
    assert detections[0].target_name == "eval-expr"
    assert detections[0].confidence.score >= 0.75

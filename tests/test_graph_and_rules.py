"""Tests for Namespace Dependency Graph, Circular Dependency Detection, and Chain of Responsibility Rule."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.domain.rules.chain_of_responsibility_rule import ChainOfResponsibilityRule
from pattern_detector.domain.rules.circular_dependency_rule import CircularDependencyRule
from pattern_detector.domain.value_objects import PatternType


def test_circular_dependency_detection() -> None:
    # Namespace A requires B, and Namespace B requires A
    code_a = """
    (ns module.alpha
      (:require [module.beta :as beta]))

    (defn alpha-fn []
      (beta/beta-fn))
    """
    code_b = """
    (ns module.beta
      (:require [module.alpha :as alpha]))

    (defn beta-fn []
      (alpha/alpha-fn))
    """

    adapter = ClojureAntlrParserAdapter()
    model = adapter.parse_sources({
        "alpha.clj": code_a,
        "beta.clj": code_b,
    })

    cycles = model.find_circular_dependencies()
    assert len(cycles) == 1
    assert set(cycles[0]) == {"module.alpha", "module.beta"}

    rule = CircularDependencyRule()
    detections = rule.detect(model)
    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CIRCULAR_DEPENDENCY
    assert detections[0].confidence.score >= 0.80
    assert len(detections[0].evidences) == 2


def test_chain_of_responsibility_rule() -> None:
    code = """
    (ns my.app.pipeline)

    (defn wrap-auth [h] (fn [r] (h r)))
    (defn wrap-cors [h] (fn [r] (h r)))
    (defn wrap-json [h] (fn [r] (h r)))

    (defn build-api-pipeline [base-handler]
      (-> base-handler
          wrap-auth
          wrap-cors
          wrap-json))
    """

    adapter = ClojureAntlrParserAdapter()
    model = adapter.parse_sources({"pipeline.clj": code})

    rule = ChainOfResponsibilityRule()
    detections = rule.detect(model)

    assert len(detections) >= 1
    pipeline_det = next(d for d in detections if d.target_name == "build-api-pipeline")
    assert pipeline_det.pattern_type == PatternType.CHAIN_OF_RESPONSIBILITY
    assert pipeline_det.confidence.score >= 0.70
    assert any("middleware" in ev.description.lower() for ev in pipeline_det.evidences)

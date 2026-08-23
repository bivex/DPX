"""Tests for verifying low false positive rate on ordinary, non-pattern Clojure code."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType


def _scan_snippet(code_map: dict[str, str]):
    adapter = ClojureAntlrParserAdapter()
    model = adapter.parse_sources(code_map)
    detector = PatternDetectorService(rules=get_default_rules())
    return detector.detect_all(model)


def test_plain_pure_math_and_string_utilities_have_zero_detections() -> None:
    code = """
    (ns my.math.utils
      (:require [clojure.string :as str]))

    (defn add [a b]
      (+ a b))

    (defn multiply [x y]
      (* x y))

    (defn factorial [n]
      (if (<= n 1)
        1
        (* n (factorial (dec n)))))

    (defn capitalize-words [text]
      (str/join " " (map str/capitalize (str/split text #"\\s+"))))
    """
    report = _scan_snippet({"math.clj": code})

    # Pure standard utilities must not trigger any design patterns
    assert report.total_detections_count == 0


def test_immutable_constants_not_flagged_as_singletons() -> None:
    code = """
    (ns my.config.constants)

    (def app-version "2.4.1")
    (def max-retries 5)
    (def default-timeout-ms 3000)
    (def supported-currencies ["USD" "EUR" "GBP" "JPY"])
    (def api-endpoints {:auth "/api/v1/auth" :users "/api/v1/users"})
    """
    report = _scan_snippet({"config.clj": code})

    # Plain def constants without atom/ref/defonce must NOT be singletons
    singleton_detections = [d for d in report.detections if d.pattern_type == PatternType.SINGLETON]
    assert len(singleton_detections) == 0


def test_plain_records_without_protocols_not_flagged_as_lifecycle_or_strategy() -> None:
    code = """
    (ns my.domain.models)

    (defrecord Point [x y])
    (defrecord UserProfile [id username email created-at])
    (defrecord OrderItem [sku quantity price])
    """
    report = _scan_snippet({"models.clj": code})

    # Plain data records without Lifecycle or Strategy protocols must not trigger Lifecycle/Strategy
    invalid_detections = [
        d for d in report.detections
        if d.pattern_type in (PatternType.LIFECYCLE_COMPONENT, PatternType.STRATEGY, PatternType.ADAPTER)
    ]
    assert len(invalid_detections) == 0


def test_string_helpers_with_make_or_create_name_not_flagged_as_factory() -> None:
    code = """
    (ns my.string.helpers
      (:require [clojure.string :as str]))

    (defn make-uppercase [s]
      (str/upper-case s))

    (defn create-slug [title]
      (-> title
          str/lower-case
          (str/replace #"[^a-z0-9]+" "-")
          (str/replace #"^-|-$" "")))

    (defn build-url [base path]
      (str base "/" path))
    """
    report = _scan_snippet({"helpers.clj": code})

    # Functions returning pure strings without record instantiations must not be factory methods
    factory_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.FACTORY_METHOD and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(factory_detections) == 0


def test_standard_higher_order_functions_not_flagged_as_decorator() -> None:
    code = """
    (ns my.fp.utils)

    (defn apply-twice [f x]
      (f (f x)))

    (defn map-values [f m]
      (into {} (for [[k v] m] [k (f v)])))

    (defn filter-by-pred [pred coll]
      (filter pred coll))
    """
    report = _scan_snippet({"fp.clj": code})

    # Standard higher-order utility functions (not returning closures wrapping request handlers) must not be decorators
    decorator_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.DECORATOR and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(decorator_detections) == 0


def test_acyclic_dependency_graph_has_zero_circular_dependencies() -> None:
    code_a = """
    (ns service.controller
      (:require [service.business :as biz]))
    (defn handle-req [req] (biz/calculate req))
    """
    code_b = """
    (ns service.business
      (:require [service.repo :as repo]))
    (defn calculate [req] (repo/fetch (:id req)))
    """
    code_c = """
    (ns service.repo)
    (defn fetch [id] {:id id :name "Test"})
    """

    report = _scan_snippet({
        "controller.clj": code_a,
        "business.clj": code_b,
        "repo.clj": code_c,
    })

    # Pure acyclic hierarchy (Controller -> Business -> Repo) must have 0 circular dependency detections
    cycle_detections = [d for d in report.detections if d.pattern_type == PatternType.CIRCULAR_DEPENDENCY]
    assert len(cycle_detections) == 0


def test_macro_without_try_finally_not_flagged_as_template_method() -> None:
    code = """
    (ns my.macros)

    (defmacro when-valid [pred value & body]
      `(if (~pred ~value)
         (do ~@body)
         nil))

    (defmacro debug-print [expr]
      `(let [val# ~expr]
         (println "DEBUG:" '~expr "=" val#)
         val#))
    """
    report = _scan_snippet({"macros.clj": code})

    # General branching macros without resource bracket try/finally must not be template methods
    template_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.TEMPLATE_METHOD and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(template_detections) == 0

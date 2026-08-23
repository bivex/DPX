"""Tests for ANTLR Clojure Parser Adapter."""

from pattern_detector.adapters.outbound.antlr import ClojureAntlrParserAdapter


def test_parse_namespace_and_states() -> None:
    code = """
    (ns my.sample.app
      "Sample namespace docstring"
      (:require [clojure.string :as str]))

    (defonce app-state (atom {:count 0}))
    (def ^:dynamic *current-user* "guest")
    """
    adapter = ClojureAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="sample.clj")

    assert ns.name == "my.sample.app"
    assert ns.docstring == "Sample namespace docstring"
    assert len(ns.requires) >= 1

    assert "app-state" in ns.states
    state = ns.states["app-state"]
    assert state.is_once is True
    assert state.kind == "atom"

    assert "*current-user*" in ns.states


def test_parse_protocol_and_records() -> None:
    code = """
    (ns my.repo)

    (defprotocol Repository
      "Data access protocol"
      (find-by-id [this id] "Finds item by id")
      (save-item [this item] [this item options]))

    (defrecord MemoryRepository [storage]
      Repository
      (find-by-id [this id]
        (get storage id))
      (save-item [this item]
        (assoc storage (:id item) item)))
    """
    adapter = ClojureAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="repo.clj")

    assert "Repository" in ns.protocols
    proto = ns.protocols["Repository"]
    assert proto.name == "Repository"
    assert len(proto.methods) == 2
    assert proto.has_method("find-by-id")
    assert proto.has_method("save-item")

    assert "MemoryRepository" in ns.records
    rec = ns.records["MemoryRepository"]
    assert rec.name == "MemoryRepository"
    assert rec.fields == ["storage"]
    assert rec.implements_protocol("Repository")
    assert len(rec.methods) == 2


def test_parse_multimethods() -> None:
    code = """
    (ns my.dispatch)

    (defmulti render-component (fn [comp] (:type comp)))

    (defmethod render-component :button [comp]
      (str "<button>" (:label comp) "</button>"))

    (defmethod render-component :input [comp]
      (str "<input type='text' value='" (:val comp) "'/>"))
    """
    adapter = ClojureAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="dispatch.clj")

    assert "render-component" in ns.multimethods
    mm_list = ns.multimethods["render-component"]
    # 1 declaration + 2 method branches
    assert len(mm_list) == 3

    branches = [m for m in mm_list if m.dispatch_val]
    assert len(branches) == 2
    assert {b.dispatch_val for b in branches} == {":button", ":input"}


def test_parse_functions_and_closures() -> None:
    code = """
    (ns my.server)

    (defn wrap-cors [handler]
      (fn [req]
        (let [resp (handler req)]
          (assoc-in resp [:headers "Access-Control-Allow-Origin"] "*"))))
    """
    adapter = ClojureAntlrParserAdapter()
    ns = adapter.parse_source(code, file_path="server.clj")

    assert "wrap-cors" in ns.functions
    fn_model = ns.functions["wrap-cors"]
    assert fn_model.parameter_lists == [["handler"]]
    assert fn_model.returns_closure is True
    assert "handler" in fn_model.calls

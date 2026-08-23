"""Agnostic Domain Code Model.

Represents structural and semantic constructs (Protocols, Records/Classes,
Functions, State, Invocations, Namespaces, Dependency Graphs) parsed from source code
without direct dependency on any AST framework.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class MethodSignature:
    """Represents a method signature inside a protocol/interface."""

    name: str
    parameter_lists: list[list[str]] = field(default_factory=list)
    docstring: str | None = None
    location: SourceLocation | None = None


@dataclass
class FunctionInvocation:
    """Represents a function or constructor call in the code."""

    caller_name: str
    target_name: str
    location: SourceLocation
    argument_count: int = 0
    argument_snippets: list[str] = field(default_factory=list)


@dataclass
class FunctionModel:
    """Represents a function, method, multimethod implementation, or macro."""

    name: str
    namespace: str
    location: SourceLocation
    docstring: str | None = None
    is_private: bool = False
    is_macro: bool = False
    is_multimethod: bool = False
    dispatch_fn: str | None = None
    dispatch_val: str | None = None
    parent_multimethod: str | None = None
    parameter_lists: list[list[str]] = field(default_factory=list)
    body_text: str = ""
    calls: list[str] = field(default_factory=list)
    invocations: list[FunctionInvocation] = field(default_factory=list)
    returns_closure: bool = False
    instantiates_types: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    @property
    def qualified_name(self) -> str:
        return f"{self.namespace}/{self.name}" if self.namespace else self.name


@dataclass
class ProtocolModel:
    """Represents a protocol, interface, or abstract trait definition."""

    name: str
    namespace: str
    location: SourceLocation
    docstring: str | None = None
    methods: list[MethodSignature] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    @property
    def qualified_name(self) -> str:
        return f"{self.namespace}/{self.name}" if self.namespace else self.name

    def has_method(self, name: str) -> bool:
        return any(m.name == name for m in self.methods)


@dataclass
class RecordModel:
    """Represents a defrecord, deftype, or class struct."""

    name: str
    namespace: str
    location: SourceLocation
    fields: list[str] = field(default_factory=list)
    implemented_protocols: list[str] = field(default_factory=list)
    methods: list[FunctionModel] = field(default_factory=list)
    is_type: bool = False
    docstring: str | None = None

    @property
    def qualified_name(self) -> str:
        return f"{self.namespace}/{self.name}" if self.namespace else self.name

    def implements_protocol(self, protocol_name: str) -> bool:
        norm = protocol_name.split("/")[-1]
        return any(p == protocol_name or p.split("/")[-1] == norm for p in self.implemented_protocols)


@dataclass
class ProtocolExtensionModel:
    """Represents an external protocol extension (extend-type / extend-protocol)."""

    target_type: str
    protocol_name: str
    namespace: str
    location: SourceLocation
    methods: list[FunctionModel] = field(default_factory=list)


@dataclass
class StateModel:
    """Represents a state holder or global binding (atom, ref, agent, defonce, var)."""

    name: str
    namespace: str
    location: SourceLocation
    kind: str  # "atom", "ref", "agent", "var", "defonce", "delay", "promise"
    initial_expr: str | None = None
    is_once: bool = False
    is_dynamic: bool = False
    watchers: list[str] = field(default_factory=list)

    @property
    def qualified_name(self) -> str:
        return f"{self.namespace}/{self.name}" if self.namespace else self.name


@dataclass
class WatchModel:
    """Represents an observer watcher subscription (add-watch)."""

    target_state_name: str
    watch_key: str
    callback_fn_name: str
    location: SourceLocation


@dataclass
class NamespaceModel:
    """Represents a single namespace / file module."""

    name: str
    file_path: str
    docstring: str | None = None
    requires: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    protocols: dict[str, ProtocolModel] = field(default_factory=dict)
    records: dict[str, RecordModel] = field(default_factory=dict)
    extensions: list[ProtocolExtensionModel] = field(default_factory=list)
    functions: dict[str, FunctionModel] = field(default_factory=dict)
    multimethods: dict[str, list[FunctionModel]] = field(default_factory=dict)
    states: dict[str, StateModel] = field(default_factory=dict)
    watches: list[WatchModel] = field(default_factory=list)


@dataclass
class CodeModel:
    """Aggregate Root representing the whole scanned codebase."""

    namespaces: dict[str, NamespaceModel] = field(default_factory=dict)

    def add_namespace(self, ns: NamespaceModel) -> None:
        self.namespaces[ns.name] = ns

    def get_namespace(self, name: str) -> NamespaceModel | None:
        return self.namespaces.get(name)

    def all_functions(self) -> list[FunctionModel]:
        res: list[FunctionModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.functions.values())
            for mm_methods in ns.multimethods.values():
                res.extend(mm_methods)
            for rec in ns.records.values():
                res.extend(rec.methods)
            for ext in ns.extensions:
                res.extend(ext.methods)
        return res

    def all_protocols(self) -> list[ProtocolModel]:
        res: list[ProtocolModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.protocols.values())
        return res

    def all_records(self) -> list[RecordModel]:
        res: list[RecordModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.records.values())
        return res

    def all_extensions(self) -> list[ProtocolExtensionModel]:
        res: list[ProtocolExtensionModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.extensions)
        return res

    def all_states(self) -> list[StateModel]:
        res: list[StateModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.states.values())
        return res

    def all_watches(self) -> list[WatchModel]:
        res: list[WatchModel] = []
        for ns in self.namespaces.values():
            res.extend(ns.watches)
        return res

    def find_protocol(self, name: str) -> ProtocolModel | None:
        norm = name.split("/")[-1]
        for ns in self.namespaces.values():
            if name in ns.protocols:
                return ns.protocols[name]
            for p_name, proto in ns.protocols.items():
                if p_name == norm or proto.name == norm:
                    return proto
        return None

    def find_records_implementing(self, protocol_name: str) -> list[RecordModel]:
        return [rec for rec in self.all_records() if rec.implements_protocol(protocol_name)]

    def find_callers_of(self, fn_name: str) -> list[FunctionModel]:
        norm = fn_name.split("/")[-1]
        callers: list[FunctionModel] = []
        for fn in self.all_functions():
            if any(call == fn_name or call.split("/")[-1] == norm for call in fn.calls):
                callers.append(fn)
        return callers

    # -------------------------------------------------------------------------
    # Graph & Cross-Namespace Dependency Analysis
    # -------------------------------------------------------------------------

    def build_namespace_dependency_graph(self) -> dict[str, set[str]]:
        """Build directed adjacency map of namespace dependencies: source_ns -> {target_ns, ...}."""
        graph: dict[str, set[str]] = {ns_name: set() for ns_name in self.namespaces}
        all_ns_names = set(self.namespaces.keys())

        for ns_name, ns in self.namespaces.items():
            # 1. Inspect explicit requires
            for req in ns.requires:
                # Match required namespace names (e.g. "[foo.bar :as b]" or "foo.bar")
                matches = re.findall(r"[a-zA-Z0-9_\.\-]+", req)
                if matches:
                    dep_name = matches[0].strip("[]()")
                    if dep_name in all_ns_names and dep_name != ns_name:
                        graph[ns_name].add(dep_name)

            # 2. Inspect qualified function calls
            for fn in ns.functions.values():
                for call in fn.calls:
                    if "/" in call:
                        prefix = call.split("/")[0]
                        if prefix in all_ns_names and prefix != ns_name:
                            graph[ns_name].add(prefix)

        return graph

    def find_circular_dependencies(self) -> list[list[str]]:
        """Detect all simple circular dependency cycles between namespaces."""
        graph = self.build_namespace_dependency_graph()
        cycles: list[list[str]] = []
        visited: set[str] = set()

        def _dfs(current: str, path: list[str], path_set: set[str]) -> None:
            path.append(current)
            path_set.add(current)

            for neighbor in sorted(graph.get(current, set())):
                if neighbor == path[0] and len(path) >= 2:
                    # Found cycle back to origin
                    cycles.append(list(path))
                elif neighbor not in path_set and neighbor not in visited:
                    _dfs(neighbor, path, path_set)

            path.pop()
            path_set.remove(current)

        for node in sorted(graph.keys()):
            _dfs(node, [], set())
            visited.add(node)

        # Deduplicate rotationally equivalent cycles
        unique_cycles: list[list[str]] = []
        seen_cycle_keys: set[tuple[str, ...]] = set()

        for c in cycles:
            # Canonical cycle representation by smallest element first
            min_idx = c.index(min(c))
            canonical = tuple(c[min_idx:] + c[:min_idx])
            if canonical not in seen_cycle_keys:
                seen_cycle_keys.add(canonical)
                unique_cycles.append(c)

        return unique_cycles

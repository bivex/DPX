"""ANTLR Outbound Adapter implementing ParserPort for Clojure."""

from __future__ import annotations

import antlr4

from pattern_detector.adapters.outbound.antlr.clojure_ast import (
    ASTNode,
    ListNode,
    MapNode,
    ReaderMacroNode,
    SetNode,
    StringNode,
    SymbolNode,
    TaggedNode,
    VectorNode,
)
from pattern_detector.adapters.outbound.antlr.clojure_visitor import ClojureASTVisitor
from pattern_detector.adapters.outbound.antlr.generated.ClojureLexer import ClojureLexer
from pattern_detector.adapters.outbound.antlr.generated.ClojureParser import ClojureParser
from pattern_detector.domain.code_model import (
    CodeModel,
    FunctionInvocation,
    FunctionModel,
    MethodSignature,
    NamespaceModel,
    ProtocolExtensionModel,
    ProtocolModel,
    RecordModel,
    StateModel,
    WatchModel,
)
from pattern_detector.ports.outbound import ParserPort


class ClojureAntlrParserAdapter(ParserPort):
    """Parses Clojure source code into agnostic domain CodeModel via ANTLR4."""

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        """Parse single Clojure source file into a NamespaceModel."""
        input_stream = antlr4.InputStream(source_code)
        lexer = ClojureLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = ClojureParser(stream)
        # Suppress syntax error spam in console
        parser.removeErrorListeners()

        tree = parser.file_()
        visitor = ClojureASTVisitor(file_path=file_path)
        ast_nodes = visitor.visitFile_(tree)

        ns_model = NamespaceModel(
            name="user",
            file_path=file_path,
        )

        for node in ast_nodes:
            if isinstance(node, ListNode) and node.items:
                self._process_top_level_form(node, ns_model)

        return ns_model

    def parse_sources(self, sources: dict[str, str]) -> CodeModel:
        """Parse multiple Clojure files into an aggregate CodeModel."""
        code_model = CodeModel()
        for file_path, content in sources.items():
            ns_model = self.parse_source(content, file_path=file_path)
            if ns_model.name == "user":
                ns_model.name = f"user_{file_path}"
            code_model.add_namespace(ns_model)
        return code_model

    # -------------------------------------------------------------------------
    # Form Processing Internals
    # -------------------------------------------------------------------------

    def _process_top_level_form(self, form: ListNode, ns: NamespaceModel) -> None:
        head = form.head_symbol
        if not head:
            return

        match head:
            case "ns":
                self._extract_ns(form, ns)
            case "defprotocol":
                self._extract_defprotocol(form, ns)
            case "defrecord" | "deftype":
                self._extract_defrecord(form, ns, is_type=(head == "deftype"))
            case "extend-type":
                self._extract_extend_type(form, ns)
            case "extend-protocol":
                self._extract_extend_protocol(form, ns)
            case "defmulti":
                self._extract_defmulti(form, ns)
            case "defmethod":
                self._extract_defmethod(form, ns)
            case "defn" | "defn-" | "defmacro":
                self._extract_defn(form, ns, is_private=(head == "defn-"), is_macro=(head == "defmacro"))
            case "def" | "defonce":
                self._extract_def(form, ns, is_once=(head == "defonce"))
            case "add-watch":
                self._extract_add_watch(form, ns)
            case _:
                # Check if top-level expression contains embedded add-watch or def
                self._scan_for_embedded_watches(form, ns)

    def _resolve_symbol_name(self, node: ASTNode) -> str | None:
        if isinstance(node, SymbolNode):
            return node.name
        if isinstance(node, TaggedNode):
            return node.symbol_name
        return None

    def _extract_ns(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if not items:
            return

        idx = 0
        sym = self._resolve_symbol_name(items[idx])
        if sym:
            ns.name = sym
            idx += 1

        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, StringNode):
                ns.docstring = first_node.value
                idx += 1

        for clause in items[idx:]:
            if isinstance(clause, ListNode) and clause.items:
                head = clause.head_symbol or (clause.items[0].to_text() if clause.items else "")
                norm_head = head.lstrip(":")
                if norm_head in ("require", "use"):
                    ns.requires.extend(item.to_text() for item in clause.items[1:])
                elif norm_head in ("import",):
                    ns.imports.extend(item.to_text() for item in clause.items[1:])

    def _extract_defprotocol(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if not items:
            return

        proto_name = self._resolve_symbol_name(items[0])
        if not proto_name:
            return

        docstring: str | None = None
        idx = 1
        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, StringNode):
                docstring = first_node.value
                idx += 1

        methods: list[MethodSignature] = []
        for m_form in items[idx:]:
            if isinstance(m_form, ListNode) and m_form.items:
                m_sym = self._resolve_symbol_name(m_form.items[0])
                if not m_sym:
                    continue
                m_name = m_sym
                m_doc: str | None = None
                param_lists: list[list[str]] = []

                for sub in m_form.items[1:]:
                    if isinstance(sub, VectorNode):
                        param_lists.append([s.to_text() for s in sub.items])
                    elif isinstance(sub, StringNode):
                        m_doc = sub.value

                methods.append(
                    MethodSignature(
                        name=m_name,
                        parameter_lists=param_lists,
                        docstring=m_doc,
                        location=m_form.location,
                    )
                )

        proto_model = ProtocolModel(
            name=proto_name,
            namespace=ns.name,
            location=form.location,
            docstring=docstring,
            methods=methods,
        )
        ns.protocols[proto_name] = proto_model

    def _extract_defrecord(self, form: ListNode, ns: NamespaceModel, is_type: bool = False) -> None:
        items = form.items[1:]
        if not items:
            return

        rec_name = self._resolve_symbol_name(items[0])
        if not rec_name:
            return

        fields: list[str] = []
        implemented_protos: list[str] = []
        methods: list[FunctionModel] = []

        idx = 1
        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, VectorNode):
                fields = [s.to_text() for s in first_node.items]
                idx += 1

        for item in items[idx:]:
            item_sym = self._resolve_symbol_name(item)
            if item_sym and isinstance(item, (SymbolNode, TaggedNode)):
                implemented_protos.append(item_sym)
            elif isinstance(item, ListNode) and item.items:
                m_sym = self._resolve_symbol_name(item.items[0])
                if not m_sym:
                    continue
                m_name = m_sym
                m_params: list[list[str]] = []
                body_start = 1
                if len(item.items) > 1 and isinstance(item.items[1], VectorNode):
                    m_params = [[p.to_text() for p in item.items[1].items]]
                    body_start = 2

                calls = self._collect_symbols(item.items[body_start:])
                invocations = self._collect_invocations(item.items[body_start:], caller_name=f"{rec_name}/{m_name}")

                fn_model = FunctionModel(
                    name=m_name,
                    namespace=ns.name,
                    location=item.location,
                    parameter_lists=m_params,
                    body_text=item.to_text(),
                    calls=calls,
                    invocations=invocations,
                )
                methods.append(fn_model)

        rec_model = RecordModel(
            name=rec_name,
            namespace=ns.name,
            location=form.location,
            fields=fields,
            implemented_protocols=implemented_protos,
            methods=methods,
            is_type=is_type,
        )
        ns.records[rec_name] = rec_model

    def _extract_extend_type(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if len(items) < 2:
            return

        target_type = self._resolve_symbol_name(items[0])
        if not target_type:
            return

        current_proto: str | None = None
        current_methods: list[FunctionModel] = []

        for item in items[1:]:
            item_sym = self._resolve_symbol_name(item)
            if item_sym and isinstance(item, (SymbolNode, TaggedNode)):
                if current_proto:
                    ns.extensions.append(
                        ProtocolExtensionModel(
                            target_type=target_type,
                            protocol_name=current_proto,
                            namespace=ns.name,
                            location=form.location,
                            methods=current_methods,
                        )
                    )
                    current_methods = []
                current_proto = item_sym
            elif isinstance(item, ListNode) and item.items:
                m_sym = self._resolve_symbol_name(item.items[0])
                if not m_sym:
                    continue
                m_name = m_sym
                m_params: list[list[str]] = []
                body_start = 1
                if len(item.items) > 1 and isinstance(item.items[1], VectorNode):
                    m_params = [[p.to_text() for p in item.items[1].items]]
                    body_start = 2
                calls = self._collect_symbols(item.items[body_start:])
                fn_model = FunctionModel(
                    name=m_name,
                    namespace=ns.name,
                    location=item.location,
                    parameter_lists=m_params,
                    body_text=item.to_text(),
                    calls=calls,
                )
                current_methods.append(fn_model)

        if current_proto:
            ns.extensions.append(
                ProtocolExtensionModel(
                    target_type=target_type,
                    protocol_name=current_proto,
                    namespace=ns.name,
                    location=form.location,
                    methods=current_methods,
                )
            )

    def _extract_extend_protocol(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if len(items) < 2:
            return

        proto_name = self._resolve_symbol_name(items[0])
        if not proto_name:
            return

        current_type: str | None = None
        current_methods: list[FunctionModel] = []

        for item in items[1:]:
            item_sym = self._resolve_symbol_name(item)
            if item_sym and isinstance(item, (SymbolNode, TaggedNode)):
                if current_type:
                    ns.extensions.append(
                        ProtocolExtensionModel(
                            target_type=current_type,
                            protocol_name=proto_name,
                            namespace=ns.name,
                            location=form.location,
                            methods=current_methods,
                        )
                    )
                    current_methods = []
                current_type = item_sym
            elif isinstance(item, ListNode) and item.items:
                m_sym = self._resolve_symbol_name(item.items[0])
                if not m_sym:
                    continue
                m_name = m_sym
                m_params: list[list[str]] = []
                body_start = 1
                if len(item.items) > 1 and isinstance(item.items[1], VectorNode):
                    m_params = [[p.to_text() for p in item.items[1].items]]
                    body_start = 2
                calls = self._collect_symbols(item.items[body_start:])
                fn_model = FunctionModel(
                    name=m_name,
                    namespace=ns.name,
                    location=item.location,
                    parameter_lists=m_params,
                    body_text=item.to_text(),
                    calls=calls,
                )
                current_methods.append(fn_model)

        if current_type:
            ns.extensions.append(
                ProtocolExtensionModel(
                    target_type=current_type,
                    protocol_name=proto_name,
                    namespace=ns.name,
                    location=form.location,
                    methods=current_methods,
                )
            )

    def _extract_defmulti(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if not items:
            return

        mm_name = self._resolve_symbol_name(items[0])
        if not mm_name:
            return

        docstring: str | None = None
        idx = 1
        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, StringNode):
                docstring = first_node.value
                idx += 1

        dispatch_fn_str = items[idx].to_text() if idx < len(items) else None

        fn_model = FunctionModel(
            name=mm_name,
            namespace=ns.name,
            location=form.location,
            docstring=docstring,
            is_multimethod=True,
            dispatch_fn=dispatch_fn_str,
            body_text=form.to_text(),
        )

        if mm_name not in ns.multimethods:
            ns.multimethods[mm_name] = []
        ns.multimethods[mm_name].append(fn_model)

    def _extract_defmethod(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if len(items) < 3:
            return

        mm_name = self._resolve_symbol_name(items[0])
        if not mm_name:
            return

        dispatch_val = items[1].to_text()
        idx = 2

        params: list[list[str]] = []
        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, VectorNode):
                params = [[p.to_text() for p in first_node.items]]
                idx += 1

        calls = self._collect_symbols(items[idx:])
        invocations = self._collect_invocations(items[idx:], caller_name=f"{mm_name}:{dispatch_val}")

        fn_model = FunctionModel(
            name=f"{mm_name}:{dispatch_val}",
            namespace=ns.name,
            location=form.location,
            parent_multimethod=mm_name,
            dispatch_val=dispatch_val,
            parameter_lists=params,
            body_text=form.to_text(),
            calls=calls,
            invocations=invocations,
        )

        if mm_name not in ns.multimethods:
            ns.multimethods[mm_name] = []
        ns.multimethods[mm_name].append(fn_model)

    def _extract_defn(self, form: ListNode, ns: NamespaceModel, is_private: bool = False, is_macro: bool = False) -> None:
        items = form.items[1:]
        if not items:
            return

        fn_name = self._resolve_symbol_name(items[0])
        if not fn_name:
            return

        docstring: str | None = None
        idx = 1

        if idx < len(items):
            first_node = items[idx]
            if isinstance(first_node, StringNode):
                docstring = first_node.value
                idx += 1

        parameter_lists: list[list[str]] = []
        body_nodes: list[ASTNode] = []

        if idx < len(items) and isinstance(items[idx], VectorNode):
            # Single arity: (defn name [args] body...)
            vec_node = items[idx]
            if isinstance(vec_node, VectorNode):
                parameter_lists.append([p.to_text() for p in vec_node.items])
            idx += 1
            body_nodes = items[idx:]
        else:
            # Multi arity: (defn name ([a] ...) ([a b] ...))
            for item in items[idx:]:
                if isinstance(item, ListNode) and item.items:
                    item_head = item.items[0]
                    if isinstance(item_head, VectorNode):
                        parameter_lists.append([p.to_text() for p in item_head.items])
                        body_nodes.extend(item.items[1:])

        calls = self._collect_symbols(body_nodes)
        invocations = self._collect_invocations(body_nodes, caller_name=fn_name)
        returns_closure = self._detect_closure_return(body_nodes)
        instantiates_types = [c.lstrip("->").lstrip("map->").rstrip(".") for c in calls if c.startswith(("->", "map->")) or c.endswith(".")]

        # Also check for add-watch calls inside function body
        self._scan_for_embedded_watches(form, ns)

        fn_model = FunctionModel(
            name=fn_name,
            namespace=ns.name,
            location=form.location,
            docstring=docstring,
            is_private=is_private,
            is_macro=is_macro,
            parameter_lists=parameter_lists,
            body_text=form.to_text(),
            calls=calls,
            invocations=invocations,
            returns_closure=returns_closure,
            instantiates_types=instantiates_types,
        )
        ns.functions[fn_name] = fn_model

    def _extract_def(self, form: ListNode, ns: NamespaceModel, is_once: bool = False) -> None:
        items = form.items[1:]
        if not items:
            return

        first_node = items[0]
        var_name = self._resolve_symbol_name(first_node)
        if not var_name:
            return

        is_dynamic = False
        if isinstance(first_node, TaggedNode):
            tag_text = first_node.tag.to_text()
            if "dynamic" in tag_text:
                is_dynamic = True

        kind = "defonce" if is_once else "var"
        initial_expr: str | None = None

        if len(items) > 1:
            val_node = items[1]
            initial_expr = val_node.to_text()
            if isinstance(val_node, ListNode) and val_node.head_symbol:
                h = val_node.head_symbol
                if h in ("atom", "ref", "agent", "delay", "promise"):
                    kind = h

        state_model = StateModel(
            name=var_name,
            namespace=ns.name,
            location=form.location,
            kind=kind,
            initial_expr=initial_expr,
            is_once=is_once,
            is_dynamic=is_dynamic,
        )
        ns.states[var_name] = state_model

    def _extract_add_watch(self, form: ListNode, ns: NamespaceModel) -> None:
        items = form.items[1:]
        if len(items) < 3:
            return

        target_name = items[0].to_text().lstrip("@")
        watch_key = items[1].to_text().lstrip(":")
        callback_name = items[2].to_text()

        watch_model = WatchModel(
            target_state_name=target_name,
            watch_key=watch_key,
            callback_fn_name=callback_name,
            location=form.location,
        )
        ns.watches.append(watch_model)

        # If target state is in the namespace, record watcher key
        if target_name in ns.states:
            ns.states[target_name].watchers.append(watch_key)

    def _scan_for_embedded_watches(self, node: ASTNode, ns: NamespaceModel) -> None:
        if isinstance(node, ListNode):
            if node.head_symbol == "add-watch":
                self._extract_add_watch(node, ns)
            for item in node.items:
                self._scan_for_embedded_watches(item, ns)
        elif isinstance(node, (VectorNode, SetNode)):
            for item in node.items:
                self._scan_for_embedded_watches(item, ns)
        elif isinstance(node, MapNode):
            for k, v in node.pairs:
                self._scan_for_embedded_watches(k, ns)
                self._scan_for_embedded_watches(v, ns)
        elif isinstance(node, TaggedNode):
            self._scan_for_embedded_watches(node.tag, ns)
            self._scan_for_embedded_watches(node.target, ns)
        elif isinstance(node, ReaderMacroNode) and node.inner:
            self._scan_for_embedded_watches(node.inner, ns)

    # -------------------------------------------------------------------------
    # Helper AST Collectors
    # -------------------------------------------------------------------------

    def _collect_symbols(self, nodes: list[ASTNode]) -> list[str]:
        symbols: set[str] = set()

        def _traverse(n: ASTNode) -> None:
            if isinstance(n, SymbolNode):
                symbols.add(n.name)
            elif isinstance(n, TaggedNode):
                _traverse(n.tag)
                _traverse(n.target)
            elif isinstance(n, (ListNode, VectorNode, SetNode)):
                for item in n.items:
                    _traverse(item)
            elif isinstance(n, MapNode):
                for k, v in n.pairs:
                    _traverse(k)
                    _traverse(v)
            elif isinstance(n, ReaderMacroNode) and n.inner:
                _traverse(n.inner)

        for node in nodes:
            _traverse(node)

        return sorted(symbols)

    def _collect_invocations(self, nodes: list[ASTNode], caller_name: str) -> list[FunctionInvocation]:
        invocations: list[FunctionInvocation] = []

        def _traverse(n: ASTNode) -> None:
            if isinstance(n, ListNode) and n.head_symbol:
                args = [item.to_text() for item in n.items[1:]]
                invocations.append(
                    FunctionInvocation(
                        caller_name=caller_name,
                        target_name=n.head_symbol,
                        location=n.location,
                        argument_count=len(args),
                        argument_snippets=args[:4],
                    )
                )
                for item in n.items[1:]:
                    _traverse(item)
            elif isinstance(n, TaggedNode):
                _traverse(n.target)
            elif isinstance(n, (VectorNode, SetNode)):
                for item in n.items:
                    _traverse(item)
            elif isinstance(n, MapNode):
                for k, v in n.pairs:
                    _traverse(k)
                    _traverse(v)
            elif isinstance(n, ReaderMacroNode) and n.inner:
                _traverse(n.inner)

        for node in nodes:
            _traverse(node)

        return invocations

    def _detect_closure_return(self, nodes: list[ASTNode]) -> bool:
        """Inspect if the function body returns an inner (fn ...) or comp/partial."""
        if not nodes:
            return False

        last_node = nodes[-1]

        def _is_closure_form(n: ASTNode) -> bool:
            if isinstance(n, ListNode) and n.head_symbol:
                if n.head_symbol in ("fn", "fn*", "comp", "partial"):
                    return True
                # Check inside let / if / do tail expressions
                if n.head_symbol in ("let", "let*", "do", "when", "if", "cond") and n.items:
                    return any(_is_closure_form(item) for item in n.items[1:])
            elif isinstance(n, ReaderMacroNode) and n.macro_type == "#":
                return True
            elif isinstance(n, TaggedNode):
                return _is_closure_form(n.target)
            return False

        return _is_closure_form(last_node)

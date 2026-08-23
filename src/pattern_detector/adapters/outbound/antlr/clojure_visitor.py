"""ANTLR Visitor converting Clojure ParseTree to ASTNode hierarchy."""

from __future__ import annotations

from typing import Any

from pattern_detector.adapters.outbound.antlr.clojure_ast import (
    ASTNode,
    KeywordNode,
    ListNode,
    LiteralNode,
    MapNode,
    NumberNode,
    ReaderMacroNode,
    SetNode,
    StringNode,
    SymbolNode,
    TaggedNode,
    VectorNode,
)
from pattern_detector.adapters.outbound.antlr.generated.ClojureParser import ClojureParser
from pattern_detector.adapters.outbound.antlr.generated.ClojureVisitor import ClojureVisitor
from pattern_detector.domain.value_objects import SourceLocation


class ClojureASTVisitor(ClojureVisitor):
    """Visits ANTLR parse tree and creates clean, pythonic ASTNode tree."""

    def __init__(self, file_path: str = "") -> None:
        super().__init__()
        self._file_path = file_path

    def _loc(self, ctx: Any) -> SourceLocation:
        start_line = ctx.start.line if hasattr(ctx, "start") and ctx.start else 1
        start_col = (ctx.start.column + 1) if hasattr(ctx, "start") and ctx.start else 1
        stop_line = ctx.stop.line if hasattr(ctx, "stop") and ctx.stop else start_line
        stop_col = (ctx.stop.column + 1) if hasattr(ctx, "stop") and ctx.stop else start_col
        return SourceLocation(
            file_path=self._file_path,
            line=start_line,
            column=start_col,
            end_line=stop_line,
            end_column=stop_col,
        )

    def visitFile_(self, ctx: ClojureParser.File_Context) -> list[ASTNode]:
        nodes: list[ASTNode] = []
        if ctx.form():
            for f in ctx.form():
                res = self.visit(f)
                if res is not None and isinstance(res, ASTNode):
                    nodes.append(res)
        return nodes

    def visitForm(self, ctx: ClojureParser.FormContext) -> ASTNode | None:
        if ctx.list_():
            return self.visit(ctx.list_())
        if ctx.vector():
            return self.visit(ctx.vector())
        if ctx.map_():
            return self.visit(ctx.map_())
        if ctx.reader_macro():
            return self.visit(ctx.reader_macro())
        if ctx.literal():
            return self.visit(ctx.literal())
        return None

    def visitForms(self, ctx: ClojureParser.FormsContext) -> list[ASTNode]:
        nodes: list[ASTNode] = []
        if ctx.form():
            for f in ctx.form():
                res = self.visit(f)
                if res is not None and isinstance(res, ASTNode):
                    nodes.append(res)
        return nodes

    def visitList_(self, ctx: ClojureParser.List_Context) -> ListNode:
        forms_ctx = ctx.forms()
        items = self.visit(forms_ctx) if forms_ctx else []
        return ListNode(location=self._loc(ctx), items=items if isinstance(items, list) else [])

    def visitVector(self, ctx: ClojureParser.VectorContext) -> VectorNode:
        forms_ctx = ctx.forms()
        items = self.visit(forms_ctx) if forms_ctx else []
        return VectorNode(location=self._loc(ctx), items=items if isinstance(items, list) else [])

    def visitMap_(self, ctx: ClojureParser.Map_Context) -> MapNode:
        forms = ctx.form()
        pairs: list[tuple[ASTNode, ASTNode]] = []
        if forms:
            for i in range(0, len(forms) - 1, 2):
                k = self.visit(forms[i])
                v = self.visit(forms[i + 1])
                if isinstance(k, ASTNode) and isinstance(v, ASTNode):
                    pairs.append((k, v))
        return MapNode(location=self._loc(ctx), pairs=pairs)

    def visitSet_(self, ctx: ClojureParser.Set_Context) -> SetNode:
        forms_ctx = ctx.forms()
        items = self.visit(forms_ctx) if forms_ctx else []
        return SetNode(location=self._loc(ctx), items=items if isinstance(items, list) else [])

    def visitTag(self, ctx: ClojureParser.TagContext) -> TaggedNode:
        loc = self._loc(ctx)
        tag_node = self.visit(ctx.form(0)) if ctx.form(0) else LiteralNode(location=loc, raw="")
        target_node = self.visit(ctx.form(1)) if ctx.form(1) else LiteralNode(location=loc, raw="")
        return TaggedNode(
            location=loc,
            tag=tag_node if isinstance(tag_node, ASTNode) else LiteralNode(location=loc, raw=""),
            target=target_node if isinstance(target_node, ASTNode) else LiteralNode(location=loc, raw=""),
        )

    def visitReader_macro(self, ctx: ClojureParser.Reader_macroContext) -> ASTNode:
        loc = self._loc(ctx)
        if ctx.tag():
            return self.visitTag(ctx.tag())
        if ctx.lambda_():
            inner_forms = [self.visit(f) for f in ctx.lambda_().form()]
            return ReaderMacroNode(
                location=loc,
                macro_type="#",
                inner=ListNode(location=loc, items=[f for f in inner_forms if isinstance(f, ASTNode)]),
            )
        if ctx.deref():
            inner = self.visit(ctx.deref().form())
            return ReaderMacroNode(location=loc, macro_type="@", inner=inner if isinstance(inner, ASTNode) else None)
        if ctx.quote():
            inner = self.visit(ctx.quote().form())
            return ReaderMacroNode(location=loc, macro_type="'", inner=inner if isinstance(inner, ASTNode) else None)
        if ctx.set_():
            return self.visit(ctx.set_())

        return LiteralNode(location=loc, raw=ctx.getText())

    def visitLiteral(self, ctx: ClojureParser.LiteralContext) -> ASTNode:
        loc = self._loc(ctx)
        if ctx.symbol():
            return SymbolNode(location=loc, name=ctx.symbol().getText())
        if ctx.keyword():
            return KeywordNode(location=loc, name=ctx.keyword().getText().lstrip(":"))
        if ctx.string_():
            raw = ctx.string_().getText()
            if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
                raw = raw[1:-1]
            return StringNode(location=loc, value=raw)
        if ctx.number():
            return NumberNode(location=loc, value=ctx.number().getText())
        if ctx.nil_():
            return LiteralNode(location=loc, raw="nil")
        if ctx.BOOLEAN():
            return LiteralNode(location=loc, raw=ctx.BOOLEAN().getText())

        return LiteralNode(location=loc, raw=ctx.getText())

    def visitSymbol(self, ctx: ClojureParser.SymbolContext) -> SymbolNode:
        return SymbolNode(location=self._loc(ctx), name=ctx.getText())

    def visitKeyword(self, ctx: ClojureParser.KeywordContext) -> KeywordNode:
        return KeywordNode(location=self._loc(ctx), name=ctx.getText().lstrip(":"))

    def visitString_(self, ctx: ClojureParser.String_Context) -> StringNode:
        raw = ctx.getText()
        if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
            raw = raw[1:-1]
        return StringNode(location=self._loc(ctx), value=raw)

    def visitNumber(self, ctx: ClojureParser.NumberContext) -> NumberNode:
        return NumberNode(location=self._loc(ctx), value=ctx.getText())

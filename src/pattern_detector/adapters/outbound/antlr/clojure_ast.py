"""Intermediate S-Expression AST representation for Clojure parse trees."""

from __future__ import annotations

from dataclasses import dataclass, field

from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class ASTNode:
    """Base node for S-expression AST."""

    location: SourceLocation

    def to_text(self) -> str:
        raise NotImplementedError


@dataclass
class SymbolNode(ASTNode):
    name: str = ""

    def to_text(self) -> str:
        return self.name


@dataclass
class KeywordNode(ASTNode):
    name: str = ""

    def to_text(self) -> str:
        return f":{self.name}" if not self.name.startswith(":") else self.name


@dataclass
class StringNode(ASTNode):
    value: str = ""

    def to_text(self) -> str:
        return f'"{self.value}"'


@dataclass
class NumberNode(ASTNode):
    value: str = ""

    def to_text(self) -> str:
        return self.value


@dataclass
class LiteralNode(ASTNode):
    raw: str = ""

    def to_text(self) -> str:
        return self.raw


@dataclass
class ListNode(ASTNode):
    items: list[ASTNode] = field(default_factory=list)

    @property
    def head_symbol(self) -> str | None:
        if not self.items:
            return None
        first = self.items[0]
        if isinstance(first, SymbolNode):
            return first.name
        if isinstance(first, KeywordNode):
            return first.name
        if isinstance(first, TaggedNode) and isinstance(first.target, SymbolNode):
            return first.target.name
        return None

    def to_text(self) -> str:
        inner = " ".join(item.to_text() for item in self.items)
        return f"({inner})"


@dataclass
class VectorNode(ASTNode):
    items: list[ASTNode] = field(default_factory=list)

    def to_text(self) -> str:
        inner = " ".join(item.to_text() for item in self.items)
        return f"[{inner}]"


@dataclass
class MapNode(ASTNode):
    pairs: list[tuple[ASTNode, ASTNode]] = field(default_factory=list)

    def to_text(self) -> str:
        entries = " ".join(f"{k.to_text()} {v.to_text()}" for k, v in self.pairs)
        return f"{{{entries}}}"


@dataclass
class SetNode(ASTNode):
    items: list[ASTNode] = field(default_factory=list)

    def to_text(self) -> str:
        inner = " ".join(item.to_text() for item in self.items)
        return f"#{{{inner}}}"


@dataclass
class TaggedNode(ASTNode):
    """Represents metadata attached via ^meta form (e.g. ^:dynamic *var*)."""

    tag: ASTNode
    target: ASTNode

    @property
    def symbol_name(self) -> str | None:
        if isinstance(self.target, SymbolNode):
            return self.target.name
        if isinstance(self.target, TaggedNode):
            return self.target.symbol_name
        return None

    def to_text(self) -> str:
        return f"^{self.tag.to_text()}{self.target.to_text()}"


@dataclass
class ReaderMacroNode(ASTNode):
    macro_type: str = ""
    inner: ASTNode | None = None

    def to_text(self) -> str:
        inner_text = self.inner.to_text() if self.inner else ""
        return f"{self.macro_type}{inner_text}"

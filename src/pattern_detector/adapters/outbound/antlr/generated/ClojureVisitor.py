# Generated from grammars/Clojure.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ClojureParser import ClojureParser
else:
    from ClojureParser import ClojureParser

# This class defines a complete generic visitor for a parse tree produced by ClojureParser.

class ClojureVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ClojureParser#file_.
    def visitFile_(self, ctx:ClojureParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#form.
    def visitForm(self, ctx:ClojureParser.FormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#forms.
    def visitForms(self, ctx:ClojureParser.FormsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#list_.
    def visitList_(self, ctx:ClojureParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#vector.
    def visitVector(self, ctx:ClojureParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#map_.
    def visitMap_(self, ctx:ClojureParser.Map_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#set_.
    def visitSet_(self, ctx:ClojureParser.Set_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#reader_macro.
    def visitReader_macro(self, ctx:ClojureParser.Reader_macroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#quote.
    def visitQuote(self, ctx:ClojureParser.QuoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#backtick.
    def visitBacktick(self, ctx:ClojureParser.BacktickContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#unquote.
    def visitUnquote(self, ctx:ClojureParser.UnquoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#unquote_splicing.
    def visitUnquote_splicing(self, ctx:ClojureParser.Unquote_splicingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#tag.
    def visitTag(self, ctx:ClojureParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#deref.
    def visitDeref(self, ctx:ClojureParser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#gensym.
    def visitGensym(self, ctx:ClojureParser.GensymContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#lambda_.
    def visitLambda_(self, ctx:ClojureParser.Lambda_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#meta_data.
    def visitMeta_data(self, ctx:ClojureParser.Meta_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#var_quote.
    def visitVar_quote(self, ctx:ClojureParser.Var_quoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#host_expr.
    def visitHost_expr(self, ctx:ClojureParser.Host_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#discard.
    def visitDiscard(self, ctx:ClojureParser.DiscardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#dispatch.
    def visitDispatch(self, ctx:ClojureParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#regex.
    def visitRegex(self, ctx:ClojureParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#literal.
    def visitLiteral(self, ctx:ClojureParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#string_.
    def visitString_(self, ctx:ClojureParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#hex_.
    def visitHex_(self, ctx:ClojureParser.Hex_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#bin_.
    def visitBin_(self, ctx:ClojureParser.Bin_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#bign.
    def visitBign(self, ctx:ClojureParser.BignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#number.
    def visitNumber(self, ctx:ClojureParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#character.
    def visitCharacter(self, ctx:ClojureParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#named_char.
    def visitNamed_char(self, ctx:ClojureParser.Named_charContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#any_char.
    def visitAny_char(self, ctx:ClojureParser.Any_charContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#u_hex_quad.
    def visitU_hex_quad(self, ctx:ClojureParser.U_hex_quadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#nil_.
    def visitNil_(self, ctx:ClojureParser.Nil_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#keyword.
    def visitKeyword(self, ctx:ClojureParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#simple_keyword.
    def visitSimple_keyword(self, ctx:ClojureParser.Simple_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#macro_keyword.
    def visitMacro_keyword(self, ctx:ClojureParser.Macro_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#symbol.
    def visitSymbol(self, ctx:ClojureParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#simple_sym.
    def visitSimple_sym(self, ctx:ClojureParser.Simple_symContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#ns_symbol.
    def visitNs_symbol(self, ctx:ClojureParser.Ns_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClojureParser#param_name.
    def visitParam_name(self, ctx:ClojureParser.Param_nameContext):
        return self.visitChildren(ctx)



del ClojureParser
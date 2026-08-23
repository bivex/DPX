# Generated from grammars/Clojure.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ClojureParser import ClojureParser
else:
    from ClojureParser import ClojureParser

# This class defines a complete listener for a parse tree produced by ClojureParser.
class ClojureListener(ParseTreeListener):

    # Enter a parse tree produced by ClojureParser#file_.
    def enterFile_(self, ctx:ClojureParser.File_Context):
        pass

    # Exit a parse tree produced by ClojureParser#file_.
    def exitFile_(self, ctx:ClojureParser.File_Context):
        pass


    # Enter a parse tree produced by ClojureParser#form.
    def enterForm(self, ctx:ClojureParser.FormContext):
        pass

    # Exit a parse tree produced by ClojureParser#form.
    def exitForm(self, ctx:ClojureParser.FormContext):
        pass


    # Enter a parse tree produced by ClojureParser#forms.
    def enterForms(self, ctx:ClojureParser.FormsContext):
        pass

    # Exit a parse tree produced by ClojureParser#forms.
    def exitForms(self, ctx:ClojureParser.FormsContext):
        pass


    # Enter a parse tree produced by ClojureParser#list_.
    def enterList_(self, ctx:ClojureParser.List_Context):
        pass

    # Exit a parse tree produced by ClojureParser#list_.
    def exitList_(self, ctx:ClojureParser.List_Context):
        pass


    # Enter a parse tree produced by ClojureParser#vector.
    def enterVector(self, ctx:ClojureParser.VectorContext):
        pass

    # Exit a parse tree produced by ClojureParser#vector.
    def exitVector(self, ctx:ClojureParser.VectorContext):
        pass


    # Enter a parse tree produced by ClojureParser#map_.
    def enterMap_(self, ctx:ClojureParser.Map_Context):
        pass

    # Exit a parse tree produced by ClojureParser#map_.
    def exitMap_(self, ctx:ClojureParser.Map_Context):
        pass


    # Enter a parse tree produced by ClojureParser#set_.
    def enterSet_(self, ctx:ClojureParser.Set_Context):
        pass

    # Exit a parse tree produced by ClojureParser#set_.
    def exitSet_(self, ctx:ClojureParser.Set_Context):
        pass


    # Enter a parse tree produced by ClojureParser#reader_macro.
    def enterReader_macro(self, ctx:ClojureParser.Reader_macroContext):
        pass

    # Exit a parse tree produced by ClojureParser#reader_macro.
    def exitReader_macro(self, ctx:ClojureParser.Reader_macroContext):
        pass


    # Enter a parse tree produced by ClojureParser#quote.
    def enterQuote(self, ctx:ClojureParser.QuoteContext):
        pass

    # Exit a parse tree produced by ClojureParser#quote.
    def exitQuote(self, ctx:ClojureParser.QuoteContext):
        pass


    # Enter a parse tree produced by ClojureParser#backtick.
    def enterBacktick(self, ctx:ClojureParser.BacktickContext):
        pass

    # Exit a parse tree produced by ClojureParser#backtick.
    def exitBacktick(self, ctx:ClojureParser.BacktickContext):
        pass


    # Enter a parse tree produced by ClojureParser#unquote.
    def enterUnquote(self, ctx:ClojureParser.UnquoteContext):
        pass

    # Exit a parse tree produced by ClojureParser#unquote.
    def exitUnquote(self, ctx:ClojureParser.UnquoteContext):
        pass


    # Enter a parse tree produced by ClojureParser#unquote_splicing.
    def enterUnquote_splicing(self, ctx:ClojureParser.Unquote_splicingContext):
        pass

    # Exit a parse tree produced by ClojureParser#unquote_splicing.
    def exitUnquote_splicing(self, ctx:ClojureParser.Unquote_splicingContext):
        pass


    # Enter a parse tree produced by ClojureParser#tag.
    def enterTag(self, ctx:ClojureParser.TagContext):
        pass

    # Exit a parse tree produced by ClojureParser#tag.
    def exitTag(self, ctx:ClojureParser.TagContext):
        pass


    # Enter a parse tree produced by ClojureParser#deref.
    def enterDeref(self, ctx:ClojureParser.DerefContext):
        pass

    # Exit a parse tree produced by ClojureParser#deref.
    def exitDeref(self, ctx:ClojureParser.DerefContext):
        pass


    # Enter a parse tree produced by ClojureParser#gensym.
    def enterGensym(self, ctx:ClojureParser.GensymContext):
        pass

    # Exit a parse tree produced by ClojureParser#gensym.
    def exitGensym(self, ctx:ClojureParser.GensymContext):
        pass


    # Enter a parse tree produced by ClojureParser#lambda_.
    def enterLambda_(self, ctx:ClojureParser.Lambda_Context):
        pass

    # Exit a parse tree produced by ClojureParser#lambda_.
    def exitLambda_(self, ctx:ClojureParser.Lambda_Context):
        pass


    # Enter a parse tree produced by ClojureParser#meta_data.
    def enterMeta_data(self, ctx:ClojureParser.Meta_dataContext):
        pass

    # Exit a parse tree produced by ClojureParser#meta_data.
    def exitMeta_data(self, ctx:ClojureParser.Meta_dataContext):
        pass


    # Enter a parse tree produced by ClojureParser#var_quote.
    def enterVar_quote(self, ctx:ClojureParser.Var_quoteContext):
        pass

    # Exit a parse tree produced by ClojureParser#var_quote.
    def exitVar_quote(self, ctx:ClojureParser.Var_quoteContext):
        pass


    # Enter a parse tree produced by ClojureParser#host_expr.
    def enterHost_expr(self, ctx:ClojureParser.Host_exprContext):
        pass

    # Exit a parse tree produced by ClojureParser#host_expr.
    def exitHost_expr(self, ctx:ClojureParser.Host_exprContext):
        pass


    # Enter a parse tree produced by ClojureParser#discard.
    def enterDiscard(self, ctx:ClojureParser.DiscardContext):
        pass

    # Exit a parse tree produced by ClojureParser#discard.
    def exitDiscard(self, ctx:ClojureParser.DiscardContext):
        pass


    # Enter a parse tree produced by ClojureParser#dispatch.
    def enterDispatch(self, ctx:ClojureParser.DispatchContext):
        pass

    # Exit a parse tree produced by ClojureParser#dispatch.
    def exitDispatch(self, ctx:ClojureParser.DispatchContext):
        pass


    # Enter a parse tree produced by ClojureParser#regex.
    def enterRegex(self, ctx:ClojureParser.RegexContext):
        pass

    # Exit a parse tree produced by ClojureParser#regex.
    def exitRegex(self, ctx:ClojureParser.RegexContext):
        pass


    # Enter a parse tree produced by ClojureParser#literal.
    def enterLiteral(self, ctx:ClojureParser.LiteralContext):
        pass

    # Exit a parse tree produced by ClojureParser#literal.
    def exitLiteral(self, ctx:ClojureParser.LiteralContext):
        pass


    # Enter a parse tree produced by ClojureParser#string_.
    def enterString_(self, ctx:ClojureParser.String_Context):
        pass

    # Exit a parse tree produced by ClojureParser#string_.
    def exitString_(self, ctx:ClojureParser.String_Context):
        pass


    # Enter a parse tree produced by ClojureParser#hex_.
    def enterHex_(self, ctx:ClojureParser.Hex_Context):
        pass

    # Exit a parse tree produced by ClojureParser#hex_.
    def exitHex_(self, ctx:ClojureParser.Hex_Context):
        pass


    # Enter a parse tree produced by ClojureParser#bin_.
    def enterBin_(self, ctx:ClojureParser.Bin_Context):
        pass

    # Exit a parse tree produced by ClojureParser#bin_.
    def exitBin_(self, ctx:ClojureParser.Bin_Context):
        pass


    # Enter a parse tree produced by ClojureParser#bign.
    def enterBign(self, ctx:ClojureParser.BignContext):
        pass

    # Exit a parse tree produced by ClojureParser#bign.
    def exitBign(self, ctx:ClojureParser.BignContext):
        pass


    # Enter a parse tree produced by ClojureParser#number.
    def enterNumber(self, ctx:ClojureParser.NumberContext):
        pass

    # Exit a parse tree produced by ClojureParser#number.
    def exitNumber(self, ctx:ClojureParser.NumberContext):
        pass


    # Enter a parse tree produced by ClojureParser#character.
    def enterCharacter(self, ctx:ClojureParser.CharacterContext):
        pass

    # Exit a parse tree produced by ClojureParser#character.
    def exitCharacter(self, ctx:ClojureParser.CharacterContext):
        pass


    # Enter a parse tree produced by ClojureParser#named_char.
    def enterNamed_char(self, ctx:ClojureParser.Named_charContext):
        pass

    # Exit a parse tree produced by ClojureParser#named_char.
    def exitNamed_char(self, ctx:ClojureParser.Named_charContext):
        pass


    # Enter a parse tree produced by ClojureParser#any_char.
    def enterAny_char(self, ctx:ClojureParser.Any_charContext):
        pass

    # Exit a parse tree produced by ClojureParser#any_char.
    def exitAny_char(self, ctx:ClojureParser.Any_charContext):
        pass


    # Enter a parse tree produced by ClojureParser#u_hex_quad.
    def enterU_hex_quad(self, ctx:ClojureParser.U_hex_quadContext):
        pass

    # Exit a parse tree produced by ClojureParser#u_hex_quad.
    def exitU_hex_quad(self, ctx:ClojureParser.U_hex_quadContext):
        pass


    # Enter a parse tree produced by ClojureParser#nil_.
    def enterNil_(self, ctx:ClojureParser.Nil_Context):
        pass

    # Exit a parse tree produced by ClojureParser#nil_.
    def exitNil_(self, ctx:ClojureParser.Nil_Context):
        pass


    # Enter a parse tree produced by ClojureParser#keyword.
    def enterKeyword(self, ctx:ClojureParser.KeywordContext):
        pass

    # Exit a parse tree produced by ClojureParser#keyword.
    def exitKeyword(self, ctx:ClojureParser.KeywordContext):
        pass


    # Enter a parse tree produced by ClojureParser#simple_keyword.
    def enterSimple_keyword(self, ctx:ClojureParser.Simple_keywordContext):
        pass

    # Exit a parse tree produced by ClojureParser#simple_keyword.
    def exitSimple_keyword(self, ctx:ClojureParser.Simple_keywordContext):
        pass


    # Enter a parse tree produced by ClojureParser#macro_keyword.
    def enterMacro_keyword(self, ctx:ClojureParser.Macro_keywordContext):
        pass

    # Exit a parse tree produced by ClojureParser#macro_keyword.
    def exitMacro_keyword(self, ctx:ClojureParser.Macro_keywordContext):
        pass


    # Enter a parse tree produced by ClojureParser#symbol.
    def enterSymbol(self, ctx:ClojureParser.SymbolContext):
        pass

    # Exit a parse tree produced by ClojureParser#symbol.
    def exitSymbol(self, ctx:ClojureParser.SymbolContext):
        pass


    # Enter a parse tree produced by ClojureParser#simple_sym.
    def enterSimple_sym(self, ctx:ClojureParser.Simple_symContext):
        pass

    # Exit a parse tree produced by ClojureParser#simple_sym.
    def exitSimple_sym(self, ctx:ClojureParser.Simple_symContext):
        pass


    # Enter a parse tree produced by ClojureParser#ns_symbol.
    def enterNs_symbol(self, ctx:ClojureParser.Ns_symbolContext):
        pass

    # Exit a parse tree produced by ClojureParser#ns_symbol.
    def exitNs_symbol(self, ctx:ClojureParser.Ns_symbolContext):
        pass


    # Enter a parse tree produced by ClojureParser#param_name.
    def enterParam_name(self, ctx:ClojureParser.Param_nameContext):
        pass

    # Exit a parse tree produced by ClojureParser#param_name.
    def exitParam_name(self, ctx:ClojureParser.Param_nameContext):
        pass



del ClojureParser
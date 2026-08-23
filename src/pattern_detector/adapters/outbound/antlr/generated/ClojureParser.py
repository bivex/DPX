# Generated from grammars/Clojure.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,256,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        94,8,1,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,5,5,114,8,5,10,5,12,5,117,9,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,140,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,
        1,15,5,15,166,8,15,10,15,12,15,169,9,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,3,16,178,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,3,22,205,8,22,1,23,1,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,220,8,27,1,28,1,28,1,28,
        3,28,225,8,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,
        3,33,237,8,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,3,36,
        248,8,36,1,37,1,37,1,38,1,38,1,39,1,39,1,39,0,0,40,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,0,0,253,0,83,1,0,0,0,2,93,1,
        0,0,0,4,98,1,0,0,0,6,101,1,0,0,0,8,105,1,0,0,0,10,109,1,0,0,0,12,
        120,1,0,0,0,14,139,1,0,0,0,16,141,1,0,0,0,18,144,1,0,0,0,20,147,
        1,0,0,0,22,150,1,0,0,0,24,153,1,0,0,0,26,157,1,0,0,0,28,160,1,0,
        0,0,30,163,1,0,0,0,32,172,1,0,0,0,34,179,1,0,0,0,36,182,1,0,0,0,
        38,186,1,0,0,0,40,189,1,0,0,0,42,193,1,0,0,0,44,204,1,0,0,0,46,206,
        1,0,0,0,48,208,1,0,0,0,50,210,1,0,0,0,52,212,1,0,0,0,54,219,1,0,
        0,0,56,224,1,0,0,0,58,226,1,0,0,0,60,228,1,0,0,0,62,230,1,0,0,0,
        64,232,1,0,0,0,66,236,1,0,0,0,68,238,1,0,0,0,70,241,1,0,0,0,72,247,
        1,0,0,0,74,249,1,0,0,0,76,251,1,0,0,0,78,253,1,0,0,0,80,82,3,2,1,
        0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,
        1,0,0,0,85,83,1,0,0,0,86,87,5,0,0,1,87,1,1,0,0,0,88,94,3,44,22,0,
        89,94,3,6,3,0,90,94,3,8,4,0,91,94,3,10,5,0,92,94,3,14,7,0,93,88,
        1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,
        94,3,1,0,0,0,95,97,3,2,1,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,
        0,0,0,98,99,1,0,0,0,99,5,1,0,0,0,100,98,1,0,0,0,101,102,5,1,0,0,
        102,103,3,4,2,0,103,104,5,2,0,0,104,7,1,0,0,0,105,106,5,3,0,0,106,
        107,3,4,2,0,107,108,5,4,0,0,108,9,1,0,0,0,109,115,5,5,0,0,110,111,
        3,2,1,0,111,112,3,2,1,0,112,114,1,0,0,0,113,110,1,0,0,0,114,117,
        1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,
        1,0,0,0,118,119,5,6,0,0,119,11,1,0,0,0,120,121,5,7,0,0,121,122,3,
        4,2,0,122,123,5,6,0,0,123,13,1,0,0,0,124,140,3,30,15,0,125,140,3,
        32,16,0,126,140,3,42,21,0,127,140,3,34,17,0,128,140,3,36,18,0,129,
        140,3,12,6,0,130,140,3,24,12,0,131,140,3,38,19,0,132,140,3,40,20,
        0,133,140,3,26,13,0,134,140,3,16,8,0,135,140,3,18,9,0,136,140,3,
        20,10,0,137,140,3,22,11,0,138,140,3,28,14,0,139,124,1,0,0,0,139,
        125,1,0,0,0,139,126,1,0,0,0,139,127,1,0,0,0,139,128,1,0,0,0,139,
        129,1,0,0,0,139,130,1,0,0,0,139,131,1,0,0,0,139,132,1,0,0,0,139,
        133,1,0,0,0,139,134,1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,
        137,1,0,0,0,139,138,1,0,0,0,140,15,1,0,0,0,141,142,5,8,0,0,142,143,
        3,2,1,0,143,17,1,0,0,0,144,145,5,9,0,0,145,146,3,2,1,0,146,19,1,
        0,0,0,147,148,5,10,0,0,148,149,3,2,1,0,149,21,1,0,0,0,150,151,5,
        11,0,0,151,152,3,2,1,0,152,23,1,0,0,0,153,154,5,12,0,0,154,155,3,
        2,1,0,155,156,3,2,1,0,156,25,1,0,0,0,157,158,5,13,0,0,158,159,3,
        2,1,0,159,27,1,0,0,0,160,161,5,32,0,0,161,162,5,14,0,0,162,29,1,
        0,0,0,163,167,5,15,0,0,164,166,3,2,1,0,165,164,1,0,0,0,166,169,1,
        0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,
        0,0,0,170,171,5,2,0,0,171,31,1,0,0,0,172,177,5,16,0,0,173,174,3,
        10,5,0,174,175,3,2,1,0,175,178,1,0,0,0,176,178,3,2,1,0,177,173,1,
        0,0,0,177,176,1,0,0,0,178,33,1,0,0,0,179,180,5,17,0,0,180,181,3,
        72,36,0,181,35,1,0,0,0,182,183,5,18,0,0,183,184,3,2,1,0,184,185,
        3,2,1,0,185,37,1,0,0,0,186,187,5,19,0,0,187,188,3,2,1,0,188,39,1,
        0,0,0,189,190,5,14,0,0,190,191,3,72,36,0,191,192,3,2,1,0,192,41,
        1,0,0,0,193,194,5,14,0,0,194,195,3,46,23,0,195,43,1,0,0,0,196,205,
        3,46,23,0,197,205,3,54,27,0,198,205,3,56,28,0,199,205,3,64,32,0,
        200,205,5,31,0,0,201,205,3,66,33,0,202,205,3,72,36,0,203,205,3,78,
        39,0,204,196,1,0,0,0,204,197,1,0,0,0,204,198,1,0,0,0,204,199,1,0,
        0,0,204,200,1,0,0,0,204,201,1,0,0,0,204,202,1,0,0,0,204,203,1,0,
        0,0,205,45,1,0,0,0,206,207,5,21,0,0,207,47,1,0,0,0,208,209,5,23,
        0,0,209,49,1,0,0,0,210,211,5,24,0,0,211,51,1,0,0,0,212,213,5,26,
        0,0,213,53,1,0,0,0,214,220,5,22,0,0,215,220,3,48,24,0,216,220,3,
        50,25,0,217,220,3,52,26,0,218,220,5,25,0,0,219,214,1,0,0,0,219,215,
        1,0,0,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,55,1,
        0,0,0,221,225,3,58,29,0,222,225,3,62,31,0,223,225,3,60,30,0,224,
        221,1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,57,1,0,0,0,226,227,
        5,28,0,0,227,59,1,0,0,0,228,229,5,29,0,0,229,61,1,0,0,0,230,231,
        5,27,0,0,231,63,1,0,0,0,232,233,5,30,0,0,233,65,1,0,0,0,234,237,
        3,70,35,0,235,237,3,68,34,0,236,234,1,0,0,0,236,235,1,0,0,0,237,
        67,1,0,0,0,238,239,5,20,0,0,239,240,3,72,36,0,240,69,1,0,0,0,241,
        242,5,20,0,0,242,243,5,20,0,0,243,244,3,72,36,0,244,71,1,0,0,0,245,
        248,3,76,38,0,246,248,3,74,37,0,247,245,1,0,0,0,247,246,1,0,0,0,
        248,73,1,0,0,0,249,250,5,32,0,0,250,75,1,0,0,0,251,252,5,33,0,0,
        252,77,1,0,0,0,253,254,5,34,0,0,254,79,1,0,0,0,12,83,93,98,115,139,
        167,177,204,219,224,236,247
    ]

class ClojureParser ( Parser ):

    grammarFileName = "Clojure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'#{'", "'''", "'`'", "'~'", "'~@'", "'^'", "'@'", 
                     "'#'", "'#('", "'#^'", "'#''", "'#+'", "'#_'", "':'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "FLOAT", "HEX", "BIN", "LONG", 
                      "BIGN", "CHAR_U", "CHAR_NAMED", "CHAR_ANY", "NIL", 
                      "BOOLEAN", "SYMBOL", "NS_SYMBOL", "PARAM_NAME", "TRASH" ]

    RULE_file_ = 0
    RULE_form = 1
    RULE_forms = 2
    RULE_list_ = 3
    RULE_vector = 4
    RULE_map_ = 5
    RULE_set_ = 6
    RULE_reader_macro = 7
    RULE_quote = 8
    RULE_backtick = 9
    RULE_unquote = 10
    RULE_unquote_splicing = 11
    RULE_tag = 12
    RULE_deref = 13
    RULE_gensym = 14
    RULE_lambda_ = 15
    RULE_meta_data = 16
    RULE_var_quote = 17
    RULE_host_expr = 18
    RULE_discard = 19
    RULE_dispatch = 20
    RULE_regex = 21
    RULE_literal = 22
    RULE_string_ = 23
    RULE_hex_ = 24
    RULE_bin_ = 25
    RULE_bign = 26
    RULE_number = 27
    RULE_character = 28
    RULE_named_char = 29
    RULE_any_char = 30
    RULE_u_hex_quad = 31
    RULE_nil_ = 32
    RULE_keyword = 33
    RULE_simple_keyword = 34
    RULE_macro_keyword = 35
    RULE_symbol = 36
    RULE_simple_sym = 37
    RULE_ns_symbol = 38
    RULE_param_name = 39

    ruleNames =  [ "file_", "form", "forms", "list_", "vector", "map_", 
                   "set_", "reader_macro", "quote", "backtick", "unquote", 
                   "unquote_splicing", "tag", "deref", "gensym", "lambda_", 
                   "meta_data", "var_quote", "host_expr", "discard", "dispatch", 
                   "regex", "literal", "string_", "hex_", "bin_", "bign", 
                   "number", "character", "named_char", "any_char", "u_hex_quad", 
                   "nil_", "keyword", "simple_keyword", "macro_keyword", 
                   "symbol", "simple_sym", "ns_symbol", "param_name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    STRING=21
    FLOAT=22
    HEX=23
    BIN=24
    LONG=25
    BIGN=26
    CHAR_U=27
    CHAR_NAMED=28
    CHAR_ANY=29
    NIL=30
    BOOLEAN=31
    SYMBOL=32
    NS_SYMBOL=33
    PARAM_NAME=34
    TRASH=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ClojureParser.EOF, 0)

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_" ):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = ClojureParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359738282) != 0):
                self.state = 80
                self.form()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(ClojureParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ClojureParser.LiteralContext,0)


        def list_(self):
            return self.getTypedRuleContext(ClojureParser.List_Context,0)


        def vector(self):
            return self.getTypedRuleContext(ClojureParser.VectorContext,0)


        def map_(self):
            return self.getTypedRuleContext(ClojureParser.Map_Context,0)


        def reader_macro(self):
            return self.getTypedRuleContext(ClojureParser.Reader_macroContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_form

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm" ):
                listener.enterForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm" ):
                listener.exitForm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForm" ):
                return visitor.visitForm(self)
            else:
                return visitor.visitChildren(self)




    def form(self):

        localctx = ClojureParser.FormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_form)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.vector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.map_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.reader_macro()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_forms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForms" ):
                listener.enterForms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForms" ):
                listener.exitForms(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForms" ):
                return visitor.visitForms(self)
            else:
                return visitor.visitChildren(self)




    def forms(self):

        localctx = ClojureParser.FormsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359738282) != 0):
                self.state = 95
                self.form()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forms(self):
            return self.getTypedRuleContext(ClojureParser.FormsContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_list_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_" ):
                listener.enterList_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_" ):
                listener.exitList_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_" ):
                return visitor.visitList_(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = ClojureParser.List_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ClojureParser.T__0)
            self.state = 102
            self.forms()
            self.state = 103
            self.match(ClojureParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forms(self):
            return self.getTypedRuleContext(ClojureParser.FormsContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = ClojureParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ClojureParser.T__2)
            self.state = 106
            self.forms()
            self.state = 107
            self.match(ClojureParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_map_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_" ):
                listener.enterMap_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_" ):
                listener.exitMap_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_" ):
                return visitor.visitMap_(self)
            else:
                return visitor.visitChildren(self)




    def map_(self):

        localctx = ClojureParser.Map_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_map_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ClojureParser.T__4)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359738282) != 0):
                self.state = 110
                self.form()
                self.state = 111
                self.form()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(ClojureParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forms(self):
            return self.getTypedRuleContext(ClojureParser.FormsContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_set_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_" ):
                listener.enterSet_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_" ):
                listener.exitSet_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_" ):
                return visitor.visitSet_(self)
            else:
                return visitor.visitChildren(self)




    def set_(self):

        localctx = ClojureParser.Set_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_set_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ClojureParser.T__6)
            self.state = 121
            self.forms()
            self.state = 122
            self.match(ClojureParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reader_macroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambda_(self):
            return self.getTypedRuleContext(ClojureParser.Lambda_Context,0)


        def meta_data(self):
            return self.getTypedRuleContext(ClojureParser.Meta_dataContext,0)


        def regex(self):
            return self.getTypedRuleContext(ClojureParser.RegexContext,0)


        def var_quote(self):
            return self.getTypedRuleContext(ClojureParser.Var_quoteContext,0)


        def host_expr(self):
            return self.getTypedRuleContext(ClojureParser.Host_exprContext,0)


        def set_(self):
            return self.getTypedRuleContext(ClojureParser.Set_Context,0)


        def tag(self):
            return self.getTypedRuleContext(ClojureParser.TagContext,0)


        def discard(self):
            return self.getTypedRuleContext(ClojureParser.DiscardContext,0)


        def dispatch(self):
            return self.getTypedRuleContext(ClojureParser.DispatchContext,0)


        def deref(self):
            return self.getTypedRuleContext(ClojureParser.DerefContext,0)


        def quote(self):
            return self.getTypedRuleContext(ClojureParser.QuoteContext,0)


        def backtick(self):
            return self.getTypedRuleContext(ClojureParser.BacktickContext,0)


        def unquote(self):
            return self.getTypedRuleContext(ClojureParser.UnquoteContext,0)


        def unquote_splicing(self):
            return self.getTypedRuleContext(ClojureParser.Unquote_splicingContext,0)


        def gensym(self):
            return self.getTypedRuleContext(ClojureParser.GensymContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_reader_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReader_macro" ):
                listener.enterReader_macro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReader_macro" ):
                listener.exitReader_macro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReader_macro" ):
                return visitor.visitReader_macro(self)
            else:
                return visitor.visitChildren(self)




    def reader_macro(self):

        localctx = ClojureParser.Reader_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_reader_macro)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.lambda_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.meta_data()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.regex()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.var_quote()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.host_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.set_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.tag()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.discard()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.dispatch()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.deref()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.quote()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.backtick()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 136
                self.unquote()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 137
                self.unquote_splicing()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 138
                self.gensym()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuote" ):
                listener.enterQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuote" ):
                listener.exitQuote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuote" ):
                return visitor.visitQuote(self)
            else:
                return visitor.visitChildren(self)




    def quote(self):

        localctx = ClojureParser.QuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ClojureParser.T__7)
            self.state = 142
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BacktickContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_backtick

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBacktick" ):
                listener.enterBacktick(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBacktick" ):
                listener.exitBacktick(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBacktick" ):
                return visitor.visitBacktick(self)
            else:
                return visitor.visitChildren(self)




    def backtick(self):

        localctx = ClojureParser.BacktickContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_backtick)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ClojureParser.T__8)
            self.state = 145
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_unquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnquote" ):
                listener.enterUnquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnquote" ):
                listener.exitUnquote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquote" ):
                return visitor.visitUnquote(self)
            else:
                return visitor.visitChildren(self)




    def unquote(self):

        localctx = ClojureParser.UnquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ClojureParser.T__9)
            self.state = 148
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unquote_splicingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_unquote_splicing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnquote_splicing" ):
                listener.enterUnquote_splicing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnquote_splicing" ):
                listener.exitUnquote_splicing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquote_splicing" ):
                return visitor.visitUnquote_splicing(self)
            else:
                return visitor.visitChildren(self)




    def unquote_splicing(self):

        localctx = ClojureParser.Unquote_splicingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unquote_splicing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ClojureParser.T__10)
            self.state = 151
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag" ):
                return visitor.visitTag(self)
            else:
                return visitor.visitChildren(self)




    def tag(self):

        localctx = ClojureParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ClojureParser.T__11)
            self.state = 154
            self.form()
            self.state = 155
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DerefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_deref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeref" ):
                listener.enterDeref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeref" ):
                listener.exitDeref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeref" ):
                return visitor.visitDeref(self)
            else:
                return visitor.visitChildren(self)




    def deref(self):

        localctx = ClojureParser.DerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_deref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ClojureParser.T__12)
            self.state = 158
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GensymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(ClojureParser.SYMBOL, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_gensym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGensym" ):
                listener.enterGensym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGensym" ):
                listener.exitGensym(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGensym" ):
                return visitor.visitGensym(self)
            else:
                return visitor.visitChildren(self)




    def gensym(self):

        localctx = ClojureParser.GensymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_gensym)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ClojureParser.SYMBOL)
            self.state = 161
            self.match(ClojureParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lambda_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_lambda_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda_" ):
                listener.enterLambda_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda_" ):
                listener.exitLambda_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda_" ):
                return visitor.visitLambda_(self)
            else:
                return visitor.visitChildren(self)




    def lambda_(self):

        localctx = ClojureParser.Lambda_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lambda_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ClojureParser.T__14)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359738282) != 0):
                self.state = 164
                self.form()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(ClojureParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def map_(self):
            return self.getTypedRuleContext(ClojureParser.Map_Context,0)


        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_meta_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeta_data" ):
                listener.enterMeta_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeta_data" ):
                listener.exitMeta_data(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_data" ):
                return visitor.visitMeta_data(self)
            else:
                return visitor.visitChildren(self)




    def meta_data(self):

        localctx = ClojureParser.Meta_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_meta_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ClojureParser.T__15)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 173
                self.map_()
                self.state = 174
                self.form()
                pass

            elif la_ == 2:
                self.state = 176
                self.form()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_quoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(ClojureParser.SymbolContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_var_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_quote" ):
                listener.enterVar_quote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_quote" ):
                listener.exitVar_quote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_quote" ):
                return visitor.visitVar_quote(self)
            else:
                return visitor.visitChildren(self)




    def var_quote(self):

        localctx = ClojureParser.Var_quoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ClojureParser.T__16)
            self.state = 180
            self.symbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Host_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClojureParser.FormContext)
            else:
                return self.getTypedRuleContext(ClojureParser.FormContext,i)


        def getRuleIndex(self):
            return ClojureParser.RULE_host_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHost_expr" ):
                listener.enterHost_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHost_expr" ):
                listener.exitHost_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHost_expr" ):
                return visitor.visitHost_expr(self)
            else:
                return visitor.visitChildren(self)




    def host_expr(self):

        localctx = ClojureParser.Host_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_host_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ClojureParser.T__17)
            self.state = 183
            self.form()
            self.state = 184
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiscardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_discard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiscard" ):
                listener.enterDiscard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiscard" ):
                listener.exitDiscard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiscard" ):
                return visitor.visitDiscard(self)
            else:
                return visitor.visitChildren(self)




    def discard(self):

        localctx = ClojureParser.DiscardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_discard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ClojureParser.T__18)
            self.state = 187
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DispatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(ClojureParser.SymbolContext,0)


        def form(self):
            return self.getTypedRuleContext(ClojureParser.FormContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_dispatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispatch" ):
                listener.enterDispatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispatch" ):
                listener.exitDispatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispatch" ):
                return visitor.visitDispatch(self)
            else:
                return visitor.visitChildren(self)




    def dispatch(self):

        localctx = ClojureParser.DispatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dispatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ClojureParser.T__13)
            self.state = 190
            self.symbol()
            self.state = 191
            self.form()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_(self):
            return self.getTypedRuleContext(ClojureParser.String_Context,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = ClojureParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ClojureParser.T__13)
            self.state = 194
            self.string_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_(self):
            return self.getTypedRuleContext(ClojureParser.String_Context,0)


        def number(self):
            return self.getTypedRuleContext(ClojureParser.NumberContext,0)


        def character(self):
            return self.getTypedRuleContext(ClojureParser.CharacterContext,0)


        def nil_(self):
            return self.getTypedRuleContext(ClojureParser.Nil_Context,0)


        def BOOLEAN(self):
            return self.getToken(ClojureParser.BOOLEAN, 0)

        def keyword(self):
            return self.getTypedRuleContext(ClojureParser.KeywordContext,0)


        def symbol(self):
            return self.getTypedRuleContext(ClojureParser.SymbolContext,0)


        def param_name(self):
            return self.getTypedRuleContext(ClojureParser.Param_nameContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ClojureParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.string_()
                pass
            elif token in [22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.number()
                pass
            elif token in [27, 28, 29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.character()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.nil_()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.match(ClojureParser.BOOLEAN)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.keyword()
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.symbol()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.param_name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ClojureParser.STRING, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_" ):
                return visitor.visitString_(self)
            else:
                return visitor.visitChildren(self)




    def string_(self):

        localctx = ClojureParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_string_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ClojureParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hex_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEX(self):
            return self.getToken(ClojureParser.HEX, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_hex_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex_" ):
                listener.enterHex_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex_" ):
                listener.exitHex_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHex_" ):
                return visitor.visitHex_(self)
            else:
                return visitor.visitChildren(self)




    def hex_(self):

        localctx = ClojureParser.Hex_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_hex_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ClojureParser.HEX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BIN(self):
            return self.getToken(ClojureParser.BIN, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_bin_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_" ):
                listener.enterBin_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_" ):
                listener.exitBin_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_" ):
                return visitor.visitBin_(self)
            else:
                return visitor.visitChildren(self)




    def bin_(self):

        localctx = ClojureParser.Bin_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_bin_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ClojureParser.BIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BIGN(self):
            return self.getToken(ClojureParser.BIGN, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_bign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBign" ):
                listener.enterBign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBign" ):
                listener.exitBign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBign" ):
                return visitor.visitBign(self)
            else:
                return visitor.visitChildren(self)




    def bign(self):

        localctx = ClojureParser.BignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_bign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ClojureParser.BIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ClojureParser.FLOAT, 0)

        def hex_(self):
            return self.getTypedRuleContext(ClojureParser.Hex_Context,0)


        def bin_(self):
            return self.getTypedRuleContext(ClojureParser.Bin_Context,0)


        def bign(self):
            return self.getTypedRuleContext(ClojureParser.BignContext,0)


        def LONG(self):
            return self.getToken(ClojureParser.LONG, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = ClojureParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_number)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ClojureParser.FLOAT)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.hex_()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.bin_()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.bign()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                self.match(ClojureParser.LONG)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def named_char(self):
            return self.getTypedRuleContext(ClojureParser.Named_charContext,0)


        def u_hex_quad(self):
            return self.getTypedRuleContext(ClojureParser.U_hex_quadContext,0)


        def any_char(self):
            return self.getTypedRuleContext(ClojureParser.Any_charContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_character

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter" ):
                listener.enterCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter" ):
                listener.exitCharacter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacter" ):
                return visitor.visitCharacter(self)
            else:
                return visitor.visitChildren(self)




    def character(self):

        localctx = ClojureParser.CharacterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_character)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.named_char()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.u_hex_quad()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.any_char()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_charContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_NAMED(self):
            return self.getToken(ClojureParser.CHAR_NAMED, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_named_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_char" ):
                listener.enterNamed_char(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_char" ):
                listener.exitNamed_char(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_char" ):
                return visitor.visitNamed_char(self)
            else:
                return visitor.visitChildren(self)




    def named_char(self):

        localctx = ClojureParser.Named_charContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_named_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ClojureParser.CHAR_NAMED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_charContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_ANY(self):
            return self.getToken(ClojureParser.CHAR_ANY, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_any_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_char" ):
                listener.enterAny_char(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_char" ):
                listener.exitAny_char(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_char" ):
                return visitor.visitAny_char(self)
            else:
                return visitor.visitChildren(self)




    def any_char(self):

        localctx = ClojureParser.Any_charContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_any_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ClojureParser.CHAR_ANY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class U_hex_quadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_U(self):
            return self.getToken(ClojureParser.CHAR_U, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_u_hex_quad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterU_hex_quad" ):
                listener.enterU_hex_quad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitU_hex_quad" ):
                listener.exitU_hex_quad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitU_hex_quad" ):
                return visitor.visitU_hex_quad(self)
            else:
                return visitor.visitChildren(self)




    def u_hex_quad(self):

        localctx = ClojureParser.U_hex_quadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_u_hex_quad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ClojureParser.CHAR_U)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nil_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(ClojureParser.NIL, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_nil_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil_" ):
                listener.enterNil_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil_" ):
                listener.exitNil_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_" ):
                return visitor.visitNil_(self)
            else:
                return visitor.visitChildren(self)




    def nil_(self):

        localctx = ClojureParser.Nil_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_nil_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(ClojureParser.NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_keyword(self):
            return self.getTypedRuleContext(ClojureParser.Macro_keywordContext,0)


        def simple_keyword(self):
            return self.getTypedRuleContext(ClojureParser.Simple_keywordContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = ClojureParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_keyword)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.macro_keyword()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.simple_keyword()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(ClojureParser.SymbolContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_simple_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_keyword" ):
                listener.enterSimple_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_keyword" ):
                listener.exitSimple_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_keyword" ):
                return visitor.visitSimple_keyword(self)
            else:
                return visitor.visitChildren(self)




    def simple_keyword(self):

        localctx = ClojureParser.Simple_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_simple_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ClojureParser.T__19)
            self.state = 239
            self.symbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(ClojureParser.SymbolContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_macro_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_keyword" ):
                listener.enterMacro_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_keyword" ):
                listener.exitMacro_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_keyword" ):
                return visitor.visitMacro_keyword(self)
            else:
                return visitor.visitChildren(self)




    def macro_keyword(self):

        localctx = ClojureParser.Macro_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_macro_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ClojureParser.T__19)
            self.state = 242
            self.match(ClojureParser.T__19)
            self.state = 243
            self.symbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ns_symbol(self):
            return self.getTypedRuleContext(ClojureParser.Ns_symbolContext,0)


        def simple_sym(self):
            return self.getTypedRuleContext(ClojureParser.Simple_symContext,0)


        def getRuleIndex(self):
            return ClojureParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = ClojureParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_symbol)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.ns_symbol()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.simple_sym()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_symContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(ClojureParser.SYMBOL, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_simple_sym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_sym" ):
                listener.enterSimple_sym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_sym" ):
                listener.exitSimple_sym(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_sym" ):
                return visitor.visitSimple_sym(self)
            else:
                return visitor.visitChildren(self)




    def simple_sym(self):

        localctx = ClojureParser.Simple_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_simple_sym)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ClojureParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ns_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NS_SYMBOL(self):
            return self.getToken(ClojureParser.NS_SYMBOL, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_ns_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNs_symbol" ):
                listener.enterNs_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNs_symbol" ):
                listener.exitNs_symbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNs_symbol" ):
                return visitor.visitNs_symbol(self)
            else:
                return visitor.visitChildren(self)




    def ns_symbol(self):

        localctx = ClojureParser.Ns_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ns_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ClojureParser.NS_SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAM_NAME(self):
            return self.getToken(ClojureParser.PARAM_NAME, 0)

        def getRuleIndex(self):
            return ClojureParser.RULE_param_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_name" ):
                listener.enterParam_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_name" ):
                listener.exitParam_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_name" ):
                return visitor.visitParam_name(self)
            else:
                return visitor.visitChildren(self)




    def param_name(self):

        localctx = ClojureParser.Param_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_param_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ClojureParser.PARAM_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






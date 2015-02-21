import logging
import sys

import ply.yacc as yacc

from ast import ArgumentList, Attribute, Decorator, Name
from lexer import tokens


#def p_error(p):
    #print "Syntax error"


def p_single_input(p):
    """single_input : NEWLINE
                    | simple_stmt
                    | compound_stmt NEWLINE"""
    print "single_input", p[:]


#def p_file_input(p):
    #"""file_input : file_input_inner ENDMARKER"""
    #print "file_input", p[:]


#def p_file_input_inner(p):
    #"""file_input_inner : empty
                        #| file_input_inner NEWLINE
                        #| file_input_inner stmt"""
    #print "file_input_inner", p


def p_decorator(p):
    """decorator : AT dotted_name LPAREN arglist RPAREN NEWLINE
                 | AT dotted_name NEWLINE"""
    if len(p) == 7:
        p[0] = Decorator(p[2], p[4])
    else:
        p[0] = Decorator(p[2])
    print "decorator", p[:]


def p_decorators(p):
    """decorators : decorator
                  | decorators decorator"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
    print "decorators", p[:]


def p_decorated(p):
    """decorated : decorators classdef
                 | decorators funcdef"""
    print "decorated", p[:]


def p_funcdef(p):
    """funcdef : DEF NAME parameters COLON suite"""
    print "funcdef", p[:]


def p_parameters(p):
    """parameters : LPAREN RPAREN
                  | LPAREN varargslist RPAREN"""
    print "parameters", p[:]


def p_varargslist(p):
    """varargslist : varargslist_inner1 STAR NAME
                   | varargslist_inner1 STAR NAME COMMA DBL_STAR NAME
                   | varargslist_inner1 DBL_STAR NAME
                   | fpdef varargslist_inner2 optional_comma
                   | fpdef EQ test varargslist_inner2 optional_comma"""
    print "varargslist", p[:]


def p_varargslist_inner1(p):
    """varargslist_inner1 : empty
                          | fpdef COMMA varargslist_inner1
                          | fpdef EQ test COMMA varargslist_inner1"""
    print "varargslist_inner1", p[:]


def p_varargslist_inner2(p):
    """varargslist_inner2 : empty
                          | COMMA fpdef varargslist_inner1
                          | COMMA fpdef EQ test varargslist_inner2"""
    print "varargslist_inner2", p[:]


def p_fpdef(p):
    """fpdef : NAME
             | LPAREN fplist RPAREN"""
    print "fpdef", p[:]


def p_fplist(p):
    """fplist : fpdef fplist_inner optional_comma"""
    print "fplist", p[:]


def p_fplist_inner(p):
    """fplist_inner : empty
                    | fplist_inner COMMA fpdef"""
    print "fplist_inner", p[:]


################
## Statements ##
################


def p_stmt(p):
    """stmt : simple_stmt
            | compound_stmt"""
    print "stmt", p[:]


def p_simple_stmt(p):
    """simple_stmt : simple_stmt_inner NEWLINE
                   | simple_stmt_inner SEMICOLON NEWLINE"""
    print "simple_stmt", p[:]


def p_simple_stmt_inner(p):
    """simple_stmt_inner : small_stmt
                         | small_stmt SEMICOLON simple_stmt_inner"""
    print "simple_stmt_inner", p[:]


def p_small_stmt(p):
    """small_stmt : expr_stmt
                  | print_stmt
                  | del_stmt
                  | pass_stmt
                  | flow_stmt
                  | import_stmt
                  | global_stmt
                  | exec_stmt
                  | assert_stmt"""
    print "small_stmt", p[:]


def p_expr_stmt(p):
    """expr_stmt : testlist
                 | testlist augassign yield_expr
                 | testlist augassign testlist
                 | testlist expr_stmt_inner"""
    print "expr_stmt", p[:]


def p_expr_stmt_inner(p):
    """expr_stmt_inner : empty
                       | EQ yield_expr expr_stmt_inner
                       | EQ testlist expr_stmt_inner"""
    print "expr_stmt_inner", p[:]


def p_augassign(p):
    """augassign : PLUS_EQ
                 | MINUS_EQ
                 | STAR_EQ
                 | SLASH_EQ
                 | MOD_EQ
                 | AMPERSAND_EQ
                 | PIPE_EQ
                 | CARET_EQ
                 | DBL_LANG_EQ
                 | DBL_RANG_EQ
                 | DBL_STAR_EQ
                 | DBL_SLASH_EQ"""
    print "augassign", p[:]


def p_print_stmt(p):
    """print_stmt : PRINT
                  | PRINT test_multiple optional_comma
                  | DBL_RANG test
                  | DBL_RANG test COMMA test test_multiple optional_comma"""
    print "print_stmt", p[:]


def p_del_stmt(p):
    """del_stmt : DEL exprlist"""
    print "del_stmt", p[:]


def p_pass_stmt(p):
    """pass_stmt : PASS"""
    print "pass_stmt", p[:]


def p_flow_stmt(p):
    """flow_stmt : break_stmt
                 | continue_stmt
                 | return_stmt
                 | raise_stmt
                 | yield_stmt"""
    print "flow_stmt", p[:]


def p_break_stmt(p):
    """break_stmt : BREAK"""
    print "break_stmt", p[:]


def p_continue_stmt(p):
    """continue_stmt : CONTINUE"""
    print "continue_stmt", p[:]


def p_return_stmt(p):
    """return_stmt : RETURN
                   | RETURN testlist"""
    print "return_stmt", p[:]


def p_yield_stmt(p):
    """yield_stmt : yield_expr"""
    print "yield_stmt", p[:]


def p_raise_stmt(p):
    """raise_stmt : RAISE
                  | RAISE test
                  | RAISE test COMMA test
                  | RAISE test COMMA test COMMA test"""
    print "raise_stmt", p[:]


def p_import_stmt(p):
    """import_stmt : import_name
                   | import_from"""
    print "import_stmt", p[:]


def p_import_name(p):
    """import_name : IMPORT dotted_as_names"""
    print "import_name", p[:]


def p_import_from(p):
    """import_from : FROM dot_multiple dotted_name IMPORT STAR
                   | FROM dot_multiple dotted_name IMPORT LPAREN import_as_names RPAREN
                   | FROM dot_multiple dotted_name IMPORT import_as_names
                   | FROM DOT dot_multiple IMPORT STAR
                   | FROM DOT dot_multiple IMPORT LPAREN import_as_names RPAREN
                   | FROM DOT dot_multiple IMPORT import_as_names"""
    print "import_name", p[:]


# '.'*
def p_dot_multiple(p):
    """dot_multiple : empty
                    | DOT dot_multiple"""
    print "dot_multiple", p[:]


def p_import_as_name(p):
    """import_as_name : NAME
                      | NAME AS NAME"""
    print "import_as_name", p[:]


def p_dotted_as_name(p):
    """dotted_as_name : dotted_name
                      | dotted_name AS NAME"""
    print "dotted_as_name", p[:]


def p_import_as_names(p):
    """import_as_names : import_as_names_inner optional_comma"""
    print "import_as_names", p[:]


# import_as_name (',' import_as_name)*
def p_import_as_names_inner(p):
    """import_as_names_inner : import_as_name
                             | import_as_name COMMA import_as_names_inner"""
    print "import_as_names_inner", p[:]


def p_dotted_as_names(p):
    """dotted_as_names : dotted_as_name
                       | dotted_as_name COMMA dotted_as_names"""
    print "dotted_as_names", p[:]


def p_dotted_name(p):
    """dotted_name : NAME
                   | dotted_name DOT NAME"""
    if len(p) == 2:
        p[0] = Name(p[1])
    else:
        p[0] = Attribute(p[3], p[1])
    print "dotted_name", p[:]


def p_global_stmt(p):
    """global_stmt : GLOBAL name_multiple"""
    print "global_stmt", p[:]


# NAME (',' NAME)*
def p_name_multiple(p):
    """name_multiple : NAME
                     | NAME COMMA name_multiple"""
    print "name_multiple", p[:]


def p_exec_stmt(p):
    """exec_stmt : EXEC expr
                 | EXEC expr IN test
                 | EXEC expr IN test COMMA test"""
    print "exec_stmt", p[:]


def p_assert_stmt(p):
    """assert_stmt : ASSERT test
                   | ASSERT test COMMA test"""
    print "assert_stmt", p[:]


def p_compound_stmt(p):
    """compound_stmt : if_stmt
                     | while_stmt
                     | for_stmt
                     | try_stmt
                     | with_stmt
                     | funcdef
                     | classdef
                     | decorated"""
    print "compound_stmt", p[:]


def p_if_stmt(p):
    """if_stmt : IF test COLON suite elif_multiple
               | IF test COLON suite elif_multiple ELSE COLON suite"""
    print "if_stmt", p[:]


# ('elif' test ':' suite)*
def p_elif_multiple(p):
    """elif_multiple : empty
                     | ELIF test COLON suite elif_multiple"""
    print "elif_multiple", p[:]


def p_while_stmt(p):
    """while_stmt : WHILE test COLON suite
                 | WHILE test COLON suite ELSE COLON suite"""
    print "while_stmt", p[:]


def p_for_stmt(p):
    """for_stmt : FOR exprlist IN testlist COLON suite
                | FOR exprlist IN testlist COLON suite ELSE COLON suite"""
    print "for_stmt", p[:]


def p_try_stmt(p):
    """try_stmt : TRY COLON suite try_inner
                | TRY COLON suite try_inner ELSE COLON suite
                | TRY COLON suite try_inner FINALLY COLON suite
                | TRY COLON suite try_inner ELSE COLON suite FINALLY COLON suite
                | TRY COLON suite FINALLY COLON suite
                """
    print "try_stmt", p[:]


# (except_clause ':' suite)+
def p_try_inner(p):
    """try_inner : except_clause COLON suite
                 | except_clause COLON suite try_inner"""
    print "try_inner", p[:]


def p_with_stmt(p):
    """with_stmt : WITH with_items COLON suite"""
    print "with_stmt", p[:]


# with_item (',' with_item)*
def p_with_items(p):
    """with_items : with_item
                  | with_item COMMA with_items"""
    print "with_items", p[:]


def p_with_item(p):
    """with_item : test
                 | test AS expr"""
    print "with_item", p[:]


def p_except_clause(p):
    """except_clause : EXCEPT
                     | EXCEPT test
                     | EXCEPT test AS test
                     | EXCEPT test COMMA test"""
    print "except_caluse", p[:]


# TODO: fix
def p_suite(p):
    """suite : simple_stmt
             | stmt suite"""
    print "suite", p[:]


#######################
## End of Statements ##
#######################


def p_testlist_safe(p):
    """testlist_safe : testlist_safe_inner optional_comma"""
    print "testlist_safe", p[:]


def p_testlist_safe_inner(p):
    """testlist_safe_inner : old_test
                           | old_test COMMA testlist_safe_inner"""
    print "testlist_safe_inner", p[:]


def p_old_test(p):
    """old_test : or_test
                | old_lambdef"""
    print "old_test", p[:]


def p_old_lambdef(p):
    """old_lambdef : LAMBDA COLON old_test
                   | LAMBDA varargslist COLON old_test"""
    print "old_lambdef", p[:]


def p_test(p):
    """test : or_test
            | or_test IF or_test ELSE test
            | lambdef"""
    print "test", p[:]


# test (',' test)*
def p_test_multiple(p):
    """test_multiple : test
                     | test_multiple COMMA test"""
    print "test_multiple", p[:]


def p_or_test(p):
    """or_test : and_test
               | and_test OR or_test"""
    print "or_test", p[:]


def p_and_test(p):
    """and_test : not_test
                | not_test AND and_test"""
    print "and_test", p[:]


def p_not_test(p):
    """not_test : NOT not_test
               | comparison"""
    print "not_test", p[:]


def p_comparison(p):
    """comparison : expr
                  | expr comp_op expr"""
    print "comparison", p[:]


def p_comp_op(p):
    """comp_op : LANG
               | RANG
               | DEQ
               | GEQ
               | LEQ
               | NEQ
               | NEQ2
               | IN
               | NOT IN
               | IS
               | IS NOT"""
    print "comparison", p[:]


def p_expr(p):
    """expr : xor_expr
            | xor_expr PIPE xor_expr"""
    print "expr", p[:]


def p_xor_expr(p):
    """xor_expr : and_expr
                | and_expr CARET xor_expr"""
    print "xor_expr", p[:]


def p_and_expr(p):
    """and_expr : shift_expr
                | shift_expr AMPERSAND and_expr"""
    print "and_expr", p[:]


def p_shift_expr(p):
    """shift_expr : arith_expr
                  | arith_expr DBL_LANG arith_expr
                  | arith_expr DBL_RANG arith_expr"""
    print "shift_expr", p[:]


def p_arith_expr(p):
    """arith_expr : term
                  | term PLUS term
                  | term MINUS term"""
    print "arith_expr", p[:]


def p_term(p):
    """term : factor
            | factor STAR factor
            | factor SLASH factor
            | factor MOD factor
            | factor DBL_SLASH factor"""
    print "term", p[:]


def p_factor(p):
    """factor : PLUS factor
              | MINUS factor
              | TILDE factor
              | power"""
    print "factor", p[:]


# TODO: fix this definition
def p_power(p):
    """power : atom
             | atom DBL_STAR factor"""
    print "power", p[:]


def p_atom(p):
    """atom : LPAREN RPAREN
            | LPAREN yield_expr RPAREN
            | LPAREN testlist_comp RPAREN
            | LSQ RSQ
            | LSQ listmaker RSQ
            | LCURL RCURL
            | LCURL dictorsetmaker RCURL
            | BACKTICK testlist1 BACKTICK
            | NAME
            | number
            | string"""
    print "atom", p[:]
    p[0] = p[1]


def p_listmaker(p):
    """listmaker : test_multiple optional_comma
                 | test list_for"""
    print "listmaker", p[:]


def p_testlist_comp(p):
    """testlist_comp : test_multiple optional_comma
                     | test comp_for"""
    print "testlist_comp", p[:]


def p_lambdef(p):
    """lambdef : LAMBDA COLON test
               | LAMBDA varargslist COLON test"""
    print "lambdef", p[:]


def p_trailer(p):
    """trailer : LPAREN arglist RPAREN
               | LSQ subscriptlist RSQ
               | DOT NAME"""
    print "trailer", p[:]


def p_subscriptlist(p):
    """subscriptlist : subscriptlist_inner optional_comma"""
    print "subscriptlist", p[:]


def p_subscriptlist_inner(p):
    """subscriptlist_inner : subscript
                           | subscript COMMA subscriptlist_inner"""
    print "subscriptlist_inner", p[:]


def p_subscript(p):
    """subscript : DOT DOT DOT
                 | test
                 | COLON
                 | COLON sliceop
                 | COLON test
                 | COLON test sliceop
                 | test COLON
                 | test COLON sliceop
                 | test COLON test
                 | test COLON test sliceop"""
    print "subscript", p[:]


def p_sliceop(p):
    """sliceop : COLON
               | COLON test"""
    print "sliceop", p[:]


def p_exprlist(p):
    """exprlist : exprlist_inner optional_comma"""
    print "exprlist", p[:]


def p_exprlist_inner(p):
    """exprlist_inner : expr
                      | expr COMMA exprlist_inner"""
    print "exprlist_inner", p[:]


def p_testlist(p):
    """testlist : exprlist_inner optional_comma"""
    print "testlist", p[:]


def p_testlist_inner(p):
    """testlist_inner : test
                      | test COMMA testlist_inner"""
    print "testlist_inner", p[:]


def p_dictorsetmaker(p):
    """dictorsetmaker : test COLON test
                      | test COLON test comp_for
                      | test COLON test dictorsetmaker_inner optional_comma
                      | test
                      | test comp_for
                      | test_multiple optional_comma"""


def p_dictorsetmaker_inner(p):
    """dictorsetmaker_inner : empty
                            | dictorsetmaker_inner COMMA test COLON test"""
    print "dictorsetmaker_inner", p[:]


def p_classdef(p):
    """classdef : CLASS NAME COLON suite
                | CLASS NAME LPAREN RPAREN COLON suite
                | CLASS NAME LPAREN testlist RPAREN COLON suite"""
    print "classdef", p[:]


def p_arglist(p):
    """arglist : arglist_inner argument optional_comma
               | arglist_inner STAR test arglist_inner
               | arglist_inner STAR test arglist_inner COMMA DBL_STAR test
               | arglist_inner DBL_STAR test"""
    print "arglist", p[:]


def p_arglist_inner(p):
    """arglist_inner : empty
                     | argument COMMA arglist_inner"""
    print "arglist_inner", p[:]


def p_argument(p):
    """argument : test
                | test comp_for
                | test EQ test"""
    print "argument", p[:]


def p_list_iter(p):
    """list_iter : list_for
                 | list_if"""
    print 'list_iter', p[:]


def p_list_for(p):
    """list_for : FOR exprlist IN testlist_safe
                | FOR exprlist IN testlist_safe list_iter"""
    print "list_for", p[:]


def p_list_if(p):
    """list_if : IF old_test
               | IF old_test list_iter"""
    print "list_if", p[:]


def p_comp_iter(p):
    """comp_iter : comp_for
                 | comp_if"""
    print 'comp_iter', p[:]


def p_comp_for(p):
    """comp_for : FOR exprlist IN or_test
                | FOR exprlist IN or_test comp_iter"""
    print "comp_for", p[:]


def p_comp_if(p):
    """comp_if : IF old_test
               | IF old_test comp_iter"""
    print "comp_if", p[:]


def p_testlist1(p):
    """testlist1 : test
                 | testlist1 COMMA test"""
    print "testlist1", p[:]


def p_encoding_decl(p):
    """encoding_decl : NAME"""
    print "encoding_decl", p[:]


def p_yield_expr(p):
    """yield_expr : YIELD
                  | YIELD testlist"""
    print "yield_expr", p[:]


def p_optional_comma(p):
    """optional_comma : COMMA
                      | empty"""
    print "optional comma", p[:]


# STRING+
def p_string(p):
    """string : STRINGLITERAL
              | STRINGLITERAL string"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]
    print "string", p[:]


def p_number(p):
    """number : FLOATNUMBER
              | BININTEGER
              | HEXINTEGER
              | OCTINTEGER
              | DECIMALINTEGER"""
    print "number", p[:]
    p[0] = p[1]


def p_empty(p):
    """empty :"""
    pass

parser = yacc.yacc()


if __name__ == '__main__':
    logging.basicConfig(filename='parser.log', level=logging.INFO)
    log = logging.getLogger()
    parser.parse(sys.stdin.read(), debug=log)

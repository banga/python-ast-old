import sys

import ply.yacc as yacc

from ast import ArgumentList, Attribute, Decorator, Name
from lexer import tokens


"""
decorator: AT dotted_name [ LPAREN [arglist] RPAREN ] NEWLINE
decorators: decorator+
decorated: decorators (classdef | funcdef)
"""


#def p_error(p):
    #print "Syntax error"


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


"""
(fpdef ['=' test] ',')* ('*' NAME [',' '**' NAME] | '**' NAME)
| fpdef ['=' test] (',' fpdef ['=' test])* [',']
"""
def p_varargslist(p):
    """varargslist : varargslist_inner1 STAR NAME
                   | varargslist_inner1 STAR NAME COMMA DBLSTAR NAME
                   | varargslist_inner1 DBLSTAR NAME
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


def p_dotted_name(p):
    """dotted_name : NAME
                   | dotted_name DOT NAME"""
    if len(p) == 2:
        p[0] = Name(p[1])
    else:
        p[0] = Attribute(p[3], p[1])


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


# TODO: fix this definition
def p_test(p):
    """test : or_test NEWLINE
            | or_test IF or_test ELSE test"""
    print "test", p[:]


# (',' test)*
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
                  | arith_expr LSH arith_expr
                  | arith_expr RSH arith_expr"""
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
            | factor DBLSLASH factor"""
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
             | atom DBLSTAR factor"""
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
               | arglist_inner STAR test arglist_inner COMMA DBLSTAR test
               | arglist_inner DBLSTAR test"""
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
    print parser.parse(sys.stdin.read())

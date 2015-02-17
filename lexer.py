__doc__ = """

Lexer for Python AST.

"""
from ply.lex import TOKEN

reserved = {
    'and': 'AND',
    'as': 'AS',
    'assert': 'ASSERT',
    'break': 'BREAK',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'def': 'DEF',
    'del': 'DEL',
    'elif': 'ELIF',
    'else': 'ELSE',
    'except': 'EXCEPT',
    'exec': 'EXEC',
    'finally': 'FINALLY',
    'for': 'FOR',
    'from': 'FROM',
    'global': 'GLOBAL',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'is': 'IS',
    'lambda': 'LAMBDA',
    'not': 'NOT',
    'or': 'OR',
    'pass': 'PASS',
    'print': 'PRINT',
    'raise': 'RAISE',
    'return': 'RETURN',
    'try': 'TRY',
    'while': 'WHILE',
    'with': 'WITH',
    'yield': 'YIELD',
}


tokens = [
    'NAME',
    'STRINGLITERAL',
    'FLOATNUMBER',
    'BININTEGER',
    'HEXINTEGER',
    'OCTINTEGER',
    'DECIMALINTEGER',
    'NEWLINE',
    'AT',
    'DOT',
    'LPAREN',
    'RPAREN',
    'LSQ',
    'RSQ',
    'LCURL',
    'RCURL',
    'LANG',
    'RANG',
    'DEQ',
    'GEQ',
    'LEQ',
    'NEQ',
    'NEQ2',
    'COMMA',
    'SEMICOLON',
    'PIPE',
    'CARET',
    'AMPERSAND',
    'LSH',
    'RSH',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'DBLSTAR',
    'DBLSLASH',
    'MOD',
    'TILDE',
    'COLON',
    'BACKTICK',
    'EQ',
] + reserved.values()


# Ignored characters
t_ignore = " \t"

t_AT = r'@'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQ = r'\['
t_RSQ = r'\]'
t_LCURL = r'{'
t_RCURL = r'}'
t_LANG = r'<'
t_RANG = r'>'
t_DEQ = r'=='
t_GEQ = r'>='
t_LEQ = r'<='
t_NEQ = r'!='
t_NEQ2 = r'<>'
t_COMMA = r','
t_SEMICOLON = r';'
t_PIPE = r'\|'
t_CARET = r'\^'
t_AMPERSAND = r'&'
t_LSH = r'<<'
t_RSH = r'>>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_DBLSTAR = r'\*\*'
t_DBLSLASH = r'//'
t_MOD = r'%'
t_TILDE = r'~'
t_COLON = r':'
t_BACKTICK = r'`'
t_EQ = r'='


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#######################################
## Integer and long integer literals ##
#######################################

digit = r'[0-9]'
hexdigit = r'[0-9a-fA-F]'
bindigit = r'[0-1]'
octdigit = r'[0-7]'
nonzerodigit = r'[1-9]'
longoptional = r'[lL]?'

octinteger = (r'0[oO]' + octdigit + r'+' + longoptional + r'|' +
              r'0' + octdigit + r'+' + longoptional)
hexinteger = r'0[xX]' + hexdigit + r'+' + longoptional
bininteger = r'0[bB]' + bindigit + r'+' + longoptional
decimalinteger = (nonzerodigit + digit + r'*' + longoptional + r'|' +
                  r'0' + longoptional)


#############################
## Floating point literals ##
#############################

exponent = r'[eE][+-]?' + digit + r'+'
fraction = r'\.' + digit + r'+'
intpart = digit + r'+'
pointfloat = (r'(' + r'(' + intpart + r')?' + fraction + r')' + r'|' +
              r'(' + intpart + r'\.)')
exponentfloat = r'((' + intpart + r'|' + pointfloat + ')' + exponent + r')'
floatnumber = exponentfloat + '|' + pointfloat


#####################
## String literals ##
#####################
longstring = (r'(' +
              r'"""([^\\]|(\\[\x00-\x7f]))*"""' +
              r'|' +
              r"'''([^\\]|(\\[\x00-\x7f]))*'''" +
              r')')
shortstring = (r'(' +
               r'"([^\\\n\"]|(\\[\x00-\x7f]))*"' +
               r'|' +
               r"'([^\\\n\']|(\\[\x00-\x7f]))*'" +
               r')')
stringprefix = r'([rR]|([uUbB][rR]?))'
stringliteral = (r'(' + stringprefix + ')?' +
                 r'(' + longstring + '|' + shortstring + ')')


@TOKEN(stringliteral)
def t_STRINGLITERAL(t):
    return t


####################################
## Identifiers and reserved words ##
####################################


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


# NOTE: These functions are defined to force an order in which
# we apply the greediest rules first

@TOKEN(floatnumber)
def t_FLOATNUMBER(t):
    return t


@TOKEN(bininteger)
def t_BININTEGER(t):
    return t


@TOKEN(hexinteger)
def t_HEXINTEGER(t):
    return t


@TOKEN(octinteger)
def t_OCTINTEGER(t):
    return t


@TOKEN(decimalinteger)
def t_DECIMALINTEGER(t):
    return t


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


# Build the lexer
import ply.lex as lex
lex.lex()


def tokenize(text):
    lex.input(text)
    while True:
        token = lex.token()
        if not token:
            break
        yield token


if __name__ == '__main__':
    def print_all(text):
        lex.input(text)
        while 1:
            tok = lex.token()
            if not tok:
                break
            print tok

    while 1:
        try:
            text = raw_input('text > ')
        except EOFError:
            break
        print_all(text)

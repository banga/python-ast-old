__doc__ = """

Lexer for Python AST.

"""
from ply.lex import TOKEN

tokens = (
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAR',
    'RPAR',
    'LBRACE',
    'RBRACE',
    'LSQB',
    'RSQB',
    'FLOATNUMBER',
    'BININTEGER',
    'HEXINTEGER',
    'OCTINTEGER',
    'DECIMALINTEGER',
)

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQB = r'\['
t_RSQB = r'\]'

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

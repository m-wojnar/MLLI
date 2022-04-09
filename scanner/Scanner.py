# Maksymilian Wojnar

import ply.lex as lex

t_ignore_COMMENT = r'\#.*'
t_ignore = '  \t'

literals = "+-*/=<>,;:'()[]{}"

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

tokens = [
             'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
             'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
             'LE', 'GE', 'NE', 'EQ',
             'FLOATNUM', 'INTNUM', 'STRING', 'ID'
         ] + list(reserved.values())

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_EQ = r'=='


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_FLOATNUM(t):
    r'(((\d*\.\d+)|(\d+\.))([eE][-+]?\d+)?)|(\d+[eE][-+]?\d+)'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'".*?"'
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}', line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

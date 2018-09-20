from enum import Enum
from ply import *


reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'return': 'RETURN',
    'void': 'VOID',
    'while': 'WHILE'
    }

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LTHAN',
    'LOEQU',
    'MTHAN',
    'MOEQU',
    'EQUALS',
    'DIFF',
    'ASSIGN',
    'SEMICOLON',
    'COMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'COMMENTS',
    'COMMENTE',
    'ID',
    'NUM',
    'LETTER',
    'DIGT',
    'ENDFILE'
    ]+list(reserved.values())

literals = [ '+','-','*','/' ]

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LTHAN     = r'<'
t_LOEQU     = r'<=' #revisar
t_MTHAN     = r'>'
t_MOEQU     = r'>=' #revisar
t_EQUALS    = r'==' #revisar
t_DIFF      = r'!=' #revisar
t_ASSIGN    = r'='
t_SEMICOLON = r';'
t_COMA      = r'\,'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LKEY      = r'\{'
t_RKEY      = r'\}'
eof         = '$'
t_ENDFILE = r'\$'

t_ignore = ' \t'


class TokenType(Enum):
    ENDFILE = eof


def t_NUM(t):
    r'\d+'
    try:
        t.value = int(t.value)
        return t
    except ValueError:
        print("Integer value too large %d", t.value)


#  Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("\nError: ")
    print(f"Linea {t.lexer.lineno}: String Unknown \"{t.value[0]}\" ")
    arr = t.lexer.lexdata.split('\n')
    linea = arr[t.lexer.lineno-1].strip()
    print(linea)
    print(" "*linea.find(t.value[0])+"^")
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_COMMENT(t):
    r'(/\*(.|\n+)*?\*/)'
    pass


lexer = lex.lex()

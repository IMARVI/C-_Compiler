from globalTypes import *
from lexer import *

f = open('./sample2.c-', 'r')

programa = f.read() + '$'

globales(programa, 0, len(programa))

token, tokenString = getToken()

while (token != TokenType.ENDFILE):
    token, tokenString = getToken()

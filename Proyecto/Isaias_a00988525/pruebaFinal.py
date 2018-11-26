from globalTypes import *
from parser import *
from semantica import *
from cgen import *

f = open('./sample2.c-', 'r')
programa = f.read()     # lee
progLong = len(programa)   # longitud original del programa
programa = programa + '$'   # agregar un caracter $ que represente EOF
posicion = 0       # posición del caracter actual del string
globales(programa, posicion, progLong)

AST = parse(True)
semantica(AST, True)
codeGen(AST, 'file.s')

from globalTypes import *
from parser import *
from semantica import *

f = open('./sample2.c-', 'r')
programa = f.read()
progLong = len(programa)
programa = programa + '$'
posicion = 0
globales(programa,posicion,progLong)

AST = parse(False)
semantica(AST, True)
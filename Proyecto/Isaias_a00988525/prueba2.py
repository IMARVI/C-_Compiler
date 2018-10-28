from globalTypes import *
from parser import *

f = open('./sample.c-', 'r')
programa = f.read()
progLong = len(programa)
programa = programa+ "$"
posicion = 0
globales(programa, posicion, progLong)

AST = parse(True)


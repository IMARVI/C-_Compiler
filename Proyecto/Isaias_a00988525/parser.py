from lexer import *
from makeParser import *

programaCargado = False
programa = ""


def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long


def cargarPrograma():
    global programaCargado
    programaCargado = True


def impresion(nodo,i):

    if isinstance(nodo,tuple):
        for n in range(len(nodo)):
            if isinstance(nodo[n], tuple) or isinstance(nodo[n], str):

                if len(nodo) > 1:
                    if n < 1:
                        if len(nodo) == 2 and isinstance(nodo[1], str):
                            print('| ' * i, nodo[0])
                        else:
                            print('| '*i, nodo[0])

                    elif isinstance(nodo[n], str):
                        print('| '*i, nodo[n])
                impresion(nodo[n], i+1)



def parse(imprime):
    t = parser.parse(programa)
    if imprime:
        impresion(t,0)

        return t

    else: 
        return t
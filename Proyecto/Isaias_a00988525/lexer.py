from globalTypes import lexer, TokenType

programaCargado = False


def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long


def cargarPrograma():
    global programaCargado
    lexer.input(programa)
    programaCargado = True


def getToken(imprime = True):

    if not programaCargado:
        cargarPrograma()

    t = lexer.token()

    if t.value is not TokenType.ENDFILE.value and imprime:
        print(f"({t.type} , \"{t.value}\")")
        return t.type, t.value
    else:
        print(f"({t.type} , \"{t.value}\")")
    return TokenType.ENDFILE,TokenType.ENDFILE.value
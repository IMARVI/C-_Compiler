import ply.yacc as yacc
from globalTypes import tokens

variables = {}
funciones = {}
params = {}

start = 'program'

# Asignamos presedencia, indicando que plus y minus tienen el mimso valor y se toma de izq
# TImes y Divide tienen mayor valor tomandolos de la izq
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
# Definimos nuestras reglas gramaticales como metodos

def p_program(p): #----------listo
    'program    : declaration_list'

    p[0] = ('programa',p[1])

def p_declaration_list(p): #----------listo
    '''     declaration_list    : declaration_list declaration
                                | declaration                
    '''
    if len(p) == 3:
        p[0] = ('declaration list',p[1],p[2])
    else: p[0] = ('declaration list',p[1])
    

def p_declaration(p): #----------listo
    '''     declaration     : var_declaration
                            | fun_declaration
                            | ENDFILE
    '''
    p[0] = ('declaration',p[1])
    

def p_var_declaration(p): #------------ listo
    '''     var_declaration : type_specifier ID SEMICOLON
                            | type_specifier ID LBRACKET NUM RBRACKET SEMICOLON
    '''
    variables[p[2]] = p[1][1]
    if len(p) == 4:
        p[0] = ('var declaration',p[1],p[2],p[3])
    else: p[0] = ('var declaration',p[1],p[2],p[3],p[4],p[5],p[6])

def p_type_specifier(p):  #------------ listo
    ''' 
            type_specifier  : INT
                            | VOID 
    '''
    p[0] = ('type specifier',p[1])

def p_fun_declaration(p): #------------ listo
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
    funciones[p[2]] = p[1][1]
    p[0] = ('fun declaration',p[1],p[2],p[3],p[4],p[5],p[6])


def p_params(p): #------------ listo
    ''' params      : param_list
                    | VOID
    '''
    p[0] = ('params',p[1])

def p_param_list(p): #------------ listo
    ''' param_list      : param_list COMA param
                        | param
    '''
    if len(p) == 4:
        p[0] = ('param list',p[1],p[2],p[3])
    else: p[0] = ('param list',p[1])

def p_param(p): #------------ listo
    ''' param   : type_specifier ID
                | type_specifier ID LBRACKET RBRACKET
    '''
    params[p[2]] = p[1][1]
    if len(p) == 3:
        p[0] = ('param',p[1],p[2])
    else: 
        p[0] = ('param', p[1],p[2],p[3])

def p_compound_stmt(p): #------------ listo
    'compound_stmt : LKEY local_declarations statement_list RKEY'
    p[0] = ('compound stmt',p[1],p[2],p[3],p[4])

def p_local_declarations(p): #------------ listo
    ''' local_declarations  : local_declarations var_declaration
                            | empty
    '''
    if len(p) == 3:
        p[0] = ("local declarations", p[1],p[2])
    

def p_statement_list(p): #------------ listo
    ''' statement_list  : statement_list statement
                        | empty
    '''
    if len(p) == 3:
        p[0] = ('statement list',p[1],p[2])

def p_statement(p): #------------ listo
    ''' statement   : expression_stmt
                    | compound_stmt
                    | selection_stmt
                    | iteration_stmt
                    | return_stmt
    '''
    p[0] = ('statement',p[1])

def p_expression_stmt(p): #------------ listo
    ''' expression_stmt  : expression SEMICOLON
                        | SEMICOLON
    '''
    if len(p) == 3:
        p[0] = ('expression stmt', p[1],p[2])
    else: p[0] = ('expression stmt',p[1])

def p_selection_stmt(p): #------------ listo
    ''' selection_stmt  : IF LPAREN expression RPAREN statement
                        | IF LPAREN expression RPAREN statement ELSE statement
    '''
    if len(p) == 6:
        p[0] = ('selection stmt',p[1],p[2],p[3],p[4],p[5])
    else: p[0] = ('selection stmt',p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_iteration_stmt(p):
    ' iteration_stmt  : WHILE LPAREN expression RPAREN statement'
    p[0] = ('iteration stmt',p[1],p[2],p[3],p[4],p[5])

def p_return_stmt(p):
    ''' return_stmt     : RETURN SEMICOLON
                        | RETURN expression SEMICOLON
    '''
    if len(p) == 3:
        p[0] = ('return stmtm',p[1],p[2])
    else: p[0] = ('return stmt',p[1],p[2],p[3])

def p_expression(p):
    ''' expression      : var ASSIGN expression
                        | simple_expression
    '''
    if len(p) == 4:
        p[0] = ('expression',p[1],p[2],p[3])
    else: p[0] = ('expression',p[1])

def p_var(p):
    ''' var     : ID
                | ID LBRACKET expression RBRACKET
    '''
    if len(p) == 5:
        p[0] = ('var',p[1],p[2],p[3],p[4])
    else: 
        p[0] = ('var', p[1])

def p_simple_expression(p):
    ''' simple_expression   : additive_expression relop additive_expression
                            | additive_expression
    '''
    if len(p) == 4:
        p[0] = ('simple expression',p[1],p[2],p[3])
    else: p[0] = ('simple expression',p[1])

def p_relop(p):
    ''' relop   : LOEQU
                | LTHAN
                | MTHAN
                | MOEQU
                | EQUALS
                | DIFF
    '''
    p[0] = ('relop',p[1])

def p_additive_expression(p):
    '''     additive_expression     : additive_expression addop term
                                    | term 
    '''
    if len(p) == 4:
        p[0] = ('additive expression',p[1],p[2],p[3])
    else: p[0] = ('additive expression',p[1])

def p_addop(p):
    '''     addop   : PLUS
                    | MINUS
    '''
    p[0] = ('addop',p[1])

def p_term(p):
    ''' term    : term mulop factor
                | factor 
    '''
    if len(p) == 4:
        p[0] = ('term',p[1],p[2],p[3])
    else: p[0] = ('term',p[1])

def p_mulop(p):
    '''     mulop   : TIMES
                    | DIVIDE
    '''
    p[0] = ('mulop',p[1])

def p_factor(p):
    ''' factor  : LPAREN expression RPAREN
                | var
                | call
                | NUM 
    '''
    if len(p) == 4:
        p[0] = ('factor',p[1],p[2],p[3])
    else: p[0] = ('factor',p[1])

def p_call(p):
    ' call    : ID LPAREN args RPAREN '
    p[0] = ('call',p[1],p[2],p[3],p[4])

def p_args(p):
    ''' args    : arg_list
                | empty
    '''
    if len(p) == 2:
        p[0] = ('args',p[1])

def p_arg_list(p):
    ''' arg_list    : arg_list COMA expression
                    | expression
    '''
    if len(p) == 4:
        p[0] = ('arg list',p[1],p[2],p[3])
    else: p[0] = ('arg list',p[1])

def p_empty(p):
    'empty :'
    pass



# Si exite un error implementamos boton de panico:
# Es decir que el seguimos sacando token hasta que salga un } o ;
def p_error(p):            
    
    if not p:
        print("End of File!")
        return

    while True:
        # Get the next token
        tok = parser.token()
        #print("next token = ",tok)
        if not tok or tok.type == 'SEMICOLON' or tok.type == 'RKEY': 
            break
    parser.restart()

# Build  parser
parser = yacc.yacc(debug=False)
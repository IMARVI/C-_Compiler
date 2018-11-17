tabla_simbolos = []
actual_scope=0
funval = []
evalNum = 2

def semantica(arbol, imprime = True):
  tabla(arbol)
  global actual_scope
  actual_scope = 0
  semantica_1(arbol,0)
  for x in range(len(tabla_simbolos)):
    print(tabla_simbolos[x])


def semantica_1(arbol,scope):
  if arbol is None or type(arbol) is int: return

  if arbol[0] == 'programa':
      semantica_1(arbol[1],scope)
  elif arbol[0] == 'declaration list':
    for x in range(1,len(arbol)):
      semantica_1(arbol[x],scope)
  elif arbol[0] == 'declaration':
    semantica_1(arbol[1],scope)
  elif arbol[0] == 'fun declaration':  
    global actual_scope
    actual_scope +=1
    semantica_1(arbol[6], actual_scope)
  elif arbol[0] == 'compound stmt':
    for x in range(1,len(arbol)):
      semantica_1(arbol[x],scope)
  elif arbol[0] == 'statement list':
    for x in range(1,len(arbol)):
      semantica_1(arbol[x],scope)
  elif arbol[0] == 'statement':
    semantica_1(arbol[1],scope)
  elif arbol[0] == 'expression stmt':
    semantica_1(arbol[1],scope)
  elif arbol[0] == 'expression':
    # debemos de checar que la variable sea signada a un valor int o arr
    if len(arbol) == 4:
      if arbol[1][1] in tabla_simbolos[scope] and tabla_simbolos[scope][arbol[1][1]] == 'int':
        if checkType(arbol[3],arbol[1][1],scope):
          return True
        else:
          print("Error:")
          print(f"El valor de asignacion {arbol[1][1]}, no corresponde al de la var {tabla_simbolos[scope][arbol[1][1]]}")
          quit()
    else:
      semantica_1(arbol[1],scope)
  elif arbol[0] == 'simple expression':
    if len(arbol) == 2:
      checkFun(arbol[1],scope)      


# --------- Metodo para checar los valores y funciones ---------
def checkFun(xpr,scope):
  global funval, evalNum
  if xpr[0] == 'call':
    if xpr[1] in tabla_simbolos[0]:      
      funval = tabla_simbolos[0][xpr[1]].split(",")
      checkFun(xpr[3],scope)
    else:
      print("Error:")
      print(f"la Funcion no ha sido definida {xpr[1]}")
      quit()
  elif xpr[0] == 'args':
    checkFun(xpr[1],scope)
  elif xpr[0] == 'expression':
    return checkFun(xpr[1],scope)
  elif xpr[0] == 'arg list':
    for x in range(1,len(xpr)):
      checkFun(xpr[x],scope)
  elif xpr[0] == 'simple expression':
    for x in range(1,len(xpr)):
      return checkFun(xpr[x],scope)
  elif xpr[0] == 'additive expression':
    # checamos que los dos valores de al suma sean int
    for x in range(1,len(xpr)):
      return checkFun(xpr[x],scope)
  elif xpr[0] == 'term':
    for x in range(1,len(xpr)):
      return checkFun(xpr[x],scope)
  elif xpr[0] == 'var':
    #  verificamos que la variable exista 
    #  y corresponda con el valor que tiene que tener la funcion
    if xpr[1] in tabla_simbolos[scope]:
      aux = tabla_simbolos[scope][xpr[1]].split(",")
      if aux[0] == funval[evalNum]:
        evalNum = evalNum+2
        return True
      else:
        print("Error:")
        print(f"El valor de asignacion {funval[evalNum]}, no corresponde al de la var {aux[0]}")
        quit()
    elif xpr[1] in tabla_simbolos[0]:
      aux = tabla_simbolos[0][xpr[1]].split(",")
      if aux[0] == funval[evalNum]:
        valNum = evalNum+2
        return True
      else:
        print("Error:")
        print(f"El valor de asignacion {funval[evalNum]}, no corresponde al de la var {aux[0]}")
        quit()
  elif xpr[0] == 'factor':
    if type(xpr[1]) is int:
      if 'int' == funval[evalNum]:
        evalNum = evalNum+2
        return True
    else:
      if len(xpr) == 4:
        return checkFun(xpr[2],scope)
      else:
        return checkFun(xpr[1],scope)

  
def checkType(xpr, var1, scope):
  if xpr[0] == 'expression':
    return checkType(xpr[1],var1,scope)
  elif xpr[0] == 'simple expression':
    for x in range(1,len(xpr)):
      return checkType(xpr[x],var1,scope)
  elif xpr[0] == 'additive expression':
    # checamos que los dos valores de al suma sean int
    for x in range(1,len(xpr)):
      return checkType(xpr[x],var1,scope)
  elif xpr[0] == 'term':
    # checamos que los dos valores sean int
    for x in range(1,len(xpr)):
      return checkType(xpr[x],var1,scope)
  elif xpr[0] == 'factor':
    #  verificamos que var1 y xpr sean int
    if type(xpr[1]) is int:
      if var1 in tabla_simbolos[scope]:
        if tabla_simbolos[scope][var1] == 'int': 
          return True
      elif var1 in tabla_simbolos[0]:
        if tabla_simbolos[0][var1] == 'int': 
          return True
      else:
        print("Error:")
        print(f"variable no exite \"{xpr[1]}\"")
        quit()
    else:
      if len(xpr) == 4:
        return checkType(xpr[2],var1,scope)
      else:
        return checkType(xpr[1],var1,scope)
  elif xpr[0] == 'call':
    if xpr[1] in tabla_simbolos[0]:
      aux = tabla_simbolos[0][xpr[1]].split(",")
      if aux[0] == tabla_simbolos[scope][var1]:
        return True
      else:
        print("Error:")
        print(f" Variables no corresponden \"{aux[0]} y {tabla_simbolos[scope][var1]}\" ")
        quit()
    else:
      print("Error:")
      print(f" Metodo no declarado \"{xpr[1]}\" ")
      quit()
  elif xpr[0] == 'var':
    # -------- Falta revisar cuando sean arreglos
    if xpr[1] in tabla_simbolos[scope]:
      if tabla_simbolos[scope][xpr[1]] == tabla_simbolos[scope][var1]:
        return True
      else:
        #  Imprimimos Error
        return False
    elif xpr[1] in tabla_simbolos[0]:
      if tabla_simbolos[0][xpr[1]] == tabla_simbolos[0][var1]:
        return True
      else:
        #  Imprimimos Error
        return False
    else:
      print("No encontrada")
      return False


# ---- Metodos para crear la Tabla ----
def tabla(arbol, imprime= True):
  tabla_real(arbol,imprime, 0)


def tabla_real(arbol, imprime, scope):
  if arbol is None or type(arbol) is int: return
  if arbol[0] == 'programa':
    tabla_simbolos.append({'scope': scope})
    tabla_real(arbol[1],True,scope)
  elif arbol[0] == 'declaration list':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'declaration':
    tabla_real(arbol[1],True,scope)
  elif arbol[0] == 'var declaration':
    if noExisteVar(arbol[2],scope):
      if len(arbol) == 4:
        tabla_simbolos[scope][arbol[2]] = arbol[1][1] #+ ","+ arbol[3]
      else:
        tabla_simbolos[scope][arbol[2]] =  arbol[1][1] + ","+ arbol[3]+ "," +str(arbol[4])+ "," +arbol[5]
  elif arbol[0] == 'fun declaration':
    global actual_scope
    actual_scope +=1
    tabla_simbolos.append({'scope': actual_scope})
    if noExisteVar(arbol[2],scope):
      if arbol[4][1] == 'void':
        tabla_simbolos[0][arbol[2]]= arbol[1][1]+",fun,void"
      else:
        tabla_simbolos[0][arbol[2]]= arbol[1][1]+",fun"
        parametros(arbol[2],arbol[4], actual_scope)
      tabla_real(arbol[6],True, actual_scope)
  elif arbol[0] == 'compound stmt':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'local declarations':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'statement list':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'statement':
    tabla_real(arbol[1],True,scope)
  elif arbol[0] == 'expression stmt':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'expression':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'var':
    # revisamos si la variable ha sido declarada
    if not varDeclarada(arbol[1],scope):
      quit()
  elif arbol[0] == 'selection stmt':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'iteration stmt':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'return stmtm':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'return stmtm':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'simple expression':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'additive expression':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'term':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'factor':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'call':
    if not varDeclarada(arbol[1],scope):
      quit()
    else:
      for x in range(1,len(arbol)):
        tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'args':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  elif arbol[0] == 'arg list':
    for x in range(1,len(arbol)):
      tabla_real(arbol[x],True,scope)
  
  
#  Metodo para ingresar las variables a la tabla
def noExisteVar(var,scope):
  if var not in tabla_simbolos[scope]:
    return True
  else: return False

#  Metodo para revisar si las variables han sido declaradas
def varDeclarada(var,scope):
  if var not in tabla_simbolos[scope]:
    if var not in tabla_simbolos[0]:
      print("Error:")
      print(f" Variable No declarada \"{var}\" ")
      return False
    else: return True
  else: return True

#  Metodo para meter los parametros de la fun a la tabla
def parametros(nombre_fun, params,scope):
  if params[0] == 'params':
    parametros(nombre_fun,params[1],scope)
  if params[0] == 'param list':
    for x in range(1,len(params)):
      parametros(nombre_fun,params[x],scope)
  elif params[0] == 'param':
    # metemos los parametros al scope correspondiente de la funcion
    tabla_simbolos[scope][params[2]] = params[1][1]

    # metemos el nombre de la fun al scope general
    valor_aux = tabla_simbolos[0][nombre_fun]
    tabla_simbolos[0][nombre_fun] = valor_aux + "," + params[1][1] +","+ params[2]
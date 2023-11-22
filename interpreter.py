import lexer




#TEMPLATE

# ----------------------- SECTION ->
# <- SECTION -----------------------

#/TEMPLATE



# ----------------------- STORAGE & RELATIONSHIPS ->

variables = {}
OPERATIONS_LIST = ["add", "sub", "mul", "div", "set", "del"]
lits = ["num_i", "str"]
#numerals, strings -> LIT

#any sort of identifier -> ID

#specialized OPERATION identifier -> OID


relationships = {
  "prnt":{
    "1":"LIT"
  },
  "defn":{
    "1":"ID"
  },
  "altv":{
    "1":"ID",
    "2":{
      "11":"ID",
      "22":"LIT"
    }
  }
}
# <- STORAGE & RELATIONSHIPS -----------------------

# ----------------------- ERRORS ->
class _error:
  def __init__(self, exception):
    self.exception = exception
  def invoke(self):
    return f"ERROR: {self.exception}"
class non_existent_error(_error):
  def __init__(self, exception):
    super().__init__(exception)
  def invoke(self):
    return f"ERROR: {self.exception} DOES NOT EXIST"

class no_command_error(_error):
  def __init__(self, exception):
    super().__init__(exception)
  def invoke(self):
    return f"ERROR: {self.exception} IS NOT A COMMAND"
# <- ERRORS -----------------------

# ----------------------- THESE ARE HELPERS ->
def v_check(vname):
  try:
    if not variables[vname]:
      return False
    return True
  except:
    return False
    
def v_set(vname, val):
  variables[vname] = val
  
def v_read(vname):
  v_exist = v_check(vname)
  if not v_exist:
    error = non_existent_error(vname)
    print(error.invoke())
    return
  return variables[vname]

def v_type_check(vname):
  a = v_read(vname)
  if a and type(a) == int:
    return "num_i"
  return "str"
  
# <- THESE ARE HELPERS -----------------------

def variableFunctionTest():
  while True:
    x = input()
    if x == "xit":
      return
    elif x == "read":
      y = input("y:")
      print(v_read(y))
    elif x == "set":
      y = input("y:")
      z = input("z:")
      v_set(y, z)
      print("1")
    elif x == "type":
      y = input("y:")
      a = v_read(y)
      if a and type(a) == int:
        print("int")
      else:
        print("str")


# ----------------------- built in funcs ->

def prnt_FUNC(line):
  a = line[0]
  if a.type == "id" and a.value not in OPERATIONS_LIST:
    print(v_read(a.value))
    return
  print(a.value)
    
def defn_FUNC(line):
  a = line[0]
  if (a.type == "id" and a.value not in OPERATIONS_LIST) and not v_check(a.value):
    variables[str(a.value)] = str(a.value)
    return
def altv_FUNC(line):
  a = line[0]
  b = line[1]
  optype = b.value
  if len(line) == 2:
    if optype == "del":
      del variables[a.value]
      return
  c = line[2]
  if a.type == "id" and b.value in OPERATIONS_LIST and c.type in lits:
    if not v_check(a.value):
      #error, no vardef
      return
    oldv = variables[a.value]
    # a is var, b is operator, c is operator coefficient
    #SET DEL ADD SUB MUL DIV 

    if optype == "set":
      variables[a.value] = c.value
      return
    if type(c.value) == type(oldv):
      if optype == "add":
        variables[a.value] = oldv + c.value
      elif optype == "sub":
        variables[a.value] = oldv - c.value
      elif optype == "mul":
        variables[a.value] = oldv * c.value
      elif optype == "div":
        variables[a.value] = oldv / c.value



# <- built in funcs -----------------------

def interpret(line):
  lexerOBJ = lexer.LEXER()
  lexxed = lexerOBJ.lexLine(line)

  lx0val = lexxed[0].value
  
  if lexxed[0].type != "key":
    error = no_command_error(lx0val)
    print(error.invoke())
    return

  #might work
  if lx0val == "prnt":
    prnt_FUNC(lexxed[1:])
  elif lx0val == "defn":
    defn_FUNC(lexxed[1:])
  elif lx0val == "altv":
    altv_FUNC(lexxed[1:])
  #aint NO way it worked

while True:
  print("I for interpreter, O to load file")
  choice = input("choose>")
  if choice.upper() == "I":
    while True:
      x = input("run>")
      if x == "EXIT":
        break
      if x:
        interpret(x)
    break
  elif choice.upper() == "O":
    f = input("enter filename (.txt)")
    file = open(f, "r")
    for line in file:
      if line:
        interpret(line)
    input("press any enter to continue")
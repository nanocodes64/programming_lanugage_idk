import lexer

################### -> W A R N I N G | CURRENTLY UNUSED!
# funcs 1
# ops 2 set
# var / literals 
################### -> W A R N I N G | CURRENTLY UNUSED!

class AST:
  primitive_funcs = {
    "PRNT":"PrintInvoke",
    "DEFN":"DefineVariable",
    "ALTV":"AlterVariable"
  }
  primitive_ops = {
    "ADD":"AdditionOperation",
    "SET":"SetOperation",
    "SUB":"SubtractOperation",
    "MUL":"MultiplyOperation",
    "DIV":"DivideOperation",
    "DEL":"DeleteOperation"
  }
  primitive_misc = {
    "VAR":"Variable"
  }
  primitive_lits = {
    "str":"StringLiteral",
    "num_i":"IntergerLiteral"
  }
  literals = [
    "str",
    "num_i"
  ]

class Node(AST):
  def __init__(self, type, left=None, right=None):
    self.type, self.value = type, None
    self.left, self.right = left, right
  def __repr__(self):
    return self.type

def parseToAST(tokens):
  nodelist = []
  for i, token in enumerate(tokens):
    if token.type == "key":
      if token.value not in AST.primitive_funcs:
        return None
      nodelist.append(Node(AST.primitive_funcs[token.value]))

    if token.type == "id":
      if token.value not in AST.primitive_ops:
        nodelist.append(Node(AST.primitive_misc["VAR"]))
      else:
        nodelist.append(Node(AST.primitive_ops[token.value]))
    if token.type in AST.literals:
      nodelist.append(Node(AST.primitive_lits[token.type]))

  

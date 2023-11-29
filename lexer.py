class TOKEN:

  def __init__(self, type, value):
    self.type, self.value = type, value

  def __repr__(self):
    return f"TOKEN(TYPE:{self.type}, VALUE:{self.value})"

class LEXER:

  num_i = "int"
  #num_f = "float" # UNUSED ATM!!
  string = "str"
  identifier = "id"
  quotation = '"'

  def __init__(self):
    pass
  
  def lexLine(self, line):  #returns array of tokens
    curr_chr = 0

    ret_tokens = []
    while curr_chr < len(line):
      chr_rn = line[curr_chr]
      if chr_rn.isalpha():
        token, type, chr_passed = self._identifier(line[curr_chr:])
      elif chr_rn.isdigit():
        token, type, chr_passed = self._numeral(line[curr_chr:])
      elif chr_rn == self.quotation:
        token, type, chr_passed = self._string(line[curr_chr:])
        chr_passed = chr_passed + 2
      else:
        curr_chr += 1
        continue  # skips below so doesnt create nil token

      ret_tokens.append(TOKEN(type, token))
      curr_chr += chr_passed

    return ret_tokens
  
  def _string(self, line):
    ret = ""  # just placeholder

    i = 1

    while i < len(line):
      rn = line[i]
      if rn == self.quotation:
        break
      ret += rn
      i += 1

    return ret, self.string, len(ret)


  def _numeral(self, line):

    ret = ""

    for i in line:
      if not i.isdigit():
        break
      ret += i

    return int(ret), self.num_i, len(ret)


  def _identifier(self, line):

    ret = ""

    for i in line:
      if not i.isalpha():
        break
      ret += i

    return ret, self.identifier, len(ret)


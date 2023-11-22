num_i = "num_i"
num_f = "num_f"
string = "str"
identifier = "id"
quotation = '"'
keyword, keywords = "key", ["prnt", "altv", "defn"]

#these are functions, prnt being print, altv altering variables, defn defining vars


#PRIMITIVES ->
def _string(line):
  ret = ""  # just placeholder

  i = 1

  while i < len(line):
    rn = line[i]
    if rn == quotation:
      break
    ret += rn
    i += 1

  return ret, string, len(ret)


def _numeral(line):

  ret = ""

  for i in line:
    if not i.isdigit():
      break
    ret += i

  return int(ret), num_i, len(ret)


def _identifier(line):

  ret = ""

  for i in line:
    if not i.isalpha():
      break
    ret += i

  if ret in keywords:
    return ret, keyword, len(ret)
  return ret, identifier, len(ret)


# <- PRIMITIVES


class TOKEN:

  def __init__(self, type, value):
    self.type, self.value = type, value

  def __repr__(self):
    return f"TOKEN(TYPE:{self.type}, VALUE:{self.value})"


class LEXER:

  def __init__(self):
    pass

  def lexLine(self, line):  #returns array of tokens
    curr_chr = 0

    ret_tokens = []
    while curr_chr < len(line):
      chr_rn = line[curr_chr]
      if chr_rn.isalpha():
        token, type, chr_passed = _identifier(line[curr_chr:])
      elif chr_rn.isdigit():
        token, type, chr_passed = _numeral(line[curr_chr:])
      elif chr_rn == quotation:
        token, type, chr_passed = _string(line[curr_chr:])
        chr_passed = chr_passed + 2
      else:
        curr_chr += 1
        continue  # skips below so doesnt create nil token

      ret_tokens.append(TOKEN(type, token))
      curr_chr += chr_passed

    return ret_tokens



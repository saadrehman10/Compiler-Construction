""" -----------WORD SPLITER LOGICS------- """
def splitByN(fileContents):
    word = []
    current = ""
    for char in fileContents:
        if char == "\n":
            word.append(current)
            current = ""
        else:
            current += char
    word.append(current)
    return word




def splitBySpace(fileContents):
    
    words = []
    while fileContents:
        index = fileContents.find (" ")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        fileContents = fileContents[index + 1:]
    return words

""" ----------CHT GPT LOGICS-------- """
    
def break_and_concat(string):
  parts = string.split('=')
  output = []
  for part in parts[:-1]:
    output.append(part)
    output.append('=')
  output.append(parts[-1])
  return output



def break_and_concat(string):
  parts = []
  part = ""
  for char in string:
    if char == '=':
      parts.append(part)
      part = ""
    else:
      part += char
  parts.append(part)
  output = []
  for part in parts[:-1]:
    output.append(part)
    output.append('=')
  output.append(parts[-1])
  return output
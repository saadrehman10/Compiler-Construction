import identifier as id
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

# ============= Function that check it is string or not =================
def is_string(input_val):
    """
    Checks if the input is a string.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a string, False otherwise.
    """


# ============= Function that check it is integer or not =================
def is_integer(input_val):
    """
    Checks if the input is an integer.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is an integer, False otherwise.
    """
    return isinstance(input_val, int)


# ============= Function that check it is Character or not =================
def is_character(input_val):
    """
    Checks if the input is a single character.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a single character, False otherwise.
    """
    return isinstance(input_val, str) and len(input_val) == 1



# ============= Function that check it is Boolean or not =================
def is_boolean(input_val):
    """
    Checks if the input is a boolean.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a boolean, False otherwise.
    """
    return isinstance(input_val, bool)




# ================ Function that check keyword ================
def is_in_array(input_val, array):
    """
    Checks if the input is present in the array.

    Parameters:
    input_val (any): The input to check.
    array (list): The array to search.

    Returns:
    bool: True if the input is present in the array, False otherwise.
    """
    return input_val in array




""" |[\[]|[\]]|[\{]|[\}]|[\;]|[\(+\)] """

def floatMaker(array):
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    print(commentIndices)
    i = 0
    while i < len(commentIndices):
        if len(commentIndices) < 2:
            break
        index1 = commentIndices[i] - 1
        index2 = commentIndices[i] + 1
        if id.isInteger(array[index1]) and id.isInteger(array[index2]):
            hold = str(array[index1]) + "." + str(array[index2])
            array[commentIndices[i] - 1] = hold
            array.pop(commentIndices[i])
            array.pop(commentIndices[i])
            commentIndices = [index for index in commentIndices if index > commentIndices[i] + 1]
        else:
            i += 1

    return array
arr = ['interface', ':', ':', 'A_B_C', 'while', '(', 'a', '.', 'b', '.', 'c', '<', '<', '<', '<', '<', '==', '78', '.', '65', 'b', '++', '+=', '56', '.', '75', 'ab', '7', '.', '11', '" abc "', '=', 'b', '=', 'c', 'string', 's', '=', "'", '\\\\\\', "'", '+', "'", '++', "'", 'n', "'", '+=', '35', "'", '\\\\', 'returnÂ', 'a', '&', '&', '==', '@bcee', '3423432']

print(floatMaker(arr))
import identifier as id
import re as regex
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

""" def floatMaker(array):
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    print(commentIndices)
    for i in commentIndices:
        if bool(regex.match(r"^[0-9]+[0-9]$|^[0-9]$", array[i-1])) and bool(regex.match(r"^[0-9]+[0-9]$|^[0-9]$", array[i+1])):
            hold = array[i-1] + array[i] + array[i+1]
            array[i-1] = hold
            array.pop(i)
            array.pop(i)
    return array
arr = ['interface', ':', ':', 'A_B_C', 'while', '(', 'a', '.', 'b', '.', 'c', '<', '<', '<', '<', '<', '==', '78', '.', '65', 'b', '++', '+=', '56', '.', '75', 'ab', '7', '.', '11', '" abc "', '=', 'b', '=', 'c', 'string', 's', '=', "'", '\\\\\\', "'", '+', "'", '++', "'", 'n', "'", '+=', '35', "'", '\\\\', 'returnÂ', 'a', '&', '&', '==', '@bcee', '3423432']

print(floatMaker(arr)) """



def floatMaker(array):
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    print(commentIndices)
    new_array = array[:]
    for i in commentIndices:
        if bool(regex.match(r"^\d*\.?\d+$", new_array[i-1])) and bool(regex.match(r"^\d*\.?\d+$", new_array[i+1])):
            hold = new_array[i-1] + new_array[i] + new_array[i+1]
            new_array[i-1] = hold
            new_array.pop(i)
            new_array.pop(i)
    return new_array


arr = ['interface', ':', ':', 'A_B_C', 'while', '(', 'a', '.', 'b', '.', 'c', '<', '<', '<', '<', '<', '==', '78', '.', '65', 'b', '++', '+=', '56', '.', '75', 'ab', '7', '.', '11', '" abc "', '=', 'b', '=', 'c', 'string', 's', '=', "'", '\\\\\\', "'", '+', "'", '++', "'", 'n', "'", '+=', '35', "'", '\\\\', 'returnÂ', 'a', '&', '&', '==', '@bcee', '3423432',".","2"]
print(floatMaker(arr))

#order matter for this part
""" tokenArray = []
for i in range (len(wordsArray)):
    
    if id.isInteger(wordsArray[i]):
        tokenArray.append("Integer")  
    elif id.isFloat(wordsArray[i]):
        tokenArray.append("Float")     
    elif id.isOperator(wordsArray[i]):
        tokenArray.append("Operator")  
    elif id.isComparator(wordsArray[i]):
       tokenArray.append("Comparator") 
    elif id.isAssignmentOperators(wordsArray[i]):
        tokenArray.append("Assignment-Operators") 
    elif id.isLogocalOperators(wordsArray[i]):
        tokenArray.append("Logical-Operators") 
    elif id.isTerminator(wordsArray[i]):
       tokenArray.append("Terminator")
    elif id.isPunctuator(wordsArray[i]):  
       tokenArray.append("Punctuator")             
    elif id.isBoolean(wordsArray[i]):
        tokenArray.append("Boolean") 
    elif id.isKeyword(wordsArray[i]):
       tokenArray.append("Keyword") 
    elif id.isCharacter(wordsArray[i]):
       tokenArray.append("Character")   
    elif id.isString(wordsArray[i]):
       tokenArray.append("String")                 
    else:
        tokenArray.append("Error")  """


""" -----xx-------test output------xx------- """


""" print (tokenArray) """


"""   while "\"" in array or "\'" in array:
       commentIndices1 = [i for i, elem in enumerate(array) if elem == "\""]#commentIndices1 = [i for i, elem in enumerate(array) if elem == "\""] ya function array ko itarate kar ka  index ko find kar raha ha or us ki index ko array ma store kar raha ha
                                                                            # index kar raha value nahi 
                                                                            # enumerate function array ko itarate kar ka index or value dono ko return kar raha ha
        commentIndices2 = [i for i, elem in enumerate(array) if elem == "\'"]#is ka seprate function banaya hai kiu ka ya error de raha tha
        if len(commentIndices1) < 2 or len(commentIndices2) < 2:
            break
        else:
            index1 = commentIndices1[0]
            index2 = commentIndices1[1] + 1   
            strArray = array[index1:index2]
            strArray= "".join(strArray)
            array[commentIndices1[0]] = strArray
            index1+=1
            index2+=1
            array = array[:index1] + array[index2:]   
    return array# array ko return kar raha ha """

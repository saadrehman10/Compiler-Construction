import re as regex
import identifier as id
def splitBySpace(fileContents):
    words = fileContents.split()
    return words


def splitByN(fileContents):
    words = []
    while fileContents:
        index = fileContents.find (r"\n")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        fileContents = fileContents[index + 1:]
    return words


def splitBy(fileContents,splitString): 
    words = []
    while fileContents:
        index = fileContents.find (splitString)
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        words.append (splitString)
        fileContents = fileContents[index + 1:]
    return words



def arrayConcatenationSame(array,operater):
    index1 = 0
    index2 = 1
    for i in range(len(array)):
        if index2 >= len(array): 
            break  
        if array[index1] == operater and array[index2] == operater:
            hold = array[index1] + array[index2]
            array[index1] = hold
            array.pop(index2)
        else:  
            index1 += 1
            index2 += 1

    return array

def arrayConcatenationOdd(array,operater01,operater02):
    index1 = 0
    index2 = 1
    
    for i in range(len(array)):
        if index2 >= len(array): 
            break  
        if array[index1] == operater01 and array[index2] == operater02:
            hold = array[index1] + array[index2]
            array[index1] = hold
            array.pop(index2)
        else:  
            index1 += 1
            index2 += 1

    return array

def commentChecker(array):
    while "##" in array:
        commentIndices = [i for i, elem in enumerate(array) if elem == "##"]
        if len(commentIndices) < 2:
            break
        index1 = commentIndices[0]
        index2 = commentIndices[1] + 1
        array = array[:index1] + array[index2:]

    return array

def commaStringChecker(array):
    while "\"" in array or "\'" in array:
        commentIndices1 = [i for i, elem in enumerate(array) if elem == "\""]
        commentIndices2 = [i for i, elem in enumerate(array) if elem == "\'"]
        if len(commentIndices1) < 2 or len(commentIndices2) < 2:
            break
        index1 = commentIndices1[0]
        index2 = commentIndices1[1] + 1   
        strArray = array[index1:index2]
        strArray= " ".join(strArray)
        array[commentIndices1[0]] = strArray
        index1+=1
        index2+=1
        array = array[:index1] + array[index2:]   
    return array


def someThingCheck(array):
    for i in range(len(array)):
        if id.isStrOrInt(array[i]):
            pattern = r"\d+|[a-zA-Z]+"
            holdArray = regex.findall(pattern, array[i])
            arr = []
            arr.append(holdArray[0])
            holdArray = holdArray[1:]
            temp = "".join(element for element in holdArray)
            arr.append(temp)
            array[i] = arr
    return array



def floatMakerType1(array):
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    for i in range (len(commentIndices)):
        try:
            commentIndices2 = [i for i, elem in enumerate(array) if elem == "."]
            index1 = commentIndices2[i] - 1
            index2 = commentIndices2[i] + 1
            if id.isInteger(array[index1]) and id.isInteger(array[index2]):
                hold = array[index1] +"."+ array[index2]
                array[index1] = hold
                array.pop(commentIndices2[i])
                array.pop(commentIndices2[i])  
        except Exception as e:
            array = floatMakerType1(array)
                        
    return array

def floatMakerType2(array):
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    for i in range (len(commentIndices)):
        try:
            commentIndices2 = [i for i, elem in enumerate(array) if elem == "."]
            index1 = commentIndices2[i] 
            index2 = commentIndices2[i] + 1
            if array[index1] == "." and id.isInteger(array[index2]):
                hold = "0" +"."+ array[index2]
                array[index1] = hold
                array.pop(commentIndices2[i]+1)
        except Exception as e:
            array = floatMakerType2(array)
                        
    return array


    
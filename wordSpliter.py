
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
        words.append ("\n")
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
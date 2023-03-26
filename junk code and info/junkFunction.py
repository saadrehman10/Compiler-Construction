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
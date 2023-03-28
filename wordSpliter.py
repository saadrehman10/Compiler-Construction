
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

def splitByEquals(fileContents):
    word = []
    current = ""
    for char in fileContents:
        if char == "=":
            word.append(current)
            current = ""
        else:
            current += char
    word.append(current)
    return word

    """ words = []
    while fileContents:
        index = fileContents.find ("=")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        fileContents = fileContents[index + 1:]
    return words """


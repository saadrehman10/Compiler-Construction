
def splitBySpace(fileContents):
    words = fileContents.split()
    return words

def splitByN(fileContents):

    words = []
    while fileContents:
        index = fileContents.find ("\\n")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        fileContents = fileContents[index + 1:]
    return words


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


def splitByEquals(fileContents):
 
    words = []
    while fileContents:
        index = fileContents.find ("=")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])
        words.append ("=")
        fileContents = fileContents[index + 1:]
    return words


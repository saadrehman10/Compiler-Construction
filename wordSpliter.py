import fileHandler

def splitBySpace(fileContents):
    words = fileContents.split()
    return words
    
def splitByN(fileContents):
    words = fileContents.split("\\n")
    return words 
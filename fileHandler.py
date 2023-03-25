
def createFile(fileName, userCode):
    with open(fileName, 'w') as file:
     file.write(userCode)
     file.close


def readFile(fileName):
     with open(fileName,'r') as file:
      fileContents = file.read()
      return fileContents
      

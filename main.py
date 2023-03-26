import fileHandler
import wordSpliter


"""-----xx------functions for main-----xx------"""

def arrayFlattener(array):
  result = []
  for element in array:
    if isinstance(element, list):
      result.extend(arrayFlattener(element))
    else:
      result.append(element)
  return result

"""-----xx------main-----xx------"""

codeLines = int(input("Enter the no of Lines you need: "))-1
userCode = str(input("Enter your code: \n")+r"\n")



fileNameMain01 = "usercode.txt"
fileHandler.createFile(fileNameMain01,userCode )
for i in range(codeLines):
    fileHandler.appendFile(fileNameMain01,input()+r"\n")




fileContentsMain = fileHandler.readFile(fileNameMain01)
wordsArray = wordSpliter.splitByN(fileContentsMain)


arrLen = len(wordsArray)
for i in range (arrLen):
    wordsArray[i] = wordSpliter.splitBySpace(wordsArray[i])


print (wordsArray)

result = arrayFlattener(wordsArray)
print(result)
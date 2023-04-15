import fileHandler
import wordSpliter


"""-----xx-----------xx-----------xx------FUNCTIONS FOR MAIN-----xx-----------xx-----------xx-----------xx------"""

def arrayFlattener(array):
  result = []
  for element in array:
    if isinstance(element, list):
      result.extend(arrayFlattener(element))
    else:
      result.append(element)
  return result

"""-----xx-----------xx-----------xx-----------xx------MAIN-----xx-----------xx-----------xx-----------xx------"""

codeLines = int(input("Enter the no of Lines you need: "))-1
userCode = str(input("Enter your code: \n1. ")+r"\n")
fileNameMain01 = "usercode.txt"
fileHandler.createFile(fileNameMain01,userCode )
for i in range(codeLines):
    var01 = input(str(i+2)+". ")
    fileHandler.appendFile(fileNameMain01,var01+r"\n")

print("COMPILING")

"""------xx------WORD SPLITTER-----xx-------"""
fileContentsMain = fileHandler.readFile(fileNameMain01)
wordsArray = wordSpliter.splitByN(fileContentsMain)

arrLen = len(wordsArray)
for i in range (arrLen):
    wordsArray[i] = wordSpliter.splitBySpace(wordsArray[i])  
wordsArray = arrayFlattener(wordsArray)

splitArray = ["=",";",":","#","+","-","*","/","%","(",")","{","}","[","]","|","&"]

for i in splitArray:
  arrLen = len(wordsArray)
  for j in range (arrLen):
      wordsArray[j] = wordSpliter.splitBy(wordsArray[j],i)
  wordsArray = arrayFlattener(wordsArray)
    


"""-----xx-------test output------xx-------"""


print (wordsArray)



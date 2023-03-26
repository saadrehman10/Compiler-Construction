import fileHandler
import wordSpliter




"""-----xx------main-----xx------"""

codeLines = int(input("Enter the no of Lines you need: "))-1
userCode = str(input("Enter your code: \n")+r"\n")
fileNameMain01 = "usercode.txt"
fileHandler.createFile(fileNameMain01,userCode )
for i in range(codeLines):
    fileHandler.appendFile(fileNameMain01,input()+r"\n")




fileContentsMain = fileHandler.readFile(fileNameMain01)
wordsArray = wordSpliter.splitBySpace(fileContentsMain)
arrLen = len(wordsArray)
for i in range (arrLen):
    wordsArray[i] = wordSpliter.splitByN(wordsArray[i])


print (wordsArray)
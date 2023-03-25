import identifier
import fileHandler
import wordSpliter



"""-----xx------main-----xx------"""

userCode = str(input("Enter your code: \n"))
fileNameMain01 = "usercode.txt"
fileHandler.createFile(fileNameMain01,userCode )

fileContentsMain = fileHandler.readFile(fileNameMain01)
wordsArray = wordSpliter.splitBySpace(fileContentsMain)

#saad 
# yar array ko dubara array ma kas type cast kara ga?

testVar =(str(wordsArray))
fileNameMain02 = "userCodeSplit.txt"
fileHandler.createFile(fileNameMain02,testVar)
testArray= fileHandler.readFile(fileNameMain02)
# yha check karo 
print(type(testArray))
print(testArray)


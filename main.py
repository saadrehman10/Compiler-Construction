import identifier
import fileHandler
import wordSpliter



"""-----xx------main-----xx------"""

userCode = str(input("Enter your code: \n"))
fileNameMain01 = "usercode.txt"
fileHandler.createFile(fileNameMain01,userCode )

fileContentsMain = fileHandler.readFile(fileNameMain01)
wordsArray = wordSpliter.splitBySpace(fileContentsMain)

# comments by saad
# yar ya dakh na ka usercodeSplite.txt ma none  kiu save ho rah ah
# or ya bhi dakh na ka har bar arra khud print kiu ho ta ha kahi print kia nahi ha
# or array ko hum log derict nahi save kar sakta kia txt ma koi or file formate usr kar na para ? ?  

testVar =(str(wordsArray))
fileNameMain02 = "UserCodeSplit"
fileHandler.createFile(fileNameMain02,testVar)
testArray= fileHandler.readFile(fileNameMain02)

print(testArray)
print(testArray)
print(testArray)
print(testArray)
print(testArray)

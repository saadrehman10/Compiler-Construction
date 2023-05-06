import fileHandler as fh
import wordSpliter as ws
import identifier as id 

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
userCode = str(input("Enter your code: \n1. ")+" "+r"\n"+" ")
fileNameMain01 = "usercode.txt"
fh.createFile(fileNameMain01,userCode )
for i in range(codeLines):
    var01 = input(str(i+2)+". ")
    fh.appendFile(fileNameMain01,var01+" "+r"\n"+" ")

print("COMPILING")

"""------xx------WORD SPLITTER-----xx-------"""
fileContentsMain = fh.readFile(fileNameMain01)
wordsArray = ws.splitByN(fileContentsMain)


for i in range (len(wordsArray)):
    wordsArray[i] = ws.splitBySpace(wordsArray[i])  
wordsArray = arrayFlattener(wordsArray)

splitArray = ["=",";",":","#","+","-","*","/","%","(",")","{","}","[","]","|","\"","'","^","!","&","<",">","?"," "]

for i in splitArray:
  for j in range (len(wordsArray)):
      wordsArray[j] = ws.splitBy(wordsArray[j],i)
  wordsArray = arrayFlattener(wordsArray)

print (wordsArray)

"""------xx------id-----xx-------"""
#order matter for this part

for i in range (len(wordsArray)):
    
    if id.isInteger(wordsArray[i]):
        wordsArray[i] = "Integer" 
    elif id.isFloat(wordsArray[i]):
        wordsArray[i] = "Float"    
    elif id.isOperator(wordsArray[i]):
        wordsArray[i] = "Operator"  
    elif id.isComparator(wordsArray[i]):
        wordsArray[i] = "Comparator"  
    elif id.isAssignmentOperators(wordsArray[i]):
        wordsArray[i] = "Assignment-Operators"     
    elif id.isBoolean(wordsArray[i]):
        wordsArray[i] = "Boolean"
    elif id.isKeyword(wordsArray[i]):
       wordsArray[i] = "Keyword" 
    elif id.isCharacter(wordsArray[i]):
        wordsArray[i] = "Character"     
    elif id.isString(wordsArray[i]):
       wordsArray[i] = "String"   
                  
    else:
        wordsArray[i] = "Error"


"""-----xx-------test output------xx-------"""


print (wordsArray)




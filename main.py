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

""" codeLines = int(input("Enter the no of Lines you need: "))
userCode = str(input("Enter your code: \n1. "))
fileNameMain01 = "usercode.txt"
fh.createFile(fileNameMain01,userCode )
for i in range(codeLines):
    var01 = input(str(i+2)+". ")
    fh.appendFile(fileNameMain01,var01)

print("COMPILING")
 """
"""------xx------WORD SPLITTER-----xx-------"""
fileNameMain01 = "usercode.txt"
fileContentsMain = fh.readFile(fileNameMain01)
wordsArray = ws.splitByN(fileContentsMain)


for i in range (len(wordsArray)):
    wordsArray[i] = ws.splitBySpace(wordsArray[i])  
wordsArray = arrayFlattener(wordsArray)

splitArray = ["=",".",";",":","#","+","-","*","/","%","(",")","{","}","[","]",
              "|","\"","'","^","!","&","<",">","?"," "]

for i in splitArray:
  for j in range (len(wordsArray)):
      wordsArray[j] = ws.splitBy(wordsArray[j],i)
  wordsArray = arrayFlattener(wordsArray)


concatArray= ["=","+","-","#","/"]
for i in concatArray:
  wordsArray = ws.arrayConcatenationSame(wordsArray,i)
concatArray2= ["+","-","*","/","!","<",">"]
for i in concatArray2:
   wordsArray = ws.arrayConcatenationOdd(wordsArray,i,"=")
wordsArray = ws.arrayConcatenationOdd(wordsArray,"^","|")


wordsArray = ws.commentChecker(wordsArray)
print(wordsArray)
wordsArray = ws.commaStringChecker(wordsArray)
wordsArray = ws.someThingCheck(wordsArray)
print(wordsArray)
wordsArray = arrayFlattener(wordsArray)
print(wordsArray)
wordsArray = ws.floatMaker(wordsArray)

print(wordsArray)


"""------xx------id-----xx-------"""
#order matter for this part
""" tokenArray = []
for i in range (len(wordsArray)):
    
    if id.isInteger(wordsArray[i]):
        tokenArray.append("Integer")  
    elif id.isFloat(wordsArray[i]):
        tokenArray.append("Float")     
    elif id.isOperator(wordsArray[i]):
        tokenArray.append("Operator")  
    elif id.isComparator(wordsArray[i]):
       tokenArray.append("Comparator") 
    elif id.isAssignmentOperators(wordsArray[i]):
        tokenArray.append("Assignment-Operators") 
    elif id.isLogocalOperators(wordsArray[i]):
        tokenArray.append("Logical-Operators") 
    elif id.isTerminator(wordsArray[i]):
       tokenArray.append("Terminator")
    elif id.isPunctuator(wordsArray[i]):  
       tokenArray.append("Punctuator")             
    elif id.isBoolean(wordsArray[i]):
        tokenArray.append("Boolean") 
    elif id.isKeyword(wordsArray[i]):
       tokenArray.append("Keyword") 
    elif id.isCharacter(wordsArray[i]):
       tokenArray.append("Character")   
    elif id.isString(wordsArray[i]):
       tokenArray.append("String")                 
    else:
        tokenArray.append("Error")  """


""" -----xx-------test output------xx------- """


""" print (tokenArray) """
while True:
    pass
import fileHandler as fh
import wordSpliter as ws
import tokenGenrater as tg

"""-----xx-----------xx-----------xx------FUNCTIONS FOR MAIN-----xx-----------xx-----------xx-----------xx------"""

def arrayFlattener(array):# ya function nested array ko flat array ma convert kar ta ha
  result = []
  for element in array:
    if isinstance(element, list):
      result.extend(arrayFlattener(element))#ya recursion ka zaria multiple nested array ko flat array ma convert kar ta halike [[[][][]][][]] ya sab flat kar da ta ha
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
 #yha user sa input lana lana ka bad usercode.txt ma save kar raha ha with \n ka sath
"""------xx------WORD SPLITTER-----xx-------"""
fileNameMain01 = "usercode.txt"
fileContentsMain = fh.readFile(fileNameMain01)
wordsArray = ws.splitByN(fileContentsMain)
for i in range (len(wordsArray)):
    wordsArray[i] = ws.splitBySpace(wordsArray[i])  
wordsArray = arrayFlattener(wordsArray)#split by N and split by space ka bad jo nested array bani ha us ko flat array ma convert kar raha ha
splitArray = ["=",".",";",":","#","+","-","*","/","%","(",")","{","}","[","]",
              "|","\"","'","^","!","&","<",">","?"," "]#in cheezo par split kar raha ha
for i in splitArray:
  for j in range (len(wordsArray)):
      wordsArray[j] = ws.splitBy(wordsArray[j],i)
  wordsArray = arrayFlattener(wordsArray)
  # yaha sa jo array hama requried ha us ki creation ho rahi ha
  #ya sari anomilies ko remove kar rahi ha
concatArray= ["=","+","-","#","/"]
for i in concatArray:
  wordsArray = ws.arrayConcatenationSame(wordsArray,i)

concatArray2= ["+","-","*","/","!","<",">"]
for i in concatArray2:
   wordsArray = ws.arrayConcatenationOdd(wordsArray,i,"=")
wordsArray = ws.arrayConcatenationOdd(wordsArray,"^","|")

wordsArray = ws.commentChecker(wordsArray)
wordsArray = ws.commentCheckersingle(wordsArray)

wordsArray = ws.commaStringChecker(wordsArray)

wordsArray = ws.alphaNumeric(wordsArray)

wordsArray = arrayFlattener(wordsArray)

wordsArray = ws.floatMakerType1(wordsArray)

wordsArray = ws.floatMakerType2(wordsArray)

print(wordsArray)
"""------xx------id-----xx-------"""
#lexical analysis ka lia token genrater ko call kar raha ha
line_number = 1
for i in wordsArray:
    hold = tg.tokenGen(i, line_number)
    if isinstance(hold, int):
        line_number +=1 #ya line number ko update kar raha ha           
    elif isinstance(hold, list):
        print(hold)

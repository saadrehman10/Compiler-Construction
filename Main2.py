import fileHandler as fh
import wordSpliter as ws
import tokenGenrater as tg
from MainClass import MainClass
import sys

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
if __name__ == '__main__':
    fileNameMain01 = "usercode.txt"
    fileContentsMain = fh.readFile(fileNameMain01)
    final = MainClass(fileContentsMain)
    final.splitByN()
    final.splitBySpace()
    final.arrayFlattener()
    final.splitBy()
    final.SplitFromArray()
    final.concatArray()
    final.concatAgain()
    final.ExtraFunc()
    final.Token()
    sys.exit(final.words)



"""------xx------id-----xx-------"""

    
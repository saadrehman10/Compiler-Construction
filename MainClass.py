from main import arrayFlattener
import wordSpliter as ws
import tokenGenrater as tg
class MainClass:
    def __init__(self,fileContentsMain):
        self.fileContents = fileContentsMain
        self.words = []
        self.splitArray = ["=",".",";",":","#","+","-","*","/","%","(",")","{","}","[","]",
              "|","\"","'","^","!","&","<",">","?"," "]
        self.concatArray= ["=","+","-","#","/"]
        self.concatArray2= ["+","-","*","/","!","<",">"]

    def splitByN(self):# new line ka lia seprate function banaya hai kiu ka \n append nahi ho raha tha
                            #still ya error mojuid ha or is ko solve karna ha abhi ya "n" append kar raha ha
        while self.fileContents:
            index = self.fileContents.find (r"\n")
            if index == -1:
                self.words.append (self.fileContents)
                break
            self.words.append (self.fileContents[:index])#js ka sclice function sa word ko split kia ha [:index] is ma : sa phala wala part or index sa aga wala part
                                                #index ko ignore kar ka word ko split kar raha ha
            self.fileContents = self.fileContents[index + 1:]

    def splitBySpace(self):
        for i in range(0,len(self.words)):
            self.words[i] = self.fileContents.split()# space ko ignore kar na ka liya split ma koi argument nahi diya 

    def arrayFlattener(self):# ya function nested array ko flat array ma convert kar ta ha
        
        for element in self.words:
            if isinstance(element, list):
                self.words.extend(arrayFlattener(element))#ya recursion ka zaria multiple nested array ko flat array ma convert kar ta halike [[[][][]][][]] ya sab flat kar da ta ha
            else:
                self.words.append(element)



    def splitBy(fileContents,splitString): #Same as splitByN function but is ma splitString argument pass kia ha or is ma splitString ko ignore kar ka word ko split kar raha ha or bad ma splitString ko bhi append kar raha ha
        words = []
        while fileContents:
            index = fileContents.find (splitString)
            if index == -1:
                words.append (fileContents)
                break
            words.append (fileContents[:index])
            words.append (splitString)
            fileContents = fileContents[index + 1:]
        return words# array ko return kar raha ha


    def SplitFromArray(self):
         for i in self.splitArray:
            for j in range (len(self.words)):
                self.words[j] = self.splitBy(self.words[j],i)
            self.self.words = self.arrayFlattener(self.words)



    def concatArray(self):
        for i in self.concatArray:
            self.words = ws.arrayConcatenationSame( self.words,i)

    def concatAgain(self):
        for i in self.concatArray2:
            self.words = ws.arrayConcatenationOdd(self.words,i,"=")
        self.words = ws.arrayConcatenationOdd(self.words,"^","|")
    
    def ExtraFunc(self):
        self.words = ws.commentChecker(self.words)

        self.words = ws.commaStringChecker(self.words)

        self.words = ws.alphaNumeric(self.words)

        self.words = self.arrayFlattener(self.words)

        self.words = ws.floatMakerType1(self.words)

        self.words = ws.floatMakerType2(self.words)


    def Token(self):
        #lexical analysis ka lia token genrater ko call kar raha ha
        line_number = 1
        for i in self.words:
            hold = tg.tokenGen(i, line_number)
            if isinstance(hold, int):
                line_number +=1 #ya line number ko update kar raha ha           
            elif isinstance(hold, list):
                print(hold)
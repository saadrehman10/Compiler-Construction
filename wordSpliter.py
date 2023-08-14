import re as regex
import identifier as id
def splitBySpace(fileContents):
    words = fileContents.split()# space ko ignore kar na ka liya split ma koi argument nahi diya 
    return words# array ko return kar raha ha


def splitByN(fileContents):# new line ka lia seprate function banaya hai kiu ka \n append nahi ho raha tha
                        #still ya error mojuid ha or is ko solve karna ha abhi ya "n" append kar raha ha
    words = []
    while fileContents:
        index = fileContents.find (r"\n")
        if index == -1:
            words.append (fileContents)
            break
        words.append (fileContents[:index])#js ka sclice function sa word ko split kia ha [:index] is ma : sa phala wala part or index sa aga wala part
                                            #index ko ignore kar ka word ko split kar raha ha
        fileContents = fileContents[index + 1:]
    return words# array ko return kar raha ha


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



def arrayConcatenationSame(array,operater):# is fun ma array ma check kar ta ha ka gha par ++,--,// etc aya ha or us ko concatinate kar ta ha same operater ka ha
    index1 = 0
    index2 = 1
    for i in range(len(array)):
        if index2 >= len(array): 
            break  
        if array[index1] == operater and array[index2] == operater:# ya condition check kar ta ha ka gha par ++,--,// etc aya ha or us ko concatinate kar ta ha same operater ka ha
            hold = array[index1] + array[index2]
            array[index1] = hold
            array.pop(index2)
        else:  
            index1 += 1
            index2 += 1

    return array# array ko return kar raha ha

def arrayConcatenationOdd(array,operater01,operater02):#same as arrayConcatenationSame function but is ma operater01 or operater02 dono ko check kar ta ha
    index1 = 0
    index2 = 1
    
    for i in range(len(array)):
        if index2 >= len(array): 
            break  
        if array[index1] == operater01 and array[index2] == operater02:# sirf is condition ka lia banaya hai ka gha par operater01 or operater02 dono aya ha or us ko concatinate kar ta ha
            hold = array[index1] + array[index2]
            array[index1] = hold
            array.pop(index2)
        else:  
            index1 += 1
            index2 += 1

    return array# array ko return kar raha ha

def commentChecker(array):# is function ma array ma check kar ta ha ka gha par ## aya ha or us ka bad wala word ko remove kar ta ha
    commentIndices = [i for i, elem in enumerate(array) if elem == "##"]
    if len(commentIndices) == 1:
        index1 = array.index("##")
        array1 = array[index1:]
        temp = "".join(element for element in array1)
        array = array[:index1]
        array.append(temp)
        return array
    else:
        while "##" in array:
            if len(commentIndices) < 2:
                break
            index1 = commentIndices[0]
            index2 = commentIndices[1] + 1
            array = array[:index1] + array[index2:]
        return array# array ko return kar raha ha

def commentCheckersingle(array):# is function ma array ma check kar ta ha ka gha par ## aya ha or us ka bad wala word ko remove kar ta ha
    commentIndices = [i for i, elem in enumerate(array) if elem == "#"]
    commentIndices1 = [i for i, elem in enumerate(array) if elem == "n"]
    while "#" in array:
        index1 = commentIndices[0]
        index2 = commentIndices1[0] 
        array = array[:index1] + array[index2:]
    return array# array ko return kar raha ha    

    

def commaStringChecker(array):# is function ma array ma check kar ta ha ka gha par " aya ha or us ka bad wala word ko remove kar ta ha
    newArray1 = []
    i = 0
    while i < len(array):
        if "\"" in array[i] or "\'" in array[i]:
            quote = array[i]
            newArray1.append(quote)
            i += 1
            while i < len(array) and array[i] != quote:
                newArray1[-1] += array[i]
                i += 1
            if i < len(array):
                newArray1[-1] += array[i]
        else:
            newArray1.append(array[i])
        i += 1
    return newArray1




def alphaNumeric(array):# ya checck kar ta ha 77723324jhkhkj32234 is type ka string ko 77723324 jhkhkj 32234 is type ma split kar ta ha
                          # 77777 ya phala ana wala integer ko seprate kar ta ha or baki ka array ko concatinate kar ta ha
    for i in range(len(array)):
        if id.isStrOrInt(array[i]):
            pattern = r"\d+|[a-zA-Z]+"# is ma \d+ is type ka pattern ha ka 1 ya 1 sa zada integer ko find kar ta ha or | is ma or ka matlab ha
            holdArray = regex.findall(pattern, array[i])
            arr = []
            arr.append(holdArray[0])
            holdArray = holdArray[1:]
            temp = "".join(element for element in holdArray)
            arr.append(temp)
            array[i] = arr
    return array# array ko return kar raha ha



def floatMakerType1(array):# ya function "44" "." "3343" jasa float ko 44.3343 ma convert kar ta ha
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    for i in range (len(commentIndices)):
        try:
            commentIndices2 = [i for i, elem in enumerate(array) if elem == "."]
            index1 = commentIndices2[i] - 1
            index2 = commentIndices2[i] + 1
            if id.isInteger(array[index1]) and id.isInteger(array[index2]):
                hold = array[index1] +"."+ array[index2]
                array[index1] = hold
                array.pop(commentIndices2[i])
                array.pop(commentIndices2[i])  
        except Exception as e:
            array = floatMakerType1(array)#agar index odd ma ho to wo out of range ho gata ha last value par ya kabhi kabhi middle par so recurrsion ka zarya solve kar raha ha dubara appna hi function ko call kar ka

                        
    return array# array ko return kar raha ha

def floatMakerType2(array):# ya function "." "3343" jasa float ko 0.3343 ma convert kar ta ha
    commentIndices = [i for i, elem in enumerate(array) if elem == "."]
    for i in range (len(commentIndices)):
        try:
            commentIndices2 = [i for i, elem in enumerate(array) if elem == "."]
            index1 = commentIndices2[i] 
            index2 = commentIndices2[i] + 1
            if array[index1] == "." and id.isInteger(array[index2]):
                hold = "0" +"."+ array[index2]
                array[index1] = hold
                array.pop(commentIndices2[i]+1)
        except Exception as e:
            array = floatMakerType2(array)# agar index odd ma ho to wo out of range ho gata ha last value par ya kabhi kabhi middle par so recurrsion ka zarya solve kar raha ha dubara appna hi function ko call kar ka
                        
    return array# array ko return kar raha ha


    
import identifier as id


def tokenGen(words, line_number):
    tokenArray = []
    if words == "n":# ya wahi new line ka lia ha jo wordSpliter.py ma ha error ha set kar na ha
        return line_number
    else:    
        if id.isInteger(words):
            tokenArray.append(('Integer', words, line_number))  
        elif id.isFloat(words):
            tokenArray.append(('Float', words, line_number))     
        elif id.isOperator(words):
            tokenArray.append(('Operater', words, line_number)) 
        elif id.isComparator(words):
            tokenArray.append(('Commparator', words, line_number))  
        elif id.isAssignmentOperators(words):
            tokenArray.append(('Assigment-Operater', words, line_number)) 
        elif id.isLogocalOperators(words):
            tokenArray.append(('Logical-Operater', words, line_number)) 
        elif id.isTerminator(words):
            tokenArray.append(('Terminator', words, line_number)) 
        elif id.isString01(words):
            tokenArray.append(('String', words, line_number))    
        elif id.isComa(words):  
            tokenArray.append(('Invalid', words, line_number))          
        elif id.isPunctuator(words):  
            tokenArray.append(('Punctuator', words, line_number))             
        elif id.isBoolean(words):
            tokenArray.append(('Boolean', words, line_number)) 
        elif id.isKeyword(words):
            tokenArray.append(('Keyword', words, line_number)) 
        elif id.isCharacter(words):
            tokenArray.append(('Identifier', words, line_number))   
        elif id.isString(words):
            tokenArray.append(('Identifier', words, line_number))                  
        else:
            tokenArray.append(('Invalid', words, line_number)) 
        return tokenArray
    
 
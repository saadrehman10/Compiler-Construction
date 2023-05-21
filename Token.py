from identifier import isString,isInteger,isKeyword
words = ['interface', ':', ':', 'A_B_C', 'while','-', '(', '\n', 'a.b.c', '<', '<', '<', '<', '<', '==', '78.65', 'b', '++',
         '+=', '56.75ab7.11', '\n', '"', 'abc', '"', 'a', '=', 'b', '=', 'c', 'string', 's', '=', "'", '\\\\\\', "'",
         '+', "'", '++', "'", 'n', "'", '+=', '35', "'", '\\\\', 'returnÂ', 'a', '&', '&', '==', '@bc']
keywords = ['interface', 'while','string','bprint','action','return']
punctuators = ['(', ')', '{', '}', '[', ']', ',', '.', ';', ':']
operators = ['+', '-', '*', '/', '=', '==', '!=', '>', '<', '>=', '<=']
string_literals = ["'", '"']



tokens = []
line_number = 1
for i in range(0,len(words)):
    if isKeyword(words[i]):
        tokens.append(('Keyword', words[i], line_number))
    
    elif words[i] == '\n':
        line_number = line_number + 1
    
    elif words[i] in operators:
        tokens.append(('operator', words[i], line_number))
    
    
    elif words[i] in punctuators:
        tokens.append(('punctuators', words[i], line_number))
    
    elif words[i] in string_literals:
        tokens.append(('string_literals', words[i], line_number))
    


    
    elif words[i] == '++':
        tokens.append(('++', words[i], line_number))

    
    elif words[i] == '--':
        tokens.append(('--', words[i], line_number))

    

    elif isString(words[i]):
        tokens.append(('string', words[i], line_number))
    
    
    


    
    
    
    

print(tokens)
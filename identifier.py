import re as regex

def isKeyword(element):
    keyword = ['if', 'else', 'elif', 'while',
        'for', 'in',  'break', 'continue',
        'return', 'import', 'from',  'global', 
        'pass', 'try', 'except',  'with',  
        'None','render']
    if element in keyword:
        return True
    else:
        return False
    

def isInteger(element):
        pattern = r"^[0-9]+[0-9]$|^[0-9]$"
        return bool(regex.match(pattern, element))

    
def isString(element):
        pattern = r"^[a-zA-Z0-9]+$"
        return bool(regex.match(pattern, element))


def isCharacter(element):
        pattern = r"^[a-zA-Z]$"
        return bool(regex.match(pattern, element))
    

def isBoolean(element):
        pattern = r"^(True|False|true|false)$"
        return bool(regex.match(pattern, element))


def isFloat(element):
        pattern = r"(^[0-9]+[0-9]|^[0-9])+(\.[0-9]+[0-9]$|\.[0-9])$"
        return bool(regex.match(pattern, element))
    

def isOperator(element):
        pattern = r"^[\+]|[\-]|[\/]|[\*]|[\%]|[\^]|[\/+\/]$"
        return bool(regex.match(pattern, element))


def isComparator(element):
        pattern = r"^[\<]|[\>]|[\=+\<]|[\=+\>]|[\=+\=]|[\=+\=+\=]|[\!+\=]$"
        return bool(regex.match(pattern, element))



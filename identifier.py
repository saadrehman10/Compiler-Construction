import re as regex

def isKeyword(element):
    keyword = ['if', 'else', 'elif', 'while',
        'for', 'stop', 'pass','return', 'carryon'
        'bprint','render','action','pub','take','package'
        'pvt','lock','unlock','char','int','float','str','interface', 'while','string','bprint','action','return']

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

def isTerminator(element):
        pattern = r"^\:|\;|\#|\#+\#$"
        return bool(regex.match(pattern, element))

def isPunctuator(element):
        pattern = r"^\[|\]|\{|\}|\(|\)|\'|\"|\?|\,$"
        return bool(regex.match(pattern, element))
    

def isOperator(element):
        pattern = r"^\+|\-|\/|\*|\%|\^|\/+\/|\++\+|\-+\-$"
        return bool(regex.match(pattern, element))


def isComparator(element):
        pattern = r"^\<|\>|\=+\<|\=+\>|\=+\=|\!+\=$"
        return bool(regex.match(pattern, element))

def isAssignmentOperators(element):
        pattern = r"^\=|\++\=|\-+\=|\*+\=|\/+\=|\%+\=$"
        return bool(regex.match(pattern, element))

def isLogocalOperators(element):
        pattern = r"^\&|\||\^+\|$"
        return bool(regex.match(pattern, element))

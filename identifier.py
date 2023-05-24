import re as regex

def isKeyword(element):
    keyword = ['if', 'else', 'elif', 'while',
        'for', 'stop', 'pass','return', 'carryon'
        'bprint','render','action','pub','take','package'
        'pvt','lock','unlock','char','int','float','str',
        'interface', 'while','string','bprint','action','return']#remove the line after testing

    if element in keyword:
        return True
    else:
        return False
    
# sara true ya false return kar raha ha
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
        pattern = r"^\[|\]|\{|\}|\(|\)|\'|\"|\?|\,|\.$"
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

def isStrOrInt(element):
        pattern = r"^\d+[a-zA-Z].+$"
        return bool(regex.match(pattern, element))

def isFloatCheck(element):
        pattern = r"^[0-9]+\.[0-9]+$"
        return bool(regex.match(pattern, element))

def isString01(element):
        pattern = r'"[^"]*"'
        return bool(regex.match(pattern, element))
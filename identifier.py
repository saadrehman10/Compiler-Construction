import re as regex


def isInteger(element):
    if isinstance(element, int):
        return True
    elif isinstance(element, str):
        pattern = r"^[0-9]$"
        return bool(regex.match(pattern, element))
    else:
        return False
    

def isString(element):
    if isinstance(element, str):
        return True
    elif isinstance(element, str):
        pattern = r"^([a-z0-9A-Z]{5,})$"
        return bool(regex.match(pattern, element))
    else:
        return False
    

def isCharacter(element):
    if isinstance(element, str):
        pattern = r"^[a-zA-Z]$"
        return bool(regex.match(pattern, element))
    else:
        return False
    

def isBoolean(element):
    if isinstance(element, bool):
        return True
    elif isinstance(element, str):
        pattern = r"^(True|False)$"
        return bool(regex.match(pattern, element))
    else:
        return False


keyword = ['if','in']

def isKeyword(element):
    if element in keyword:
        return "Given Element is Keyword"
    else:
        return "Given Element is not a Keyword"





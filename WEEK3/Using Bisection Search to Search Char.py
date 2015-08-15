def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if aStr == '' or len(aStr) == 0:
        return False

    mid = aStr[(len(aStr)/2)]

    if char == mid:
        return True

    else:
        if char < mid:
            return isIn(char, aStr[:-1])
        elif char > mid:
            return isIn(char, aStr[1:])
    return isIn(char, aStr)


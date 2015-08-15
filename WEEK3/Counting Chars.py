__author__ = 'SWAPNIL'
def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0

    length = 1
    if aStr[: -1] == '':
        return 1

    return length + lenRecur(aStr[:-1])



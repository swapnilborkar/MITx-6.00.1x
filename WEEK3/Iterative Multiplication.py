__author__ = 'SWAPNIL'
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1.000
    while exp > 0:
        result = result * base
        exp -= 1
    return result

iterPower(2, 4)
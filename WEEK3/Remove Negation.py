__author__ = 'SWAPNIL'
def removeNegation(a):
    if a < 0:
        return a * -1
    else:
        return a

applyToEach(testList, removeNegation)
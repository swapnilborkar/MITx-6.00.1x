__author__ = 'SWAPNIL'
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict.values():
        count += len(i)
    return count
__author__ = 'SWAPNIL'
def oddTuples(aTup):
    '''

    :param aTup: Tuple
    :return: Tuples on odd indexes
    '''

    if aTup:
        return (aTup[0],) + oddTuples(aTup[2:])
    else:
        return ()
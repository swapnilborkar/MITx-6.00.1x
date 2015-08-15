__author__ = 'SWAPNIL'
def printMove(fr, to):
    '''
    :param fr:
    :param to:
    :return:
    '''

    print("Move from " + str(fr) + " to " + str(to))

def towers(n, fr, to, sp):
    '''

    :param n:
    :param fr:
    :param to:
    :param sp:
    :return:
    '''

    if n==1:
        printMove(fr, to)
    else:
        towers(n-1, fr, sp, to)
        towers(1, fr, to, sp)
        towers(n-1, sp, to, fr)

towers(5, "Source", "Destination", "Spare")
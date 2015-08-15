__author__ = 'SWAPNIL'

def isPalindrome(s):
    '''

    :param s: str
    :return:
    '''

    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        print(ans)

    def isPal(s):
        if len(s) <= 1:
            print(True)
        else:
            print(s[0]==s[-1] and isPal(s[1: -1]))
    print(isPal(toChars(s)))

isPalindrome('cat')
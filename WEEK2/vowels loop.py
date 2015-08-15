__author__ = 'SWAPNIL'

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = str.lower(char)
    if char in 'aeiou':
      return True
    else:
        return False

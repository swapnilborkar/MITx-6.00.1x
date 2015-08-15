__author__ = 'SWAPNIL'
#Newton Raphson for Sqr Root

epsilon = 0.01
y = 12345.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print("Square Root of " + str(y) + " is " + str(guess))
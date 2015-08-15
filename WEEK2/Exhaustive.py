x = 12345
epsilon = 0.01
step = epsilon**2
guesses = 0
ans = 0.0
while(abs(ans**2-x)) >= epsilon and ans<=x:
    ans = ans + step
    guesses = guesses + 1
print("Guesses Taken: " +str(guesses))
if abs(ans**2-x) >= epsilon:
    print("Failed on Sqr Root of:  "+ str(x))
else:
    print(str(ans)+" is close to square root of" + str(x))
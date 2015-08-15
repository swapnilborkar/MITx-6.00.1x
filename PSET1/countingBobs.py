__author__ = 'SWAPNIL'
lengthS= len(s)
bob='bob'
lengthBob=len(bob)
count=0

for i in range(lengthS-1):
    if s[i: i + lengthBob]==bob:
        count+=1
    else:
        count+=0
print("Number of times bob occurs is: "+ str(count))
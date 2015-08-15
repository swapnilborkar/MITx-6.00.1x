begin=0
end=100
choice=""
print("Please think of a number between 0 and 100!")
while choice!='c':

    mid=(begin+end)/2
    print("Is your secret number "+ str(mid) +"?")
    choice=raw_input(" Enter 'h' to indicate the guess is too high."
    " Enter 'l' to indicate the guess is too low."
    " Enter 'c' to indicate the guess is correct.")


    if choice == 'h':
        end = mid
    elif choice == 'l':
        begin = mid
    elif choice == 'c':
        print("Game over. Your secret number was: " + str(mid))
    else:
        print("Invalid Input. Try Again")


low = 1
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("Press Enter to start the game")

guess = 1
guesses = 1
while low != high:
    print("\t Guessing in the range {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
        # guess higher. the low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # guess lower. the higher end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h, l or c")
    #guesses = guesses + 1 - here the python creates a new variable
    guesses += 1 # this is called augmented assignment # here python reuses the same variable
else:
    print("You thought of a number {}".format(low))
    print("I got it in {} guesses".format(guesses))
import random

answer = random.randint(0, 10)
print(answer) #TODO: Remove after testing


print("Please guess a number within 1 and 10, enter 0 to exit the game: ")
while True:
    guess = int(input())
    if guess == 0:
        print("exit")
        break
    elif guess == answer:
        print("You guessed it right")
        break
    elif guess < answer:
        print("please guess higher")
    elif guess > answer:
        print("please guess Lower")

    # if guess < answer:
    #     print("please guess higher")
    # else:
    #     print("please guess lower")
    # guess = int(input())
    # if guess == answer:
    #     print("Well done, you guessed it")
    # else:
    #     print("Sorry you guessed it wrong")



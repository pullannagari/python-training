import random


def get_integer(prompt):
    """
    Get an Integer from Standard Input(stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Enter a valid interger value")


print(get_integer.__doc__)
print("*" * 80)
help(get_integer)

answer = random.randint(0, 10)
print(answer) #TODO: Remove after testing


print("Please guess a number within 1 and 10, enter 0 to exit the game: ")
while True:
    guess = get_integer(": ")
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
name = input("Please enter your name: ")
age = int(input("How old are you, {}?".format(name)))

if 18 <= age < 31:
    print("Welcome to the club, {}".format(name))
else:
    print("Sorry club is only for cool people")
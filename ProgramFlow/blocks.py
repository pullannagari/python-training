name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
elif age == 9:
    print("Sorry, Yoda, you aren't born in Return of the Jedi")
else:
    print("Please comeback in {} years".format(18 - age))


# for i in range(1, 13):
#     print("No. {} squared is {} and qubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)


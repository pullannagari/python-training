day = "Saturday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) and not raining: #Paranthesis is not necessary but makes it clear and less ambiguous code
    print("Go swimming")
else:
    print("Learn Python")

# 0 evaluates to false
if 0:
    print("True") #unreachable code
else:
    print("False")
# "" string evaluates to false
name = input("Please enter your name: ")
if name: #same as name != ""
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
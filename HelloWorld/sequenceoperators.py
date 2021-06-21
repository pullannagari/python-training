string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print(
    "he's " "probably " "pining " "for the " "fjords")  # strings can be concatenated without the + operator, not recommended

print("Hello " * 5)
# print("Hello " * 5 + 4) #evaluates to an error owing to operator precedence
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)
print("thurs" in today)

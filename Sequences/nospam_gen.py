menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"]
]

# using if condition
for meal in menu:
    if "spam" in meal:
        items = ", ".join(item for item in meal if item != "spam")
        print(items)
        # for item in meal:
        #     if item != "spam":
        #         print(item, end=", ")
    else:
        print(meal)
    print()

print("@"*80)
# using remove

# for meal in menu:
#     if "spam" in meal:
#         for item in meal:
#             if item == "spam":
#                 meal.remove(item)
#     print(meal)

# the above code works but is not recommended in python,
# always loop from backwards when modifying the list within the loop

for meal in menu:
    if "spam" in meal:
        for index in range(len(meal) -1, -1, -1):
            if meal[index] == "spam":
                del meal[index]
        print(meal)
    else:
        print(meal)


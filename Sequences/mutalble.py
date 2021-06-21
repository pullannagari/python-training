shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

a = b = c = d = e = f = g = another_list
print("adding cream")
b.append("cream")   # There are both methods and functions in python.
                    # Methods are functions that belongs to an object.
                    # append() in this case is applicable for all mutable sequence types
print(c)
print(d)
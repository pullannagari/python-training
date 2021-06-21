pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)   # sorted returns a new list
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)    # sorted returns a new list
print(sorted_numbers)
print(numbers)

# sorted is a built in function, while sort is a method of list type
# sorted always returns a new list, while sort will sort the list in place
# sort returns None while sorted returns the new sorted list

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key = str.casefold)  # Don't include the patanthesis when mentioning the key
print(missing_letter)
# python lets you rebind the names of varibles and functions, including the built in functions

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]
names.sort()
print(names)
names.sort(key=str.casefold)
print(names)


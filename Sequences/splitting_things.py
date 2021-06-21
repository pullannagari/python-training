panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()  #split returns a list, by default separator is space " "
print(words)

numbers = "9,223,372,036,854,775,807"
numbers_split = numbers.split(sep=",")
print(numbers_split)  # using a named parameter

for index in range(len(numbers_split)):
    numbers_split[index] = int(numbers_split[index])

print(numbers_split)

# solving by creating a new list
# int_num = []
# for num in numbers_split:
#     int_num.append(int(num))
# print(int_num)


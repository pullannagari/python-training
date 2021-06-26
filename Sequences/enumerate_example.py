# efficient in getting the indexes and values at the index
# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"):  # enumerate returns tuples
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
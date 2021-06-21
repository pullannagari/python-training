# strings are pythons sequence data types
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# Python supports negative indexing for strings, -1 indicates last character
print(parrot[-1])
print(parrot[-14])

print()
# mini challenge - negative index based we win
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
# SLICING - upto but not incuding
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])  # start value is optional if starts with
print(parrot[10:14])
print(parrot[10:])  # last value is optional if end with the end of the sequence

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

letters = " abcdefghijklmnopqrstuvwxyz"
for i in range(1, 28):
    print(letters[i - 1:i])

# slices can be used even with negative integers, but only from left to right
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])

# STEPPING
print(parrot[0:6:2])  # Nre - first slices the sequence and then steps in the order mentioned
print(parrot[0:6:3])  # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])

print(number[1::4])
separators = number[1::4]
print(separators)

separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators+char

print(separators)

values = "".join( char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))



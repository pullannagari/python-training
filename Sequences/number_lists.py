empty_list = []
even = [ 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# print(numbers)
#
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#
# digits = sorted("432985617")
# print(digits)  # prints a list of sorted strings
#
# unsorted_digits = list("432985617")
# print(unsorted_digits)
#
# more_numbers = list(numbers)    # used to copy the list - NOT RECOMMENDED
# more_numbers = numbers[:]   # slicing also produces new list and can be used to copy the list - NOT RECOMMENDED
# more_numbers = numbers.copy()   # recommended, introduced in 3.3
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)

numbers = [even, odd]
print(numbers)

for numbers_list in numbers:
    print(numbers_list)
    for number in numbers_list:
        print(number)
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("iss"))

# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)
# print(another_even)

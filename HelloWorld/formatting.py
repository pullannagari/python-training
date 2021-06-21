for i in range(1, 13):
    print("the number {0:<2} squared is {1:>3} and cubed is {2:^4}".format(i, i ** 2,
                                                                           i ** 3))  # number of spced to reserve and left aligned, right aligned and centered

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))  # defaults to 6 digits after the decimal
print("Pi is approximately {0:12.50f}".format(
    22 / 7))  # python determines precision is more important and prints 50 digits after decimal point
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(
    22 / 7))  # max precision for floating point numbers is between 51 and 53 digits
print("Pi is approximately {0:<72.50f}".format(22 / 7))

print()

for i in range(1, 13):
    print("the number {} squared is {:>3} and cubed is {:>4}".format(i, i ** 2,
                                                                     i ** 3))  # without fiels numbers takes the order in which the variables are mentioned. you cannot use values more than once

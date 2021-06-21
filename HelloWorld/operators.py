a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo, the remainder after integer division

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))

# BODMAS - BRACKETS, ORDER, DIVISION/MULTIPLICATION(SAME), ADDITION/SUBTRACTION(SAME). WHEN WE HAVE SAME PRIORITY THE ORDER IS LEFT TO RIGHT

print(a / (b * a) / b)

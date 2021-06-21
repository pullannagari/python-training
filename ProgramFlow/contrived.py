# con·trived
# /kənˈtrīvd/
# Learn to pronounce
# adjective
# deliberately created rather than arising naturally or spontaneously.

# FOR ELSE, else is activated if all the iterations are complete/there is no break

numbers = [1, 45, 132, 161, 610]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are fine")
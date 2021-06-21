for i in range(1,21): # range end value is upto but not including
    print("i is now {}".format(i))

print("~"*80)

for i in range(10): #start value defaults to 0
    print("i is now {}".format(i))

print("~"*80)

for i in range(0, 10, 2): #start index is mandatory if there is step value
    print("i is now {}".format(i))

for i in range(10, -1, -2): # 0 will not be printed
    print("i is now {}".format(i))
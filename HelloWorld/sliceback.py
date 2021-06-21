letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[
            25::-1]  # alphabets in the reverse order, we are not specifying the end since it would start at z and works it out till the start of the string since step is negative
print(backwards)
backwards = letters[
            ::-1]  # this is the same as above, since the step is negative it knows to starts from backwards and defaluts to end of the sequence
print(backwards)
backwards = letters[25:-27:-1]  # this is also the same
print(backwards)
# ::-1 is an idiom in python to obtain a reverse of the string
#  WHEN SLICING BACKWARDS ENSURE THAT THE START VALUE IS GREATER THAN THE STOP VALUE

# Challenge

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

last8chars = letters[:16:-1]
print(last8chars)

print(letters[-4:])  # prints the last 4 characters in the letters sequence

# more idioms
print(letters[-1:])  # prints the last character in the sequence
print(letters[
      :1])  # prints the first character in the sequence, useful when the sequence is empty since letter[0] crashes

# there are 5 sequence types in python
# string                : "hello", "world"
# list                  : ["computer", "monitor", "keyboard"]
# tuple
# range
# bytes and bytearray

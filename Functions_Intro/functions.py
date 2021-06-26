def multiply(x: float, y: float) -> float:  # function name follows the same rules as the variable names
    """
    multiply the two input parameters.
    although the function is intended for
    multiplying two numbers, you can also
    pass a string, for example and you'll
    get the string repeated

    :param x: operand for multiplication
    :param y: operand for multiplication
    :return: result of the multiplication
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Checks if the reverse of the string equals the string parameter

    :param string: parameter to check if it is a palindrome
    :return: boolean value based on whether input is a palindrome or not
    """
    string = palindrome_sentence(string).casefold()
    backwards = string[::-1]
    return backwards == string
    #     return True
    # return False
# leave 2 lines before and after the function definition


def palindrome_sentence(sentence: str) -> str:
    """
    Remove the characters which are not alpha-numeric from the parameter

    :param sentence: string which may contain
                     non-alpha numeric values
    :return: string containing only alpha-numeric values
    """
    trimmed_sentence = ""
    for char in sentence:
        if char.isalnum():
            trimmed_sentence += char
    return trimmed_sentence


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n` """
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


answer = multiply(10.5, 4)
# if the functions don't return value.
# None is assigned

print(answer)

forty_two = multiply(6, 7)
print(forty_two)

for val in range(1, 10):
    print("2 times {} is {}".format(val, multiply(2, val)))
    print(val, fibonacci(val))

str = "Do geee see god?"
print("{} is a {} Palindrome".format(str, is_palindrome(str)))


# using default parameters,
# the argument becomes
# optional at the caller
def banner_text(text: str = " ", screen_width: int = 60) -> None:
    """
    centers the text and prints with padded ** at the start and the end
    :param text: string to be centered and printed
    :param screen_width: width of the screen on which text should be printed
    :raises ValueError: if the supplies string is longer than screen width
    """
    if len(text) > screen_width - 4:
        raise ValueError("screen {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


width = 60
banner_text("*")
banner_text("lorem ipsum lorem ipsum")
banner_text("the quick brown fox jumped over lazy dog")
banner_text(screen_width=60)  # key word arguments are used when both
# arguments are optional
banner_text("lorem ipsum lorem ipsum", width)
banner_text("the quick brown fox jumped over the lazy dog", width)
banner_text("*", width)

# result = banner_text("Nothing is returned", width)  # returns None by default
# print(result)

# numbers = [ 1, 3, 5, 2, 6]
# print(numbers.sort())  # prints None since sort() returns None

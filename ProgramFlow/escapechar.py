split_string = "This string has been\nsplit over\nmultiple lines"
print(split_string)

tabbed_string = "This string has been\ttabbed\tmultiple\ttimes"
print(tabbed_string)

escape_char = "The pet shop owner said \"No, no, 'e 's uh,...he's resting\"."
escape_char_single = 'The pet shop owner said "No, no, \'e \'s uh,...he\'s resting".'
print(escape_char)
print(escape_char_single)

triple_quotes = """The pet shop owner said "No, no, 'e 's uh,...he's resting". """
print(triple_quotes)

split_multiple_lines = """This String
has been
split over
multiple lines"""
print(split_multiple_lines)

split_multiple_lines_escape = """This String\
has been\
split over\
multiple lines"""
print(split_multiple_lines_escape)

print("escaping the characters in path for ex c:\\documents\\notes\\here.xml")
print(r"escaping using raw c:\\documents\\notes\\here.xml")

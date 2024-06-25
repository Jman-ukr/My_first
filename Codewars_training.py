"""Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length )."""

# def solution(a, b):
#     return a+b+a if len(a) < len(b) else b+a+b

# ShortLongShort.solution("1", "22"); // returns "1221"

"""You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.
Write a program that returns the girl's age (0-9) as an integer.
Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". 
The first character in the string is always a number."""
# get_age("2 years old"), 2)
# def get_age(age):
#     return int(age[0])
# print(get_age("2 years old"))

"""Create a function that accepts a string and a single character, and returns an integer of the count of occurrences 
the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned."""
# V1
def str_count(strng, letter):
    if not strng:
        return 0
    counter = 0
    for char in strng:
        if char == letter:
            counter += 1
    return counter
print(str_count("Hello", 'o'))

# V2
def str_count(strng, letter):
    return strng.count(letter)
print(str_count("Hello", 'o'))

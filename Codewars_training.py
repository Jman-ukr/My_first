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
# def str_count(strng, letter):
#     if not strng:
#         return 0
#     counter = 0
#     for char in strng:
#         if char == letter:
#             counter += 1
#     return counter
# print(str_count("Hello", 'o'))

# V2
# def str_count(strng, letter):
#     return strng.count(letter)
# print(str_count("Hello", 'o'))

"""Create a combat function that takes the player's current health and the amount of damage recieved, 
and returns the player's new health. Health can't be less than 0."""

# V1
# def combat(health, damage):
#     result = health - damage
#     if result > 0:
#         return result
#     else:
#         return 0
# print(combat(83, 16))
# # V2
# def combat(health, damage):
#     return max(0, health-damage)
# print(combat(83, 16))

"""Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel."""
# V1
# def disemvowel(string_):
#     char_to_remome = "aoeiuAOEIU"
#     new_string = ""
#     for char in string_:
#         if char not in char_to_remome:
#             new_string += char
#     return new_string
# print(disemvowel("Ayy common way to deal with this situation is to remove all of the vowels"))
# V2
# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")
# print(disemvowel("Ayy common way to deal with this situation is to remove all of the vowels"))

"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number."""

# V1
def high_and_low(numbers):
    list_of_num = list(map(int, numbers.split())) # Розділяємо рядок на список чисел і конвертуємо кожен елемент у ціле число
    min_num = min(list_of_num)
    max_num = max(list_of_num)
    result = f'{max_num} {min_num}'
    return result

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# V2
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
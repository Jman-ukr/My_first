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
# def high_and_low(numbers):
#     list_of_num = list(map(int, numbers.split())) # Розділяємо рядок на список чисел і конвертуємо кожен елемент у ціле число
#     min_num = min(list_of_num)
#     max_num = max(list_of_num)
#     result = f'{max_num} {min_num}'
#     return result

# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# V2
# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"

# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

"""Напиши функцію, яка приймає список чисел і повертає їх суму."""
# def sum_of_list(numbers: list) ->int:
#     if not numbers:
#         return 0
#     result = sum(numbers)
#     return result
# print(sum_of_list([1, 2, 3, 4, 5]))

"""Напиши функцію, яка приймає рядок і повертає цей рядок у зворотному порядку."""
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("I love ChatGPT"))

"""Напиши функцію, яка приймає словник і повертає ключ з найбільшим значенням."""
# V1
# def max_value_key(d):
#     if not d:
#         return None
#     list_of_keys = []
#     for key in d.keys():
#         list_of_keys.append(key)
#     max_key = max(list_of_keys)
#     return max_key

# V2
# def max_value_key(d):
#     return max(d.keys(), default=None)
#
# # Приклад використання:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(max_value_key(my_dict))  # Виведе: 'c'

"""The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, 
i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'."""
# def dna_to_rna(dna):
#     return dna.replace("T", "U")

"""Write a function that given, an array arr, returns an array containing at each index i the amount of numbers 
that are smaller than arr[i] to the right."""

#V1
# def smaller(arr):
#
#     n = len(arr)
#     result = [0] * n  # Ініціалізуємо масив результатів нулями
#
#     # Зворотній прохід по масиву
#     for i in range(n - 2, -1, -1):
#         count = 0
#         # Перевіряємо елементи праворуч від поточного елемента
#         for j in range(i + 1, n):
#             if arr[j] < arr[i]:
#                 count += 1
#         # Оновлюємо результат для поточного елемента
#         result[i] = count
#
#     return result
# print(smaller([5, 4, 3, 2, 1]))

# V2

# def smaller(arr):
#     # Good Luck!
#     return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

"""Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list [3, 4, 3, 6] the function should return 10,
and for the list [1, 10, 3, 10, 10] the function should return 4."""
#V1
# def sum_no_duplicates(l):
#     count_dict = {}
#     for num in l:
#         count_dict[num] = count_dict.get(num, 0) + 1
#     result_list = [key for key, value in count_dict.items() if value == 1]
#     return sum(result_list)
#
# print(sum_no_duplicates([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1]))

#V2

# def sum_no_duplicates(l):
#     return sum(n for n in set(l) if l.count(n) == 1)

"""In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the 
"Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly 
one of the two expressions are true, false otherwise. For example:"""
# def xor(a,b):
#     if a == False and b == False:
#         return False
#     elif a == True and b == True:
#         return False
#     return True
# V2
# def xor(a,b):
#     return a != b
"""Make a function that returns the value multiplied by 50 and increased by 6. 
If the value entered is a string it should return "Error"."""
# def problem(a):
#     if isinstance(a, str):
#         return f"Error"
#     else:
#         return a * 50 + 6

# V2
# def problem(a):
#     return "Error" if isinstance(a,str) else a*50+6

"""Given a string, you have to return a string in which each character (case-sensitive) is repeated once."""
# def double_char(s):
#     list_s = list(s)
#     new_s = []
#     for char in list_s:
#         new_s.append(char)
#         new_s.append(char)
#     new_s_str = ''.join(new_s)
#     return new_s_str
# print(double_char("Hello World"))

# V2
# def double_char(s):
#     return ''.join(c * 2 for c in s)

# V3
# def double_char(s):
#     return ''.join(map(lambda e:e*2,s))





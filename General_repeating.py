'''About print function 1.6. pages from 25 to 27'''

# V1

# print('String 1', 'String 2', sep='|')
#
# for n in range(1, 5):
#     print(n, end=' ')
# print()
# print('New text')
#
# print("""String 1
# String 2
# String 3""")

# V2
# import sys
# sys.stdout.write('String 1\n')
# sys.stdout.write('String 2')

'''Input function'''

# name = input('Enter your name dude: ')
# print(f'Hello, {name}!!!')
# input('Put <Enter> for closing window')

# for i in 'String':
#     print(i, end=' ')
# print()
#
# d = {'x': 1, 'y': 2}
# for key in d:
#     print(key, end=' ')


'''Напишіть програму, яка буде приймати оцінку студента (від 0 до 100) і виводити відповідне повідомлення згідно з оцінкою за такими критеріями:
Відмінно: 90-100
Добре: 80-89
Задовільно: 70-79
Потребує вдосконалення: менше 70'''

# grade = int(input('Enter your current grade dude: '))
# if grade >= 90: print('Excellent')
# elif 90 > grade >= 80: print('Good')
# elif 80 > grade >= 70: print('Satisfactory')
# else:
#     print('Come on dude')


"""Loop for"""

# for s in 'str':
#     print(s, end=' ')
# else:
#     print('\nLoop completed')

# arr = {'x': 1, 'y': 2, 'z': 3}
# for key, value in arr.items():
#     print(key, value)
# for key in arr:
#     print(key, arr[key])

# arr = [(1, 2), (3, 4)]
# for a,b in arr:
#     print(a,b, sep='|')

"""Cycle for"""
# for s in 'str':
#     print(s, end='')
# else:
#     print('\nCycle is over')

#  Підрахунок суми елементів у списку:
# Створіть список чисел і використайте цикл for для обходу кожного елемента у списку. Використовуйте змінну для підрахунку суми всіх чисел у списку.

# list = range(1, 11)
# sum_of_numbers = 0
# for num in list:
#     sum_of_numbers += num
# print(sum_of_numbers)

# Виведення пари значень та їхніх індексів:
# Створіть список із стрічок. Використайте функцію enumerate, щоб отримати індекс кожного елемента разом із самим елементом. Потім виведіть кожну пару значень.

# list = ['I am a good python developer']
# words = list[0].split()
# split_text = []
# for char in words:
#     split_text += char
# for x in enumerate(split_text):
#     print(x)

# Створіть програму, яка генерує таблицю множення для заданого числа. Використовуйте цикл for та функцію range,
# щоб пройтися по всім числам від 1 до 10 та вивести їх добуток з заданим числом.

# arr = range(1, 11)
# number = int(input('Enter the number: '))
# result = []
# for num in arr:
#     print(f'{number} * {num} = {number * num}')

# Фільтрація списку за певною умовою:
# Створіть список чисел. Використайте цикл for та функцію range, щоб пройтися по кожному елементу списку. Виведіть лише ті числа, які діляться на 3 без остачі.

# list = [x for x in range(1, 101)]
# result = []
# for num in range(1, len(list)):
#     if list[num] % 3 == 0:
#         result.append(list[num])
# print(result)

"""Random module"""

# Генерація випадкового числа: Напишіть програму, яка генерує випадкове ціле число в діапазоні від 1 до 100 і виводить його на екран.

# import random
# random_number = random.randint(1, 100)
# print(f'Random_number is: {random_number}')

# Гра "Вгадай число": Напишіть просту гру, де комп'ютер загадує випадкове число від 1 до 10, а користувач повинен спробувати вгадати це число.

import random
# random_number = random.randint(1, 10)
# user_number = int(input('Enter random number from 1 to 10: '))
# if random_number == user_number:
#     print('You are good dude')
# else:
#     print('Dude, come on. Try again')
# input('Touch <Enter> to close this window')

# Перемішування списку: Напишіть програму, яка перемішує елементи списку.

# my_list = [x for x in range(1, 6)]
# random.shuffle(my_list)
# print(my_list)
#
# arr = 'string'
# print(random.choice(arr))
#
# print(random.sample(arr, 2))

#  Створіть програму генерації випадкових паролей з 8 символами. Всі англ букви та цифри

# import string
# import random
# def generator_password(count_char=8):
#     all_characters = string.ascii_letters + string.digits
#     arr = list(all_characters)
#     password = []
#     for _ in range(count_char):
#         password.append(random.choice(arr))
#     return "".join(password)
# print(generator_password())

"""Type of data string"""
# def test():
#     """This is the description of function"""
#     pass
# print(test.__doc__)

"""Using r, slash and n"""
# print("String1\nString2")
# print(r"String1\nString2")
# print(r"C:\Pyton\lib\package")
# print("C:\\Pyton\\lib\\package")
# print('This character \\ is not special')

"""Operations with strings"""

# arr = "Python"
# arr1 = "J" + arr[1:]
# arr2 = arr[:len(arr)-1]
# print(arr2)

# print("String1" "String2")
#
# arr = 'string' + str(10)
# print(arr)

# s = "word1 word2 word3"
# print(s.split())


# string = 'I am a good python developer'
# my_list = list(string)
# my_list = [char for char in my_list if char != ' ']   # Deleting spaces
# print(my_list)
#
# my_list = ['I am a good python developer']
# string_my_list = my_list[0]
# new_list = []
# for char in string_my_list:
#     if char != ' ':
#         new_list.append(char)
# print(new_list)

# words = ['apple', 'grapes', 'banana']
# counter = 0
# for word in words:
#     for char in word:
#         if char == 'p':
#             counter += 1
# print(counter)

"""Метод str.format() використовується для форматування рядків в Python. Він дозволяє вставляти значення змінних у рядок 
та налаштовувати їх відображення. Ось декілька прикладів застосування str.format():"""

# Вставка значень без форматування:
# name = "John"
# age = 30
# print("Hello, my name is {} and I am {} years old.".format(name, age))
# Встановлення порядкового номера для вставки значень:
#
# print("My name is {0} and I am {1} years old.".format(name, age))
# Використання іменованих аргументів:
#
# print("My name is {name} and I am {age} years old.".format(name="Alice", age=25))
# Форматування чисел:
#
# pi = 3.14159
# print("The value of pi is {:.2f}.".format(pi))
# Вставка змінних у специфічному порядку:
#
# print("{1} is the capital of {0}.".format("France", "Paris"))
# Використання вкладених функцій та виразів:
#
# name = "John"
# print("Hello, my name is {} and I am {} years old.".format(name.upper(), 30 * 2))
# За допомогою методу str.format() можна вставляти значення змінних у рядок у багатоформатному вигляді, що робить його
# корисним для будь-яких ситуацій, коли потрібно динамічно створювати рядки з різними значеннями.

"""Метод strip() використовується для видалення пробілів та інших символів пропуску з початку та кінця рядка. Ось як працює цей метод:"""

# Видалення пробілів з початку та кінця рядка:
# text = "   Hello, world!   "
# print(text.strip())  # Output: "Hello, world!"

# Видалення вказаних символів з початку та кінця рядка:
# text = "...Hello, world!..."
# print(text.strip("."))  # Output: "Hello, world!"

# Видалення пробілів з початку рядка:
# text = "   Hello, world!   "
# print(text.lstrip())  # Output: "Hello, world!   "

# Видалення пробілів з кінця рядка:
# text = "   Hello, world!   "
# print(text.rstrip())  # Output: "   Hello, world!"

# Метод strip() повертає новий рядок, у якому видалені пробіли та інші символи пропуску з початку та кінця вихідного рядка.
# Це дозволяє легко очищати рядки від зайвих пробілів або інших символів, що можуть виникати після операцій з рядками.

"""Метод .count для підрахунку клькості входжень у рядок"""

# def str_count(strng, letter):
#     return strng.count(letter)
# print(str_count("Hello", 'o'))

"""Tasks from Mate academy"""

# Напиши функцію get_string_length, яка приймає рядок string і повертає його довжину (кількість символів у ньому).
# def get_string_length(string: str):
#     return len(string)
# print(get_string_length('Abracadabra'))

# Наш новий бос, як виявилося, просто ненавидить голосні літери, тому нам потрібно прибрати їх з усієї документації 🤔
# Напиши функцію remove_vowels, яка приймає рядок document і повертає новий рядок, де всі голосні видалені.
# Зверни увагу: голосними літерами є aeiouy у будь-якому регістрі.
# def remove_vowels(document: str) -> str:
#     vowels = 'aeiouy'
#     new_document = ''
#     for char in document.lower():
#         if char not in vowels:
#             new_document += char
#     return new_document
# print(remove_vowels("captain"))

# У цьому завданні створи функцію make_abbr, яка приймає рядок зі слів words та повертає абревіатуру з них у верхньому регістрі.
# Рядок words містить одне або декілька слів, розділених пробілом. А якщо words не містить жодного символу — поверни пустий рядок.
# def make_abbr(words: str) -> str:
#     if not words:
#         return ''
#     abbr = words[0]
#     for char in range(1, len(words)):
#         if words[char] == ' ':
#             abbr += words[char + 1]
#     return abbr.upper()
# print(make_abbr("national aeronautics space administration"))

# Створи функцію decrypt_message, яка приймає рядок message та повертає новий рядок, де символи з message розташовані у зворотному порядку.

# V1
# def decrypt_message(message: str) -> str:
#     return message[::-1]
# V2
# def decrypt_message(message: str) -> str:
#     return ''.join(reversed(message))
# print(decrypt_message("!!!reeb gniknird ekil eW"))

# V3
# def decrypt_message(message: str) -> str:
#     reversed_message = ''
#     for char in range(len(message) -1, -1, -1):
#         reversed_message += message[char]
#     return reversed_message
# print(decrypt_message("!!!reeb gniknird ekil eW"))

# V4
# def decrypt_message(message: str) -> str:
#     list_message = list(message)
#     list_message.reverse()
#     new_reversed_str_message = ''.join(list_message)
#     return new_reversed_str_message
# print(decrypt_message("!!!reeb gniknird ekil eW"))

# V5
# def decrypt_message(message: str) -> str:
#     reversed_message = ''
#     for char in message:
#         reversed_message = char + reversed_message
#     return reversed_message
# print(decrypt_message("!!!reeb gniknird ekil eW"))

"""Створи функцію is_werewolf, яка приймає рядок target і повертає True, якщо це перевертень, або False — якщо ні."""

# V1
# def is_werewolf (target: str) -> bool:
#     new_target = ''.join(char for char in target if char.isalpha())
#     return new_target.lower() == new_target.lower()[::-1]
# print(is_werewolf("eva, can i see bees in a cave"))
#
# # V2
# import re
# def is_werewolf (target: str) -> bool:
#     new_target = re.sub(r'[ ,.?]', '', target.lower())
#     return new_target == new_target[::-1]
# print(is_werewolf("eva, can i see bees in a cave"))

# Sum of numbers

# sum = 0
# while True:
#     num = input('Enter number: ')
#     if num == 'stop':
#         break
#     if num == '':
#         print('Dude you didn`t enter the number')
#         continue
#     if num[0] == '-':
#         if not num[1:].isdigit():
#             print('Dude you have to enter the number, not str')
#             continue
#     else:
#         if not num.isdigit():
#             print('Dude you have to enter the number, not str')
#             continue
#     num = int(num)
#     sum += num
# print(f"Sum of numbers is: {sum}")
# input()

"""Модуль string в Python надає корисні константи та функції для роботи з рядками. Давай розглянемо основні можливості 
цього модуля та його застосування."""

"""Основні константи модуля string
string.ascii_letters: Всі літери латинського алфавіту (великі та малі)."""
# import string
# print(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

"""string.ascii_lowercase: Малі літери латинського алфавіту."""
# print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'

"""string.ascii_uppercase: Великі літери латинського алфавіту."""
# print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

"""string.digits: Цифри від 0 до 9."""
# print(string.digits)  # '0123456789'

"""string.punctuation: Всі знаки пунктуації."""
# print(string.punctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

"""string.whitespace: Всі символи пробільних знаків (пробіл, табуляція, новий рядок тощо)."""
# print(repr(string.whitespace))  # ' \t\n\r\x0b\x0c'

"""Функція str.maketrans і метод str.translate"""
"""Функція str.maketrans створює таблицю перекладу, яка використовується методом str.translate для заміни 
або видалення символів у рядку."""
# Приклад використання str.maketrans та str.translate
# import string

# text = "This is a simple text example. This example is meant to be simple, so we can analyze it easily. Let's see how many times each word appears in this text."

# Створення таблиці перекладу для видалення пунктуації
# translation_table = str.maketrans('', '', string.punctuation)

# Застосування таблиці перекладу для видалення пунктуації та приведення тексту до нижнього регістру
# clean_text = text.translate(translation_table).lower()

# print(clean_text)

"""Bytes datatype"""
"""bytes - це не змінний (immutable) тип даних в Python, який представляє собою послідовність байтів. Кожен байт може 
приймати значення від 0 до 255. Об'єкти типу bytes використовуються для представлення байтових даних, таких як текст 
у кодуванні ASCII, бінарні дані, зображення, аудіо та інші формати файлів."""

# data1 = b'Hello'
# length = len(data1)
# print(length)
#
# data2 = bytes([104, 101, 108, 108, 111])
#
# data3 = 'hello'.encode('utf-8')

"""Regular expressions"""

"""Регулярні вирази в програмуванні" - це спеціальні образці символів, які використовуються для пошуку та виконання 
операцій з текстовими даними. Вони дозволяють шукати певні шаблони у тексті, виконувати заміни та витягувати певні 
частини тексту відповідно до заданих правил."""

"""Під час компіляції регулярний вираз перетворюється в деяку внутрішню структуру даних, яка дозволяє виконувати 
операції з текстом ефективно. Ця внутрішня структура може бути оптимізована для швидкого виконання пошуку та інших операцій."""


   # \b вказує на межу слова.
   # \w* відповідає будь-якій послідовності букв або цифр, яка може бути нульовою або більшою.
   # [^.]* відповідає будь-якій послідовності символів, які не містять крапку. Метасимвол ^ у квадратних дужках означає "все, крім"
   # \. відповідає крапці, яка закінчує речення.
   # ^ у регулярних виразах позначає початок рядка. Якщо використовувати його всередині виразу, то він буде відповідати початку
   # кожного рядка, а не початку речення.
   # $ вказує на кінець рядка.
   # . відповідає будь-якому символу (включаючи пробіли), який повторюється нуль або більше разів
   # [A-Z] всі великі літери
   # [a-z] всі малі літери
   # [0-9] всі цифри
   # [] Квадратні дужки визначають набір символів. Наприклад, [abc] відповідає будь-якому символу з набору a, b або c.
   # () Круглі дужки використовуються для групування патернів. Вони також використовуються для захоплення підвиразів для подальшого використання.
   # Все, що знаходиться всередині круглих дужок, розглядається як один елемент. pattern = re.compile(r'Hello, (world)!')
   # \ Використовується для вказання спеціальних послідовностей або для уникнення інтерпретації спеціальних символів.
   # \\ відповідає літері \
   # | Використовується для вказання альтернативи між двома патернами. Наприклад, cat|dog знайде або "cat", або "dog".
   # * Квантифікатор * вказує на нуль або більше повторень попереднього елементу. Наприклад, a* відповідає будь-якій кількості символів a, включаючи нуль a.
   # + Квантифікатор + вказує на одне або більше повторень попереднього елементу. Наприклад, a+ відповідає одному або більше символу a, але не нуль.
   # ? Квантифікатор ? вказує на нуль або одне повторення попереднього елементу. Цей квантифікатор робить попередній елемент необов'язковим. Наприклад, colou?r відповідає як "color", так і "colour".
   # \w відповідає будь-якій букві чи цифрі.
   # \d відповідає будь-якій цифрі.
   # \s відповідає будь-якому пробільному символу (пробіл, табуляція, переведення каретки тощо).
   # \W відповідає будь-якому символу, який не є буквою чи цифрою.
   # \D відповідає будь-якому символу, який не є цифрою.
   # \S відповідає будь-якому символу, який не є пробільним символом.
   # {} використовується для вказання кількості повторень попереднього елемента або групи.
   # {n}: Відповідає рівно n повторенням попереднього елемента. Наприклад, \d{3} відповідає будь-якій послідовності з трьох цифр.
   # {n,}: Відповідає принаймні n повторенням попереднього елемента. Наприклад, \w{3,} відповідає будь-якому слову, яке має принаймні три букви.
   # {n,m}: Відповідає від n до m повторень попереднього елемента. Наприклад, [a-z]{2,4} відповідає будь-якому слову, яке містить від двох до чотирьох малих літер латинського алфавіту.
   # re.IGNORECASE або re.I:Ігнорує регістр символів під час пошуку.
   # re.MULTILINE або re.M: Зробить спеціальні символи ^ і $ відповідними початку та кінцю кожного рядка, а не всього рядка тексту.
   # re.DOTALL або re.S: Дозволяє символу . включати в себе символ нового рядка (\n), що допомагає шукати збіги у тексті, який містить переведення рядка.
   # re.VERBOSE або re.X: Дозволяє додавати коментарі до регулярних виразів, що полегшує їх читання та розуміння.
   # re.UNICODE або re.U: Дозволяє використовувати кодування Unicode у регулярних виразах.
   # re.ASCII: Змушує інтерпретувати \w, \W, \b, \B, \d, \D, \s, \S як ASCII символи.
   # re.DEBUG: Виводить відладочну інформацію про скомпільований регулярний вираз.
   # *? Збігається з нульовою або більшою кількістю попереднього елемента, найменша можлива кількість.
# Наприклад, вираз a*? збігається з нульовою або більшою кількістю символів "a", найменша можлива кількість.
   # +? Збігається з одним або більше попереднього елемента, найменша можлива кількість.
# Наприклад, вираз a+? збігається з одним або більше символом "a", найменша можлива кількість.
   # ?? Збігається з нульовою або одним попереднім елементом, перший, який знайдено.
# Наприклад, вираз a?? збігається з нульовим або одним символом "a", першим, який знайдено.
   # {n,m}? Збігається з n до m попередніх елементів, найменша можлива кількість.
# Наприклад, вираз a{2,4}? збігається з двома до чотирьох символами "a", найменша можлива кількість.

   #Позитивний перегляд (Positive Lookahead):
   #Позитивний перегляд відбувається, коли певний патерн слідує за певним текстом, але цей патерн не входить у збіг.
   #Синтаксис: (?=pattern)
   #Наприклад, вираз \w+(?=\d) збігається з будь-яким словом, яке слідує за цифрою.
   # (?=pattern) позитивний перегляд вперед
   # (?<=pattern) позитивний перегляд назад

   #Від'ємний перегляд (Negative Lookahead):
   #Від'ємний перегляд відбувається, коли певний патерн НЕ слідує за певним текстом.
   #Синтаксис: (?!pattern)
   #Наприклад, вираз \w+(?!\d) збігається з будь-яким словом, яке НЕ слідує за цифрою.
   # (?!pattern) негативний перегляд вперед
   # (?<!pattern) негативний перегляд назад



import re
# text = """Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and
# first released in 1991. Python features a dynamic type system and automatic memory management and supports multiple
# programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a
# large and comprehensive standard library. Evgenrevin@gmail.ru
# Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open
# source software and has a community-based development model, as do nearly all of Python's other implementations. Python
# and CPython are managed by the non-pr0fit Python Software Foundation.
# As of January 2022, Python ranks as one of the top programming languages according to multiple indices. Python is often
# praised for its readability and simplicity, and is commonly used in web development, data science, artificial intelligence,
# machine learning, automation, scripting, and more."""
# pattern = re.compile(r'more', re.IGNORECASE) # Ignore register, dot . is any symbol
' Знайдіть всі входження слова "Python" і підрахуйте кількість входжень'
# pattern = re.compile(r'Python')
# matches = pattern.findall(text)
# print(matches)
# print(len(matches))
#
'  Знайдіть всі входження слова, яке починається з літери "p" (або "P").'
# pattern = re.compile(r'\bp\w*\b', re.I)
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі речення, які закінчуються символом крапки.'
# pattern = re.compile(r'[^.]*\.$', re.MULTILINE) # [^.]* відповідає будь-якій послідовності символів, які не містять крапку.
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі речення, які починаються зі слова "Python"'
# pattern = re.compile(r'\bPython[^.]*\.', re.MULTILINE) # \. відповідає крапці, яка закінчує речення.
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі слова, які містять цифри.'
# pattern = re.compile(r'\b\w*\d\w*\b')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі слова, які починаються "y" і закінчуються літерою "d"'
# pattern = re.compile(r'\bu\w*d\b')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі слова, які починаються з великої літери.'
# pattern = re.compile(r'[A-Z]\w*\b')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі слова, які складаються лише з літер (без цифр або символів).'
# pattern = re.compile(r'\b[a-zA-Z]+\b')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі числа у тексті.'
# pattern = re.compile(r'\d')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі слова, які закінчуються на літеру "s".'
# pattern = re.compile(r'\b\w*s\b')
# matches = pattern.findall(text)
# print(matches)
#
' Знайдіть всі адреси електронної пошти у тексті.'
# pattern = re.compile(r'\b[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
# matches = pattern.findall(text)
# print(matches)
# pattern = re.compile(r'\b\w{3}\b')
# matches = pattern.findall(text)
# print(matches)
' Знайдіть всі числа, які складаються з трьох цифр у тексті.'
# pattern = re.compile(r'\b\d{4}\b')
# matches = pattern.findall(text)
# print(matches)
' Знайдіть всі слова, які містять від 4 до 6 символів у тексті.'
# pattern = re.compile(r'\b\w{4,6}\b')
# matches = pattern.findall(text)
# print(matches)
' Знайдіть всі слова, які починаються з великої літери у тексті.'
# pattern = re.compile(r'\b[A-Z]+\w*\b')
# matches = pattern.findall(text)
# print(matches)
#
""" Method finditer() в модулі регулярних виразів Python (re) є корисним інструментом для пошуку всіх входжень певного
# патерну у тексті. Він подібний до методу findall(), але замість повернення списку збігів він повертає ітератор, який
# можна ітерувати, щоб отримувати кожний збіг окремо."""
# pattern = re.compile(r'\b[A-Z]\w*\b')
# matches_iter = pattern.finditer(text)
# for match in matches_iter:
#     print("Match:", match.group())
#     print("Position:", match.start(), '-', match.end())
#
' Знайдіть всі слова, які мають за собою крапку, але не включають крапку в результат.'
# pattern = re.compile(r'\b\w+(?=\.)\b')
# matches = pattern.findall(text)
# print(matches)
' Пошук кількості входжень слова "language", якщо воно слідує за словом "programming".'
# pattern = re.compile(r'(?<=programming\s)language', re.I)
# matches_iter = pattern.finditer(text)
# for match in matches_iter:
#     print("Match:", match.group())
#     print("Position:", match.start(), '-', match.end())
' Знайдіть всі слова, які не містять цифри.'
# pattern = re.compile(r'\w+(?!\d)')
# matches = pattern.findall(text)
# print(matches)

" Пошук всіх слів, які не містять букву 'o', але можуть містити будь-які інші символи."
# pattern = re.compile(r'\b(?!\w*o)\w+\b', re.I)
# matches = pattern.findall(text)
# print(matches)
"""Метод match() пошук першого елементу згідно шаблону тільки на початку рядка (перше слово), повертає match object"""
# pattern = re.compile(r'\b\w{5}\b')
# match = pattern.match(text)
# if match:
#     print(match.group())
# else:
#     print('Not found')
"""Метод search() пошук першого збігу з шаблоном """
# pattern = re.compile(r'\b\w{5}\b')
# match = pattern.search(text)
# if match:
#     print("Found match:", match.group())
# else:
#     print("Not found")
"""Метод fullmatch() в модулі re в Python використовується для перевірки того, чи повністю відповідає весь рядок заданому шаблону."""
# import re
# text1 = "Hello, world!"
# pattern = re.compile(r'Hello, world!')  # Шаблон, який відповідає тексту "Hello, world!"
# match = pattern.fullmatch(text1)
# if match:
#     print("Рядок повністю відповідає шаблону.")
# else:
#     print("Рядок не відповідає шаблону.")

"""Об'єкт Match є об'єктом, який повертається методами match() і search() з модуля re в Python, якщо вони знаходять 
збіг з регулярним виразом у тексті. Цей об'єкт містить інформацію про знайдений збіг, таку як зіставлене значення, 
позицію у тексті і т. д."""

# Ось основні атрибути об'єкта Match:

# group(): Повертає фактичне значення, яке збіглося з регулярним виразом.
# start(): Повертає позицію початку збігу у тексті.
# end(): Повертає позицію кінця збігу у тексті.
# span(): Повертає кортеж (start, end), який містить позиції початку і кінця збігу.

# import re
#
# text = "Hello, world!"
#
# pattern = re.compile(r'Hello, (\w+)!')
# match = pattern.search(text)
#
# if match:
#     print("Знайдено збіг:", match.group())  # Виводиться збігова частина тексту: "Hello, world!"
#     print("Початок збігу:", match.start())   # Виводиться позиція початку збігу: 0
#     print("Кінець збігу:", match.end())     # Виводиться позиція кінця збігу: 13
#     print("Позиції збігу:", match.span())   # Виводиться кортеж з позиціями початку і кінця збігу: (0, 13)
""""""

"""Метод sub() для знаходження та заміни. Якщо співпадінь не знайдено - повернеться початковий текст
   Метод можливо використовувати як функцію, без модуля re"""
# Замініть всі слова, які починаються на букву "a"

# import re
# text = "apple banana orange, apple banana orange, apple banana orange"
# new_text = re.sub(r'\b[aA]\w+\b','Musya', text)
# print(new_text)

"""Метод subn() замінює всі входження плюс повертає кількість зроблених замін"""

# У цьому прикладі ми шукаємо слово "apple" (ігноруючи регістр) і замінюємо його на "banana". Після цього ми виводимо новий текст та кількість здійснених замін.

# import re
#
# text = "Apple and orange are fruits. I like apples."
# new_text, num_replacements = re.subn(r'\bapple\b', 'banana', text, flags=re.IGNORECASE)
#
# print("New Text:", new_text)
# print("Number of Replacements:", num_replacements)
"""Метод split() використовується для розділення рядка на підрядки за певним роздільником і повертає список підрядків."""
#  Приклад 1: Розділення рядка за пробілами
# text = "Python is a programming language"
# words = text.split()
# print(words)
# # Вивід: ['Python', 'is', 'a', 'programming', 'language']

"""Функція escape() зазвичай використовується для екранування спеціальних символів у рядках, щоб їх можна було використовувати 
як частину регулярних виразів."""
# import re
#
# # Приклад рядка, який містить спеціальні символи
# text = "Escape special characters: ^$.*+?()[]{}|\\"
#
# # Екранування спеціальних символів у тексті
# escaped_text = re.escape(text)
#
# print("Original text:", text)
# print("Escaped text:", escaped_text)

"""Функція purge() проводить чистку кеша, результат не повертає"""
# re.purge()

"""Списки List"""
# Створення списку
# a = list()

"""Зрізи в списках"""
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""Список, що містить перші п'ять елементів."""
# my_list1 = my_list[:5]
"""Список, що містить останні п'ять елементів."""
# my_list2 = my_list[-1:-6:-1]
"""Список, що містить парні числа."""
# my_list3 = my_list[1::2]
"""Список, що містить непарні числа."""
# my_list4 = my_list[::2]
"""Список, що містить кожен третій елемент, починаючи з першого."""
# my_list5 = my_list[2::3]

"""Метод sort() сортує список на місці, тобто змінює оригінальний список. Він не повертає новий список, а просто змінює 
порядок елементів у вже існуючому."""
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort()  # Сортує список у порядку зростання
# print(my_list)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

"""Функція sorted() повертає новий відсортований список, залишаючи оригінальний список незмінним."""
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted_list = sorted(my_list)  # Повертає новий відсортований список
# print(sorted_list)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
# print(my_list)  # Оригінальний список залишається незмінним [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
"""Обидва методи, sort() і sorted(), приймають аргумент reverse, який дозволяє сортувати список у зворотному порядку."""
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# my_list.sort(reverse=True)  # Сортує список у зворотному порядку
# print(my_list)  # [9, 6, 5, 5, 5, 4, 3]

"""Сортування списку словників"""
# my_list = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Jane', 'age': 30},
#     {'name': 'Dave', 'age': 20}
# ]
#
# # Сортування за ключем 'age'
# my_list.sort(key=lambda x: x['age'])
# print(my_list)
# [{'name': 'Dave', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]

"""Використання operator модуля
Модуль operator надає зручні функції для сортування списків словників."""
# from operator import itemgetter
#
# my_list = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Jane', 'age': 30},
#     {'name': 'Dave', 'age': 20}
# ]
#
# # Сортування за ключем 'age'
# my_list.sort(key=itemgetter('age'))
# print(my_list)


# nested_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # вкладені списки
# nested_list2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
# arr = []
# for i in range(2):
#     arr.append([]) # створення вкладеного списку за допомогою методу append() всередині циклу
# print(arr)

"""Вкладені списки - це колекція списків, де кожен елемент головного списку також є списком. 
Це дає нам можливість створювати багатовимірні структури даних, які можуть представляти складні дані."""
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# У цьому прикладі nested_list - це вкладений список, який містить три підсписки. Кожен підсписок представляє рядок чисел.

# Ми можемо отримати доступ до елементів вкладеного списку, використовуючи індексацію:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[0])       # Виведе: [1, 2, 3]
# print(nested_list[1][2])    # Виведе: 6

# Ітерація через вкладений список виглядає так:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for sublist in nested_list:
#     for item in sublist:
#         print(item)

# Додавання елементів:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested_list.append([10, 11, 12]) # Додати новий підсписок
# nested_list[0].append(4) # Додати елемент до підсписку
# print(nested_list)

# Вилучення елементів:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# del nested_list[1] # Вилучення підсписку
# nested_list[0].remove(2) # Вилучення елемента з підсписку
# print(nested_list)

# Зміна значень:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested_list[1][1] = 10 # Зміна значення елемента
# print(nested_list)

"""Напишіть функцію, яка приймає на вхід вкладений список та елемент, і повертає True, якщо елемент знайдено у 
вкладеному списку, або False, якщо його немає."""
# def find_match(nested_list: list, element_to_find) -> bool:
#     if not nested_list or not element_to_find:
#         return False
#     for sublist in nested_list:
#         if element_to_find in sublist:
#             return True
#     return False
#
#
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# element_to_find = 5
# print(find_match(nested_list, element_to_find))

"""Обертання вкладеного списку: Напишіть функцію, яка обертає вкладений список, тобто перетворює його так, 
щоб рядки стали стовпцями, а стовпці - рядками."""

# def reverse_nested_list(nested_list: list) -> list:
#     if not nested_list:
#         return []
#     num_rows = len(nested_list) # нові рядки
#     num_cols = len(nested_list[0]) # нові стовпчики
#     result_list = []
#     for col in range(num_rows):
#         new_row = []  # Для кожного стовпця ми створюємо новий порожній список new_row, в який будемо додавати елементи з вихідного списку.
#         for row in range(num_cols):
#             new_row.append(nested_list[row][col]) # row - поточний рядок, а col - поточний стовпець.
#         result_list.append(new_row)
#
#     return result_list
#
#
# nested_list = [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]
# print(reverse_nested_list(nested_list))

"""Обчислення діагоналі матриці: Напишіть функцію, яка приймає на вхід квадратну матрицю (вкладений список списків) і 
обчислює суму її діагональних елементів."""
# def sum_diagonal_matrix(nested_list: list) -> int:
#     if not nested_list:
#         return 0
#     num_rows = len(nested_list)
#
#     for row in nested_list:  # Перевірка чи матриця квадратна
#         if len(row) != num_rows:
#             raise ValueError("The matrix is not rectangle")
#
#     result = 0
#     for i in range(num_rows):
#         result += nested_list[i][i]  # Додаємо елементи головної діагоналі
#
#     return result
#
# nested_list = [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]
# print(sum_diagonal_matrix(nested_list))


"""Напишіть функцію, яка приймає на вхід вкладений список чисел і повертає суму всіх елементів у цьому списку."""
# def sum_of_all_elements(nested_list: list):
#     if not nested_list:
#         return 0
#     result = 0
#     for row in nested_list:
#         result += sum(row)
#     return result
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(sum_of_all_elements(nested_list))

"""Напишіть функцію, яка приймає на вхід матрицю (вкладений список списків) і перевіряє, чи є вона квадратною (тобто кількість рядків дорівнює кількості стовпців)."""
# def is_matrix_rectangle(nested_list: list):
#     num_cows = len(nested_list)
#     for num in nested_list:
#         if len(num) != num_cows:
#             return False
#     return True
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# print(is_matrix_rectangle(nested_list))

"""Напишіть функцію, яка додає дві матриці разом. Матриці можуть бути представлені як вкладені списки, де кожен 
внутрішній список відповідає рядку матриці."""

# def sum_of_matrix(matrix1: list, matrix2: list) -> list:
#     if not matrix1 or not matrix2:
#         return []
#     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
#         return []
#     rows = len(matrix1)
#     cols = len(matrix1[0])
#     result_matrix = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result_matrix.append(row)
#     return result_matrix
#
#
# nested_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested_list2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# print(sum_of_matrix(nested_list1, nested_list2))

# my_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']
# last_two_elements = my_list[-2:]
# print(last_two_elements)
"""Список, що містить друге та четверте слово, перевернуті."""
# new_list = []
# for char in range(len(my_list)):
#     if char == 1 or char == 3:
#         new_list.append(my_list[char][::-1])
# print(new_list)

"""Список, що містить лише перші дві букви кожного слова."""
# Лох варіант
# word1 = [my_list[0][:2:]]
# word2 = [my_list[1][:2:]]
# word3 = [my_list[2][:2:]]
# word4 = [my_list[3][:2:]]
# word5 = [my_list[4][:2:]]
# new_list = word1 + word2 + word3 + word4 + word5
# print(new_list)

# Профі варіант V1
# new_list = [word[:2] for word in my_list]
# print(new_list)
# Профі варіант V2
# def get_first_two_chars(word):
#     return word[:2]
#
# my_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']
# new_list = list(map(get_first_two_chars, my_list))
# print(new_list)  # Виводить ['ap', 'ba', 'or', 'gr', 'st']

# варіант з вводом кількості символів від користувача
# def get_manual_chars(num_chars):
#     def inner_get_chars(word):
#         return word[:num_chars]
#     return inner_get_chars
#
# num_chars = int(input("Write how many letters do you want to get: "))
# my_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']
# new_list = list(map(get_manual_chars(num_chars), my_list))
# print(new_list)

"""Напиши функцію make_stickers, яка приймає кількість деталей details_count і назву частини робота robot_part. 
Функція має повертати список рядків у форматі "{robot_part} detail #{n}", де n - номер деталі по порядку.
Приклади:
make_stickers(3, "Body")  # ["Body detail #1", "Body detail #2", "Body detail #3"]
make_stickers(4, "Head")  # ["Head detail #1", "Head detail #2", "Head detail #3", "Head detail #4"]
make_stickers(0, "Foot")  # []"""
# def make_stickers(details_count:int, robot_part:str) -> list:
#     if details_count <= 0:
#         return []
#     result = []
#     for n in range(details_count):
#         result.append(f'{robot_part} detail #{n+1}')
#     return result
# print(make_stickers(4, "Head"))

"""Напиши функцію double_power, яка приймає список потужностей current_powers та повертає список із подвоєними значеннями."""
# def double_power(current_powers: list) ->list:
#     if not current_powers:
#         return []
#     return [i * 2 for i in current_powers]
# print(double_power([2, 2, 3]))
"""Напиши функцію is_sorted, яка отримує список чисел box_numbers і повертає True, якщо всі числа розташовані в порядку зростання, або False — якщо ні.
Зверни увагу: числа в списку можуть повторюватися.
Наприклад:
is_sorted([1, 2, 3, 4, 5])  # True
is_sorted([0, 1, 1, 1, 2])  # True
is_sorted([1, 2, 11])  # True
is_sorted([5])  # True
is_sorted([])  # True
is_sorted([0, 3, 1, 2, 2, 2])  # False
is_sorted([1, 11, 2])  # False"""
# def is_sorted(box_numbers: list) ->bool:
#     if not box_numbers:
#         return False
#     if len(box_numbers) == 1:
#         return True
#     for num in range(len(box_numbers) -1):
#         if box_numbers[num] > box_numbers[num + 1]:
#             return False
#     return True
# print(is_sorted([0, 3, 1, 2, 2, 2]))

"""List generators  [], expression generators  ()  """

# arr = [1, 2, 3, 4]
# arr = [i * 2 for i in arr]
# print(arr)

"""Основна відмінність полягає у тому, що генератор списку повертає новий список, тоді як вираз-генератор створює 
ітеруємий об'єкт, відомий як "генератор". Генератор списку зберігає всі значення в пам'яті, тоді як вираз-генератор 
створює значення на льоту при ітерації, що дозволяє економити пам'ять, особливо для великих обсягів даних."""

"""Напиши генератор списку, який містить квадрати чисел від 1 до 10."""
# arr = [i * 2 for i in range(1, 11)]

""" Вираз-генератор (generator expression) у Python дозволяє створювати генератори, які є ітеруємими об'єктами, 
що генерують елементи на льоту, один за іншим, без зберігання їх у пам'яті. Це робить їх дуже ефективними з точки зору 
використання пам'яті, особливо при роботі з великими обсягами даних."""

# (expression for item in iterable if condition) повертає ітератор
# arr = [1, 2, 3, 4]
# arr = [i * 10 for i in arr if i % 2 == 0]
# print(arr)

"""Builtin functions"""

"""map() function"""
"""Функція map() в Python застосовує задану функцію до всіх елементів вказаної послідовності (або кількох послідовностей) 
і повертає ітератор з результатами. Це дозволяє легко виконувати операції над всіма елементами списку або іншого 
ітерованого об'єкта без використання явних циклів."""
# def square(x):
#     return x ** 2
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))
#
# numbers1 = [1, 2, 3, 4]
# numbers2 = [10, 20, 30, 40]
# summed_numbers = map(lambda  x, y: x + y, numbers1, numbers2)
# print(list(summed_numbers))

"""zip() function"""
"""Функція zip приймає на вхід ітерабельні об'єкти та об'єднує їх в кортежі"""
# Три списки
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [0.1, 0.2, 0.3]
# Використання zip для поєднання елементів
# zipped = zip(list1, list2, list3)
# Перетворення результату на список
# zipped_list = list(zipped)
# print(zipped_list)
# Виведе: [(1, 'a', 0.1), (2, 'b', 0.2), (3, 'c', 0.3)]
"""Перетворення назад:"""
# Зіпований список
# zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# Розпакування
# unzipped_list1, unzipped_list2 = zip(*zipped_list)
# print(unzipped_list1)
# Виведе: (1, 2, 3)
# print(unzipped_list2)
# Виведе: ('a', 'b', 'c')

"""filter() function"""
"""Функція filter() в Python використовується для створення ітератора, який містить тільки ті елементи з ітерабельного 
об'єкта, для яких задана функція повертає значення True. Читабельність: Код стає простішим та читабельнішим.
Ефективність: filter() створює ітератор, що може бути більш ефективним при обробці великих обсягів даних, оскільки елементи обробляються "на льоту"."""
# def is_even(x):
#     return x % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(is_even, numbers)
# even_numbers_list = list(even_numbers)
# print(even_numbers_list)

"""Основна відмінність між append() і extend() полягає в тому, що append() додає один елемент до списку, тоді як extend() 
додає всі елементи іншого списку (або будь-якого іншого ітерабельного об'єкта) до кінця поточного списку."""

"""list.insert(index, element)"""
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 'X')
# print(my_list)  # Виведе: [1, 2, 'X', 3, 4, 5]

"""element = list.pop(index); index (необов'язковий): Індекс елемента, який потрібно видалити зі списку. 
Якщо index не вказаний, видаляється останній елемент списку.
element: Значення елемента, який був видалений."""

# my_list = [1, 2, 3, 4, 5]
# element = my_list.pop(2)
# print(element)  # Виведе: 3
# print(my_list)  # Виведе: [1, 2, 4, 5]

"""Метод del використовується для видалення елементів зі списку за їхнім індексом або діапазоном індексів. Ось синтаксис методу del:"""
# del list[index]
# де list - це ім'я списку, а index - це індекс елемента, який потрібно видалити.

# my_list = [1, 2, 3, 4, 5]
# del my_list[2]  # Видалення елемента з індексом 2 (третій елемент)
# print(my_list)  # Виведе: [1, 2, 4, 5]

"""Метод remove() використовується для видалення першого входження конкретного елемента зі списку. 
Він приймає один аргумент - значення елемента, який потрібно видалити."""
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)
# print(my_list)  # Виведе: [1, 2, 4, 5]

"""Метод clear() використовується для видалення всіх елементів зі списку, роблячи його порожнім."""
# my_list = [1, 2, 3, 4, 5]
# my_list.clear()
# print(my_list)  # Виведе: []

"""Метод index() використовується для знаходження індексу першого входження певного значення у списку."""
# my_list = [1, 2, 3, 4, 3, 5]
# index_of_three = my_list.index(3)
# print(index_of_three)  # Виведе: 2

"""Метод count() використовується для підрахунку кількості входжень певного значення у списку."""
# my_list = [1, 2, 3, 4, 3, 5]
# count_of_three = my_list.count(3)
# print(count_of_three)  # Виведе: 2

"""Функція any() приймає ітерабельний об'єкт (наприклад, список) і повертає True, якщо хоча б один елемент цього об'єкту
є істинним (не рівним нулю, пустим або False), в іншому випадку повертає False."""
# my_list = [0, False, '', None, 5]
# result = any(my_list)
# print(result)  # Виведе: True

"""Функція all() приймає ітерабельний об'єкт (наприклад, список) і повертає True, якщо всі елементи цього об'єкту є 
істинними (не рівні нулю, пусті або False), в іншому випадку повертає False."""
# my_list = [1, True, 'hello']
# result = all(my_list)
# print(result)  # Виведе: True

"""reverse() змінює послідовність на протилежну"""
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)  # Виведе: [5, 4, 3, 2, 1]

"""Функція reversed() в Python не змінює сам список, а створює ітератор, який обертається у зворотньому порядку над списком 
або іншим ітерабельним об'єктом. Це означає, що reversed() повертає ітератор, який можна використовувати для ітерації через 
елементи у зворотньому порядку без зміни оригінального списку."""
# my_list = [1, 2, 3, 4, 5]
# reversed_list = reversed(my_list)
# print(list(reversed_list))  # Виведе: [5, 4, 3, 2, 1]

"""Метод sort() сортує елементи списку на місці (тобто змінює сам список) і не повертає нового списку."""
# list.sort(key=None, reverse=False)
# key (необов'язковий): Функція, яка буде використана для сортування. Наприклад, key=str.lower буде сортувати елементи без врахування регістру.
# reverse (необов'язковий): Якщо встановлено в True, список буде відсортований у зворотному порядку (за спаданням).

"""Функція sorted() повертає новий відсортований список і не змінює вихідний список."""
# sorted(iterable, key=None, reverse=False)

# my_list = [5, 2, 9, 1, 5, 6]
# sorted_list = sorted(my_list)
# print(sorted_list)  # Виведе: [1, 2, 5, 5, 6, 9]
# print(my_list)  # Виведе: [5, 2, 9, 1, 5, 6]
#
# sorted_list_desc = sorted(my_list, reverse=True)
# print(sorted_list_desc)  # Виведе: [9, 6, 5, 5, 2, 1]

"""sort(): Використовуйте, коли вам потрібно відсортувати список на місці і не потрібен оригінальний порядок елементів після сортування.
   sorted(): Використовуйте, коли вам потрібно отримати новий відсортований список, зберігаючи оригінальний список без змін."""

""""Кортежі tuple() - впорядковані послідовності елементів. Це тіж самі списки але незмінні (immutable)"""
# my_tuple = tuple()
"""Створіть кортеж чисел і знайдіть їх суму."""
# numbers_tuple = tuple(range(1, 11))
# sum_values = sum(numbers_tuple)
# print(sum_values)

"""Створіть кортеж строк і змініть їх порядок в зворотньому напрямку."""
# string_tuple = ("apple", "banana", "cherry", "date")
# reverse_string_tuple = ()
# for i in reversed(string_tuple):
#      reverse_string_tuple += (i,)
# print(f'{reverse_string_tuple=}')
#
# # або
# reverse_string_tuple = tuple(reversed(string_tuple))
# print(f'{reverse_string_tuple=}')
#
# # або
# reverse_string_tuple = string_tuple[::-1]
# print(f'{reverse_string_tuple=}')

"""Створіть два кортежі і об'єднайте їх, створивши новий кортеж."""

# string_tuple1 = ("apple", "banana", "cherry", "date")
# string_tuple2 = (1, 2, 3, 4)
# common_string_tuple = string_tuple1 + string_tuple2
# print(common_string_tuple)
# common_string_tuple_cycle = ()
# for i, n in zip(string_tuple1, string_tuple2):
#     common_string_tuple_cycle += (i,)
#     common_string_tuple_cycle += (n,)
# print(common_string_tuple_cycle)

"""Створіть кортеж, що містить ім'я та вік, і розпакуйте його значення в дві змінні."""
# names_age = (('Jenya', 23), ('Tanya', 26), ('Bodya', 32), ('Musya', 38))
# names = []
# age = []
# for i, n in names_age:
#     names += [i]
#     age += [n]
# print(f'''{names=},
# {age=}''')

"""Створіть кортеж різних типів даних і перевірте, чи є певний елемент у кортежі."""
# diffrent_values_tuple = ('apple', 2, 7, 'Busya', {'Robbin', 'Bobin'}, [1, 2, 3,])
# print({'Robbin', 'Bobin'} in diffrent_values_tuple)

"""Створіть список елементів і перетворіть його в кортеж"""
# list_values = [3, 5, 6, 4, 5, 9, 7, 8,]
# tuple_list_values = tuple(list_values)
# print(tuple_list_values)
#
"""Створіть кортеж чисел і використайте зріз для отримання підмножини цих чисел."""
# slice_tuple_list_values = tuple_list_values[1:5]
# print(slice_tuple_list_values)

"""Створіть кортеж, який містить координати точки в тривимірному просторі (x, y, z)."""
# x, y, z = (34, 56, 118)

"""Порівняйте два кортежі і виведіть повідомлення про те, чи вони рівні, чи різні."""

# string_tuple1 = ("apple", "banana", "cherry", "date")
# string_tuple2 = (1, 2, 3, 4, 5)
# if len(string_tuple1) == len(string_tuple2):
#     print('Кортежі рівні')
# else: print('Кортежі не рівні')

"""Створіть кортеж, що містить числа від 1 до 10 включно."""
# num_tuple = tuple(range(1, 11))
# print(num_tuple)


# students_data = (
#     ('John', 'Doe', [85, 90, 88]),
#     ('Alice', 'Smith', [78, 92, 85]),
#     ('Bob', 'Johnson', [60, 75, 82]),
#     )
# students_data = list(students_data)

"""Напишіть функцію для обчислення середнього балу кожного студента і повернення результату у новому кортежі."""
# def calculate_average_grades(students_data: tuple) -> list:
#     names = ()
#     surnames = ()
#     marks = []
#     average_marks = []
#
#     for name, surname, student_mark in students_data:
#         names += (name,)
#         surnames += (surname,)
#         marks.append(student_mark)
#         average_mark = round(sum(student_mark) / len(marks))
#         average_marks.append(average_mark)
#     result = [names, surnames, average_marks]
#     return result
# print("{:<15} {:<15} {:<15}".format("Name", "Surname", "Average Mark"))


# def calculate_average_grades(students_data: tuple) -> list:
#     names = ()
#     surnames = ()
#     marks = []
#     average_marks = []
#
#     for name, surname, student_marks in students_data:
#         names += (name,)
#         surnames += (surname,)
#         marks.append(student_marks)  # Використовуємо список для оцінок
#
#         # Обчислюємо середню оцінку для кожного студента
#         avg_mark = sum(student_marks) / len(student_marks)
#         average_marks.append(avg_mark)
#
#     result = [names, surnames, average_marks]
#     return result

"""Множини set() - невпорядковані послідовності УНІКАЛЬНИХ елементів. Не підтримує індексацію"""
# my_set = set()
"""add(element): Додає елемент до множини. Якщо елемент вже присутній, нічого не змінюється."""
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # виведе: {1, 2, 3, 4}
"""remove(element): Видаляє заданий елемент з множини. Якщо елемент відсутній, видає помилку KeyError."""
"""discard(element): Видаляє заданий елемент з множини, якщо він присутній. Якщо елемент відсутній, нічого не змінюється."""
"""clear(): Видаляє всі елементи з множини, робить її порожньою"""


"""Операції над декількома множинами"""

"""union(other_set): Повертає нову множину, яка є об'єднанням поточної множини з іншою множиною."""
"""intersection(other_set): Повертає нову множину, яка є перетином поточної множини з іншою множиною."""
"""difference(other_set): Повертає нову множину, яка містить елементи, що присутні в поточній множині, але відсутні в іншій множині."""
"""symmetric_difference(other_set): Повертає нову множину, яка містить елементи, що присутні або в поточній множині, або в іншій множині, але не в обох."""

"""Функції для роботи з множинами"""
"""set(iterable): Створює нову множину, що містить елементи з ітерабельного об'єкту (наприклад, списку, кортежу)."""

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = {7, 8, 9, 10, 11}

"""Створіть нову множину, яка містить усі унікальні елементи з усіх трьох початкових множин."""

# uniq_set = set1.union(set2, set3)
# print(uniq_set)

"""Знайдіть симетричну різницю між першою та другою множинами."""

# sym_difr = set1.symmetric_difference(set2)
# print(sym_difr)

"""Перевірте, чи є спільні елементи у другій та третій множинах."""

# common_values = set2.isdisjoint(set3)
# print(common_values)

"""Виведіть всі елементи, які є унікальними для кожної множини (тобто елементи, які не мають спільних елементів в інших множинах)."""

# uniq_set1 = set1.difference(set2.union(set3))
# print('Унікальні елементи першої множини:', uniq_set1)
# uniq_set2 = set2.difference(set1.union(set3))
# print('Унікальні елементи другої множини:',uniq_set2)
# uniq_set3 = set3.difference(set1.union(set2))
# print('Унікальні елементи третьої множини:',uniq_set3)

"""Створіть програму, яка приймає дві множини від користувача, обчислює їхні об'єднання та різницю, а потім виводить результат."""

# def set_difference_union(set1, set2) -> list:
#     result = []
#     input_set1 = input('Введіть через пробіл цифри першої множини: ')
#     input_set2 = input('Введіть через пробіл цифри другої множини: ')
#     set1 = set(input_set1.split())
#     set2 = set(input_set2.split())
#     set_union = set1.union(set2)
#     set_difference = set1.difference(set2)
#     result = [f'Union :{set_union}, Difference: {set_difference}']
#     return result
# print(set_difference_union(0, 0))

"""Frozen_set = frozenset('Frozen') це множина, яку неможливо змінити"""
# print(Frozen_set)

"""Генератори множин"""
# words = ["sun", "sea", "water", "cloud", "tree", "summer", "winter"]
# longer_than_four = {word for word in words if len(word) > 4}
# print(longer_than_four)

"""Itertools Modul - - це універсальний модуль Python, який спрощує та покращує операції, пов'язані з ітераціями, 
завдяки готовим до використання функціям для створення та маніпулювання ітераторами.

                                        Використання itertools: 
1. Складні комбінації та перестановки: Якщо вам потрібно генерувати комбінації, перестановки або 
декартові добутки елементів, використання itertools спростить завдання і зробить код більш читабельним. 
2. Ефективність пам'яті: Коли потрібно обробляти великі набори даних і важливо уникати створення проміжних списків в пам'яті, 
itertools створює генератори, які працюють "на льоту".
3. Складні фільтри та групування: Для складних операцій фільтрації або групування даних, де звичайний цикл став би занадто громіздким.
4. Акумуляція значень: Для обчислення накопичувальних сум або інших подібних операцій.
"""

"""Метод count у модулі itertools в Python використовується для створення нескінченного ітератора, який повертає 
послідовність чисел, починаючи з певного значення і збільшуючи його на заданий крок."""

# from itertools import count
#
# iterator = count(start=3, step=2)
# for _ in range(5):
#     print(next(iterator), end=" ")

"""Метод cycle створює ітератор, який безкінечно повторює послідовність елементів з заданого ітерабельного об'єкта."""

# from itertools import cycle
#
# numbers = cycle([1, 2, 3])
# for _ in range(6):
#     print(next(numbers), end=" ")

"""Метод  repeat створює ітератор, який повторює заданий об'єкт безкінечно або певну кількість разів."""

# from itertools import repeat
#
# repeated_numbers = repeat(5, times=3)
# for num in repeated_numbers:
#     print(num)

"""Метод combinations використовується для створення ітератора, який повертає всі можливі комбінації заданої довжини 
з елементів ітерабельного об'єкта без повторень."""

# from itertools import combinations
#
# numbers = [1, 2, 3, 4]
# combo = combinations(numbers, 2)
# for comb in combo:
#     print(comb, end=" ")

"""Метод combinations_with_replacement використовується для створення ітератора, який повертає всі можливі комбінації 
заданої довжини з елементів ітерабельного об'єкта з повтореннями."""

# from itertools import combinations_with_replacement

# Створюємо ітератор, який повертає всі можливі комбінації довжиною 2 зі списку букв
# letters = ['a', 'b', 'c']
# combs_with_replacement = combinations_with_replacement(letters, 2)

# Виводимо комбінації з повтореннями
# for comb in combs_with_replacement:
#     print(comb)

"""Метод permutations використовується для створення ітератора, який повертає всі можливі перестановки заданої довжини 
з елементів ітерабельного об'єкта."""
# from itertools import permutations

# Створюємо ітератор, який повертає всі можливі перестановки довжиною 2 зі списку букв
# letters = ['a', 'b', 'c']
# perms = permutations(letters, 2)

# Виводимо перестановки
# for perm in perms:
#     print(perm)

"""Метод product використовується для створення ітератора, який повертає декартовий добуток декількох ітерабельних об'єктів."""

# from itertools import product

# Створюємо ітератор, який повертає декартовий добуток двох списків чисел
# numbers1 = [1, 2, 3]
# numbers2 = ['a', 'b']
# cartesian_product = product(numbers1, numbers2)

# Виводимо декартовий добуток
# for item in cartesian_product:
#     print(item)
"""Метод accumulate: Повертає ітератор, який накопичує результати функції для всіх елементів ітерабельного об'єкта."""
# from itertools import accumulate
# import operator
#
# numbers = [1, 2, 3, 4, 5]
# result = accumulate(numbers, operator.add)
# print(list(result))  # [1, 3, 6, 10, 15]

"""Метод chain: Об'єднує кілька ітерабельних об'єктів в один."""
# from itertools import chain
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# combined = chain(list1, list2)
# print(list(combined))  # [1, 2, 3, 'a', 'b', 'c']

"""Метод compress: Фільтрує елементи ітерабельного об'єкта на основі іншого ітерабельного об'єкта з булевими значеннями."""
# from itertools import compress
#
# data = ['a', 'b', 'c', 'd']
# selectors = [1, 0, 1, 0]
# result = compress(data, selectors)
# print(list(result))  # ['a', 'c']

"""Метод dropwhile: Відкидає елементи з ітерабельного об'єкта до тих пір, поки функція повертає True, а потім повертає всі інші елементи."""
# from itertools import dropwhile
#
# numbers = [1, 2, 3, 4, 5]
# result = dropwhile(lambda x: x < 3, numbers)
# print(list(result))  # [3, 4, 5]

"""Метод takewhile: Повертає елементи з ітерабельного об'єкта, поки функція повертає True."""
# from itertools import takewhile
#
# numbers = [1, 2, 3, 4, 5]
# result = takewhile(lambda x: x < 3, numbers)
# print(list(result))  # [1, 2]

"""Метод groupby: Групує елементи ітерабельного об'єкта за ключем."""
# from itertools import groupby
#
# data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 25}]
# grouped = groupby(data, key=lambda x: x['age'])
# for key, group in grouped:
#     print(key, list(group))
# 25 [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}]
# 30 [{'name': 'Bob', 'age': 30}]

"""Dictionaries in Python — це зручний і потужний інструмент для зберігання та обробки даних у вигляді пар "ключ-значення". 
Вони аналогічні асоціативним масивам або хеш-таблицям в інших мовах програмування. Розглянемо основні можливості та 
операції зі словниками в Python. Елементи у словниках зберігаються в вільному порядку"""
# my_first_dictionary = {'key': 'value'}

# k = ['a', 'b'] - список з ключами
# v = [1, 2] - список зі значеннями
# list(zip(k, v)) - створення списку кортежей
# d = dict(zip(k, v)) - створення словника
# print(d)
"""створення словника за допомогою фігурних скобок"""
# e = {'a': 1, 'b': 2}
# print(e)

"""fromkeys метод в Python дозволяє створити новий словник із заданими ключами та встановленим значенням за замовчуванням 
для кожного ключа. Цей метод є статичним і його можна викликати як у самого словника, так і у типу dict."""
# dict.fromkeys(iterable, value=None)
# iterable — послідовність, яка містить ключі для нового словника.
# value (необов'язковий) — значення, яке буде встановлено для всіх ключів. За замовчуванням None.
"""Example:"""
# keys = ('name', 'age', 'city')
# new_dict = dict.fromkeys(keys, "unknown")
# print(new_dict)

"""При створенні словника в змінній зберігається ссилка на об'єкт, а не сам об'єкт. З цього виходить, що для словників неможливе групове присваювання"""
# d1 = {'a': 1, 'b': 2}
# d2 = dict(d1)
# d = d1 is d2 # різні об'єкти
# print(d) # False

"""Створення словника за допомогою comprehensions виразу"""
# data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
# name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
# print(name_age_dict)

"""Створення поверхневої копії shallow copy. Поверхнева копія створює новий об'єкт, але не копіює вкладені об'єкти всередині нього. 
Замість цього вона лише копіює посилання на ці вкладені об'єкти. Це означає, що зміни у вкладених об'єктах у копії 
впливатимуть на оригінальний об'єкт, і навпаки."""
import copy

# original_dict = {
#     'a': 1,
#     'b': {'c': 2}
# }
#
# shallow_copy = original_dict.copy()
#
# # Змінимо вкладений об'єкт у копії
# shallow_copy['b']['c'] = 3
#
# print("Original:", original_dict)  # {'a': 1, 'b': {'c': 3}}
# print("Shallow Copy:", shallow_copy)  # {'a': 1, 'b': {'c': 3}}

"""Глибока копія створює новий об'єкт, а також рекурсивно копіює всі об'єкти, вкладені у вихідний об'єкт. Це означає, 
що зміни у вкладених об'єктах в копії не впливатимуть на оригінальний об'єкт, і навпаки."""
# import copy
#
# original_dict = {'a': 1, 'b': {'c': 2}}
#
# deep_copy = copy.deepcopy(original_dict)
# deep_copy['b']['c'] = 3
# print(original_dict)  # {'a': 1, 'b': {'c': 2}}
# print(deep_copy) # {'a': 1, 'b': {'c': 3}}

"""Метод get() використовується для отримання значення зі словника за ключем. Він є безпечнішим варіантом доступу до значення, 
оскільки, якщо ключ не знайдено у словнику, метод не викине помилку, а поверне значення за замовчуванням або None, 
якщо значення за замовчуванням не вказано. Також можна вказати власне значення за замовчуванням для випадку, коли ключ не знайдено."""
# value = my_dict.get(key, default=None)

"""Метод get() є корисним, коли ви хочете отримати значення зі словника, але не впевнені, чи існує відповідний ключ, 
або якщо вам потрібно обробити випадок, коли ключ відсутній."""
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Отримання значень за ключами
# name = my_dict.get('name')
# print(name)  # Виведе: John

# Отримання значення за неіснуючим ключем
# email = my_dict.get('email')
# print(email)  # Виведе: None

# Отримання значення за неіснуючим ключем зі значенням за замовчуванням
# email = my_dict.get('email', 'no_email@example.com')
# print(email)  # Виведе: no_email@example.com

"""Метод setdefault() використовується для отримання значення зі словника за ключем. Якщо ключ вже присутній у словнику, 
метод поверне відповідне значення. Якщо ключ відсутній, метод додасть нову пару "ключ-значення" з заданим значенням за 
замовчуванням і поверне це значення."""
# value = my_dict.setdefault(key, default=None)

"""Метод setdefault() корисний тоді, коли вам потрібно додати новий ключ до словника і встановити йому значення за замовчуванням,
 або якщо вам потрібно отримати значення за ключем, переконавшись, що цей ключ існує у словнику."""
# my_dict = {'name': 'John', 'age': 30}

# Отримання значень за ключами
# name = my_dict.setdefault('name')
# print(name)  # Виведе: John

# Додавання нового ключа зі значенням за замовчуванням
# email = my_dict.setdefault('email', 'no_email@example.com')
# print(email)  # Виведе: no_email@example.com
# print(my_dict)  # Виведе: {'name': 'John', 'age': 30, 'email': 'no_email@example.com'}

# Використання методу без значення за замовчуванням
# city = my_dict.setdefault('city')
# print(city)  # Виведе: None
# print(my_dict)  # Виведе: {'name': 'John', 'age': 30, 'email': 'no_email@example.com', 'city': None}

# Зміна значення існуючого ключа
# name = my_dict.setdefault('name', 'Mike')  # Не змінить значення, оскільки ключ вже існує
# print(name)  # Виведе: John
# print(my_dict)  # Виведе: {'name': 'John', 'age': 30, 'email': 'no_email@example.com', 'city': None}

"""Так як словники відносяться до змінних типів даних, ми можемо міняти значення за ключем. Якщо елемент з вказаним ключем 
відсутній, він буде добавлений в словник"""

# Початковий словник
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# Зміна значення існуючого ключа
# my_dict['b'] = 5
# print(my_dict)  # {'a': 1, 'b': 5, 'c': 3}

# Зміна значення неіснуючого ключа
# my_dict['d'] = 7
# print(my_dict)  # {'a': 1, 'b': 5, 'c': 3, 'd': 7}

"""Словники підтримують ітерації, отже по ним можна проходитись циклом for та використовувати модуль itertools"""
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d.keys():
#     print("({0}) => {1}".format(key, d[key]), end=" ")
# print()
# for key in d:
#     print("({0}) => {1}".format(key, d[key]), end=" ")

# import itertools

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Фільтрація за значенням
# filtered_dict = {k: v for k, v in my_dict.items() if v > 2}
# print(filtered_dict)

# Групування за значенням
# grouped_dict = {}
# for key, group in itertools.groupby(my_dict.items(), lambda x: x[1]):
#     grouped_dict[key] = [item[0] for item in group]
# print(grouped_dict)

"""Так як словники є невпорядкованими структурами, елементи виводяться в довільному порядку
Щоб вивести елементи з сортуванням по ключам, треба отримати список ключів, а потім використати методь sort()"""
# d = {'x': 1, 'y': 2, 'z': 3}
# k = list(d.keys())
# k.sort()
# for key in k:
#     print("({0}) => {1}".format(key, d[key]), end=" ")

"""для сортування ключів також можна використати функцію sorted() і зразу же їй передати об'єкт словника, а не результат 
виконання методу keys()"""
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in sorted(d):
#     print("({0}) => {1}".format(key, d[key]), end=" ")

"""Метод keys() повертає об'єкт виду dict_keys, який містить усі ключі словника. Цей об'єкт підтримує ітерації і може бути 
перетворений на список."""

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# Отримати всі ключі
# keys = my_dict.keys()
# print(keys)  # dict_keys(['a', 'b', 'c'])

# Перетворити на список
# keys_list = list(keys)
# print(keys_list)  # ['a', 'b', 'c']

# Ітерувати по ключах
# for key in my_dict.keys():
#     print(key)

"""Метод values() Повертає об'єкт dict_values, який містить усі значення словника."""

# values = my_dict.values()
# print(values)  # dict_values([1, 2, 3])

# values_list = list(values)
# print(values_list)  # [1, 2, 3]

"""Метод items() Повертає об'єкт dict_items, який містить пари (ключ, значення)."""

# items = my_dict.items()
# print(items)  # dict_items([('a', 1), ('b', 2), ('c', 3)])
#
# items_list = list(items)
# print(items_list)  # [('a', 1), ('b', 2), ('c', 3)]

"""Метод get() Повертає значення за вказаним ключем. Якщо ключ відсутній, повертає значення за замовчуванням 
(або None, якщо значення за замовчуванням не вказано)."""

# value = my_dict.get('b')
# print(value)  # 2
#
# value = my_dict.get('d', 'Not Found')
# print(value)  # Not Found

"""Метод setdefault() Повертає значення за вказаним ключем. Якщо ключ відсутній, додає його зі значенням за замовчуванням 
і повертає це значення."""

# value = my_dict.setdefault('d', 4)
# print(value)  # 4
# print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

"""Метод pop() Видаляє ключ і повертає його значення. Якщо ключ відсутній, викликає помилку, 
якщо не вказано значення за замовчуванням."""

# value = my_dict.pop('a')
# print(value)  # 1
# print(my_dict)  # {'b': 2, 'c': 3, 'd': 4}
#
# value = my_dict.pop('e', 'Not Found')
# print(value)  # Not Found

"""Метод popitem() Видаляє і повертає пару (ключ, значення) з кінця словника. Якщо словник порожній, викликає помилку."""

# item = my_dict.popitem()
# print(item)  # ('d', 4)
# print(my_dict)  # {'b': 2, 'c': 3}

"""Метод update() Оновлює словник, додаючи пари з іншого словника або ітерації пар (ключ, значення)."""

# my_dict.update({'e': 5, 'f': 6})
# print(my_dict)  # {'b': 2, 'c': 3, 'e': 5, 'f': 6}
#
# my_dict.update(g=7, h=8)
# print(my_dict)  # {'b': 2, 'c': 3, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

"""Метод clear() Видаляє всі елементи зі словника."""

# my_dict.clear()
# print(my_dict)  # {}

"""Генератори словників dictionary comprehensions дозволяють створювати нові словники за допомогою синтаксису, 
подібного до генераторів списків. Вони забезпечують зручний і компактний спосіб побудови словників на основі існуючих 
ітераційних структур."""

# my_dictionary = {key_expr: value_expr for item in iterable}

"""Приклади використання
Створення словника зі списку чисел:"""
# numbers = [1, 2, 3, 4]
# squares = {n: n**2 for n in numbers}
# print(squares)  # Виведе: {1: 1, 2: 4, 3: 9, 4: 16}

"""Створення словника зі списку рядків:"""
# words = ["apple", "banana", "cherry"]
# lengths = {word: len(word) for word in words}
# print(lengths)  # Виведе: {'apple': 5, 'banana': 6, 'cherry': 6}

"""Фільтрація за допомогою умов:"""
# numbers = [1, 2, 3, 4, 5, 6]
# even_squares = {n: n**2 for n in numbers if n % 2 == 0}
# print(even_squares)  # Виведе: {2: 4, 4: 16, 6: 36}

"""Генерація словника зі списку кортежів:"""
# pairs = [('a', 1), ('b', 2), ('c', 3)]
# my_dict = {key: value for key, value in pairs}
# print(my_dict)  # Виведе: {'a': 1, 'b': 2, 'c': 3}

"""Зміна значень у наявному словнику:"""
# old_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict = {k: v*2 for k, v in old_dict.items()}
# print(new_dict)  # Виведе: {'a': 2, 'b': 4, 'c': 6}

"""Ви також можете використовувати вкладені цикли в генераторах словників."""
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_dict = {i: value for i, row in enumerate(matrix) for value in row}
# print(flat_dict)  # Виведе: {0: 1, 0: 2, 0: 3, 1: 4, 1: 5, 1: 6, 2: 7, 2: 8, 2: 9}

"""Приклад з вкладеними генераторами словників"""
# Вкладені генератори словників для створення словника з іншого словника
# nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# flat_dict = {outer_k + '_' + inner_k: inner_v for outer_k, inner_dict in nested_dict.items() for inner_k, inner_v in inner_dict.items()}
# print(flat_dict)  # Виведе: {'first_a': 1, 'second_b': 2}

"""Створіть словник, де ключами будуть рядки зі списку words, а значеннями - їх довжини."""
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# my_dict = {key: len(key) for key in words}
# print(my_dict)

"""Як створити словник, де ключами є числа від 1 до 5, а значеннями - квадрати цих чисел?"""
# my_dict = {}
# for i in range(1, 6):
#     my_dict[i] = i ** 2
# for key, value in my_dict.items():
#     print(key, value)
"""Як видалити всі пари ключ-значення зі словника inventory, які мають значення менше 10?"""
# filtered_inventory = {key: value for key, value in my_dict.items() if value >= 10}
# print(filtered_inventory)

""" Як вибрати випадковий ключ-значення зі словника my_dict"""
# import random
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# random_key, random_value = random.choice(list(my_dict.items()))
#
# print("Випадковий ключ:", random_key)
# print("Випадкове значення:", random_value)

""" Як перевірити, чи містить словник my_dict хоча б один ключ "age"?"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# print(my_dict.get('age', None))

""" Як знайти ключ за відповідним значенням "value" у словнику my_dict"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# search_key = {key: value for key, value in my_dict.items() if value == 'orange'}
# print(search_key)

""" Як видалити перший елемент у словнику my_dict"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# first_value = list(my_dict.values())[0] if my_dict else None
# key_to_remove = [key for key, value in my_dict.items() if value == first_value]
# print(type(key_to_remove))
# for key in key_to_remove:
#     del my_dict[key]
# print(my_dict)

""" Як об'єднати два словники, і якщо ключі співпадають, додати їхні значення?"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# my_dict2 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# common_double_dict = {}
# for key, value in my_dict.items():
#     common_double_dict[key] = my_dict.get(key, 0) + value
# for key, value in my_dict2.items():
#     common_double_dict[key] = my_dict2.get(key, 0) + value
# print(common_double_dict)

"""Як видалити перший елемент у словнику my_dict"""
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value_to_remove = list(my_dict.values())[0]
# key_to_remove = [key for key, value in my_dict.items() if value == value_to_remove]
# for key in key_to_remove:
#     del my_dict[key]
# print(my_dict)

""" Як видалити всі пари ключ-значення зі словника, які мають значення, які повторюються?"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# my_dict2 = {}
# for key, value in my_dict.items():
#     if value not in my_dict2.values():
#         my_dict2[key] = value
#
# print(my_dict2)

""" Як визначити, чи є два словники рівними?"""
# my_dict = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape', 6: 'orange'}
# my_dict2 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'apple', 5: 'grape'}
# if len(my_dict) == len(my_dict2):
#     print('Yes')
# else:
#     print('No')
""" Як перевірити, чи існує словник my_dict"""
# print(my_dict)

# Створюємо порожній словник з використанням анонімної функції
# my_dict = {i + 1: lambda: random.randint(1, 100) for i in range(30)}

""" Як визначити максимальне значення у словнику my_dict"""

# scores = {}
# for i in range(1, 6):
#     scores[i] = i ** 2
# print(scores)
# max_value_in_dict_scores = max(value for value in scores.values())
# print(max_value_in_dict_scores)

"""#Створіть словник чисел і використайте анонімну функцію для відфільтрування лише тих значень,
які задовольняють певну умову (наприклад, парні числа)."""
# import random
# import re

# start = 1
# end = 20
# my_dict = {num: num for num in range(start, end + 1)}
# print(my_dict)
# sorted_dict = filter(lambda x: x % 2 == 0, my_dict.values())
# print(list(sorted_dict))


"""Створіть два словники та напишіть функцію, яка об'єднує їх у новий словник. Якщо ключі збігаються, об'єднайте значення в одне."""
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'd': 5, 'e': 6}
# def add_dicts(dict1:dict, dict2:dict) ->dict:
#     dict3 = {}
#     dict3.update(dict1)
#     for key, value in dict2.items():
#         if key in dict3:
#             dict3[key] += value
#         else:
#             dict3[key] = value
#     return dict3
# print(add_dicts(dict1, dict2))
"""Створіть словник, який містить рядок тексту.
# Підрахуйте кількість кожної цифри у тексті та збережіть результат у словнику.
# Виведіть отриманий словник підрахунку кількості кожної цифри у тексті."""

# text_dictionary = {
#      'sample_text': "T1h2i4s i6s a7 sa4787mpl1845650e t4457ext. It4564645 can co739664ntain multi400568ple se55ntence3223s."}
# count_dict = {}
# text = text_dictionary['sample_text']
# for num in text:
#      if num.isdigit():
#           count_dict[num] = count_dict.get(num, 0) + 1
# print('Кількість цифр в цьому виразі:')
# print()
# for key, value in count_dict.items():
#     print(key, value, end="|")

"""Модуль datetime надає класи для маніпуляції датою і часом."""
"""Створення об'єктів дати та часу"""
import datetime
""" Поточна дата та час"""
# now = datetime.datetime.now()
# print(now)

""" Поточна дата"""
# today = datetime.date.today()
# print(today)

"""Створення конкретної дати"""
# specific_date = datetime.date(2024, 6, 15)
# print(specific_date)

"""Створення конкретного часу"""
# specific_time = datetime.time(14, 30, 0)
# print(specific_time)

"""Створення конкретної дати та часу"""
# specific_datetime = datetime.datetime(2024, 6, 15, 14, 30, 0)
# print(specific_datetime)

"""Функція gmtime() повертає поточний час в форматі UTC (з координованого всесвітнього часу).
Результатом буде об'єкт класу struct_time, який містить інформацію про рік, місяць, день, годину, хвилину, секунду та інші атрибути."""
import time
# Отримання поточного часу у форматі UTC
# utc_time = time.gmtime()
# print(utc_time)

"""Функція localtime() повертає поточний локальний час з урахуванням налаштувань часового поясу на комп'ютері.
Результатом також буде об'єкт класу struct_time, але з інформацією, відповідною налаштуванням локального часу на вашому комп'ютері."""
# Отримання поточного локального часу
# local_time = time.localtime()
# print(local_time)

"""Клас struct_time є структурою даних, що містить інформацію про час у певному форматі. Він містить такі атрибути:

tm_year: рік
tm_mon: місяць (1-12)
tm_mday: день місяця (1-31)
tm_hour: година (0-23)
tm_min: хвилина (0-59)
tm_sec: секунда (0-59)
tm_wday: день тижня (0 - понеділок, 6 - неділя)
tm_yday: день року (1-366)
tm_isdst: флаг підсвічування літнього часу (1, 0, або -1)
Цей об'єкт зазвичай повертається функціями gmtime() і localtime(), і його можна обробляти для подальшої обробки даних про час."""

"""Ось як виглядає простий приклад використання функцій gmtime() і localtime():"""
import time

# Отримання поточного часу у форматі UTC
# utc_time = time.gmtime()
# print("UTC час:", utc_time)

# Отримання поточного локального часу
# local_time = time.localtime()
# print("Локальний час:", local_time)

"""Завдання: вивід поточної дати часу, дня тижня, року на українській мові """
import datetime
# Отримання поточної дати та часу
# now = datetime.datetime.now()
# Створення словника для відповідності назв днів тижня українською мовою
# ukrainian_days = {0: "Понеділок",1: "Вівторок",2: "Середа",3: "Четвер",4: "П'ятниця",5: "Субота",6: "Неділя"}

# Отримання номера дня тижня (понеділок - 0, ..., неділя - 6)
# weekday = now.weekday()
# Визначення року
# year = now.year

# Вивід результату на екран
# print("Поточна дата і час:", now.strftime("%Y-%m-%d %H:%M:%S"))
# print("День тижня:", ukrainian_days[weekday])
# print("Рік:", year)

"""Метод strftime() дозволяє форматувати об'єкт datetime у рядок за допомогою форматованих кодів. Ці коди визначають, 
як саме дата та час будуть представлені у рядку."""

"""Ось деякі з найбільш використовуваних форматованих кодів:

%Y: рік у форматі чотирьох цифр (наприклад, 2024)
%m: місяць у форматі двох цифр (01-12)
%d: день місяця у форматі двох цифр (01-31)
%H: година у 24-годинному форматі (00-23)
%M: хвилини (00-59)
%S: секунди (00-59)
%f: мікросекунди (000000-999999)
%A: повна назва дня тижня
%a: скорочена назва дня тижня
%B: повна назва місяця
%b: скорочена назва місяця
%p: AM або PM
%Z: назва часового поясу"""

import datetime

# now = datetime.datetime.now()

# Форматування у вигляді "YYYY-MM-DD HH:MM:SS"
# formatted_date_time_1 = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Форматування 'YYYY-MM-DD HH:MM:SS':", formatted_date_time_1)

# Форматування з повними назвами місяців та днів тижня
# formatted_date_time_2 = now.strftime("%A, %B %d, %Y %H:%M:%S")
# print("Форматування з повними назвами:", formatted_date_time_2)

# Форматування зі скороченими назвами місяців та днів тижня та 12-годинним форматом
# formatted_date_time_3 = now.strftime("%a, %b %d, %Y %I:%M:%S %p")
# print("Форматування зі скороченими назвами та 12-годинним форматом:", formatted_date_time_3)

"""Метод strptime() (від англ. "string parse time") приймає два аргументи:

Рядок, який потрібно розпарсити.
Формат, у якому представлена дата і час у цьому рядку.
Форматовані коди
Для парсингу використовуються ті ж самі форматовані коди, що і для форматування за допомогою методу strftime(). Ось деякі з них:

%Y: рік у форматі чотирьох цифр (наприклад, 2024)
%m: місяць у форматі двох цифр (01-12)
%d: день місяця у форматі двох цифр (01-31)
%H: година у 24-годинному форматі (00-23)
%M: хвилини (00-59)
%S: секунди (00-59)
%f: мікросекунди (000000-999999)"""

"""Ось приклад, який демонструє парсинг різних форматів дат та часу з рядків:"""
import datetime

# Різні формати рядків дат та часу
# date_str1 = "2024-06-15 14:30:00"
# date_str2 = "15/06/2024 14:30"
# date_str3 = "15 June 2024 14:30:00"
# date_str4 = "15 Jun 2024 02:30:00 PM"

# Парсинг рядків у об'єкти datetime
# parsed_date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
# parsed_date2 = datetime.datetime.strptime(date_str2, "%d/%m/%Y %H:%M")
# parsed_date3 = datetime.datetime.strptime(date_str3, "%d %B %Y %H:%M:%S")
# parsed_date4 = datetime.datetime.strptime(date_str4, "%d %b %Y %I:%M:%S %p")

# Вивід результатів
# print("Парсинг 'YYYY-MM-DD HH:MM:SS':", parsed_date1)
# print("Парсинг 'DD/MM/YYYY HH:MM':", parsed_date2)
# print("Парсинг з повними назвами місяців:", parsed_date3)
# print("Парсинг зі скороченими назвами місяців та 12-годинним форматом:", parsed_date4)

"""Для отримання складових дати та часу в Python використовуються об'єкти з модуля datetime, такі як date, time,
та datetime. Ці об'єкти мають атрибути, які дозволяють легко доступитися до різних компонентів дати та часу."""

"""Об'єкт datetime представляє і дату, і час, тому має атрибути як для дати, так і для часу:

year: рік (напр. 2024)
month: місяць (01-12)
day: день місяця (01-31)
hour: година (00-23)
minute: хвилина (00-59)
second: секунда (00-59)
microsecond: мікросекунда (000000-999999)"""

import datetime

# Отримання поточної дати та часу
# now = datetime.datetime.now()

# Доступ до складових дати та часу
# print("Рік:", now.year)
# print("Місяць:", now.month)
# print("День:", now.day)
# print("Година:", now.hour)
# print("Хвилина:", now.minute)
# print("Секунда:", now.second)
# print("Мікросекунда:", now.microsecond)

# Отримання дня тижня
# day_of_week = now.weekday()
# print("День тижня (0 - понеділок, ..., 6 - неділя):", day_of_week)

# Альтернативний спосіб: отримання повної назви дня тижня
# weekday_name = now.strftime("%A")
# print("Назва дня тижня:", weekday_name)

"""Операції з датами і часом у Python дозволяють вам виконувати різноманітні маніпуляції з датами, такі як додавання або 
віднімання певної кількості днів, годин, хвилин тощо, а також визначення різниці між двома датами і часом. Для цього 
використовується модуль datetime зі своїм класом datetime і об'єктом timedelta."""

"""Клас timedelta визначає різницю між двома моментами часу. Він може використовуватися для додавання або віднімання 
певного часового інтервалу (наприклад, днів, годин, хвилин) до або від об'єкта datetime."""

# import datetime

# Поточна дата і час
# now = datetime.datetime.now()

# Додавання 3 днів до поточної дати і часу
# three_days = datetime.timedelta(days=3)
# future_date = now + three_days

# Віднімання 1 години від поточної дати і часу
# one_hour = datetime.timedelta(hours=1)
# past_date = now - one_hour

# Дві дати для порівняння
# date1 = datetime.datetime(2024, 6, 15, 12, 0, 0)
# date2 = datetime.datetime(2024, 6, 10, 8, 0, 0)
# difference = date1 - date2

# Вивід результатів
# print("Поточна дата і час:", now)
# print("Дата і час через 3 дні:", future_date)
# print("Дата і час на годину раніше:", past_date)
# print("Дата 1:", date1)
# print("Дата 2:", date2)
# print("Різниця між датами:", difference)

"""Робота з часовими поясами в Python зазвичай виконується за допомогою бібліотеки pytz. Ця бібліотека надає засоби для
 роботи зі списком часових поясів ІАНА (tz database) і здійснює конвертацію між різними часовими зонами."""

"""Приклад конвертації зі стандартного часового поясу UTC"""
# import datetime
# import pytz

# Поточний час у форматі UTC
# utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

# Конвертація у часовий пояс New York
# ny_tz = pytz.timezone('America/New_York')
# ny_time = utc_now.astimezone(ny_tz)

# print("Поточний час у New York:", ny_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

"""Робота з календарем в Python може включати різні завдання, такі як визначення кількості днів у місяці, 
перевірка високосного року, отримання дати на кілька днів вперед або назад, а також перевірка та обробка святкових днів. 
Для цих завдань використовуються модулі datetime та calendar в стандартній бібліотеці Python."""

"""Для визначення кількості днів у місяці використовують функцію monthrange з модулю calendar."""
"""У цьому прикладі calendar.monthrange(year, month) повертає кортеж (перший_день_тижня, кількість_днів_у_місяці), 
тому [1] витягуємо кількість днів у місяці."""
# import calendar

# Визначення кількості днів у червні 2024 року
# year = 2024
# month = 6
# days_in_month = calendar.monthrange(year, month)[1]

# print(f"У червні {year} року є {days_in_month} днів.")

"""Перевірка та обробка святкових днів"""
# import datetime

# Приклад власного списку святкових днів
# holidays = {
#     datetime.date(2024, 1, 1): "Новий Рік",
#     datetime.date(2024, 3, 8): "Міжнародний жіночий день",
#     datetime.date(2024, 5, 1): "День праці",
    # Додайте інші святкові дні за потреби
# }

# Перевірка, чи є сьогодні святковим днем
# today = datetime.date.today()
# if today in holidays:
#     print(f"Сьогодні {today} - святковий день: {holidays[today]}")
# else:
#     print(f"Сьогодні {today} - не святковий день.")

"""Модуль timeit призначений спеціально для вимірювання часу виконання малих фрагментів коду. Він автоматично виконує 
декілька проходів і обчислює середній час виконання для більш точного результату."""

"""Використання timeit для вимірювання часу виконання фрагменту коду"""

# import timeit

# Функція або фрагмент коду, який потрібно виміряти
# def my_function():
#     result = 0
#     for i in range(1000000):
#         result += i
#     return result

# Вимірюємо час виконання функції `my_function` за допомогою `timeit`
# execution_time = timeit.timeit(my_function, number=1)  # number - кількість викликів функції для вимірювання часу

# print(f"Час виконання: {execution_time:.6f} секунд")
"""У цьому прикладі:

Функція my_function виконується один раз (за допомогою параметру number=1).
timeit.timeit автоматично вимірює час виконання функції і повертає час у секундах.
Модуль time
Модуль time надає більш загальні засоби для роботи з часом, включаючи функції для вимірювання часу до і після виконання певного коду.

Використання time для вимірювання часу виконання фрагменту коду"""

# import time

# Початковий час
# start_time = time.time()

# Функція або фрагмент коду, який потрібно виміряти
# result = 0
# for i in range(1000000):
#     result += i

# Кінцевий час
# end_time = time.time()

# Вивід часу виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time:.6f} секунд")
"""У цьому прикладі:

time.time() повертає поточний час у секундах з початку епохи (зазвичай 1 січня 1970 року).
start_time і end_time використовуються для вимірювання часу до і після виконання циклу.
Різниця між end_time і start_time дає загальний час виконання фрагменту коду.
Вибір між timeit та time
timeit зазвичай використовується для вимірювання часу виконання коротких фрагментів коду, таких як функції або одиночні 
операції. Він автоматично проводить декілька проходів і розраховує середнє значення, що дозволяє отримати більш точний результат.

time надає більш гнучкий підхід для вимірювання часу виконання будь-якого коду. Ви вручну встановлюєте початковий 
і кінцевий час, що дозволяє вам точно визначити, який саме фрагмент коду вимірюється і як саме він виконується.

Рекомендації
Використовуйте timeit, якщо вам потрібно виміряти час виконання окремих функцій або невеликих блоків коду.
Використовуйте time, якщо вам потрібно виміряти загальний час виконання більшої програми або складнішого алгоритму."""


"""Користувацькі функції def() — це визначені користувачем блоки коду, які можна викликати за допомогою імені функції, 
щоб виконати певну задачу. Функції допомагають робити код більш організованим, модульним і повторно використовуваним. 
"""
# def ім'я_функції(параметри):
#     '''Документація функції'''
#     блок_коду
#     return значення
# print("After me: Hello fellows")

"""Після ключового слова return виконання функції буде завершене"""
# def func():
#     print("Text until return")
#     return "Returned result"
#     print("That instruction never won't be done")
# print(func())

"""Інструкції return може не бути взагалі"""
# def print_ok():
#     print("Message Ok")
# print(print_ok())

"""Об'єднання рядків rows"""
# def merging_lists(row1:str, row2:str) -> str:
#     return row1 + row2
# print(merging_lists('str', 'ing'))

"""Інструкція def створює об'єкт, який має тип function і зберігає посилання на нього в ідентифікаторі. 
Таким чином ми можемо зберегти це посилання в іншій змінній або передати як аргумент в іншу функцію."""

# def sum(x, y):
#     return x + y
# f = sum
# v = f(10, 20)
# print(v)

"""Напишіть функцію use_for_list, яка приймає два аргументи: функцію f і список lst. 
Функція use_for_list повинна повернути новий список, у якому до кожного елементу початкового списку 
застосовано функцію f."""

# def double(x):
#     return x * 2
#
# def use_for_list(func, lst):
#     return [double(element) for element in lst]
#
# list_of_numbers = list(range(1, 11))
# new_list_double_numbers = use_for_list(double, list_of_numbers)
# print(new_list_double_numbers)

"""Using *args and **kwargs Ви також можете використовувати * args (позиційні аргументи) і * * kwargs (аргументи ключових слів) 
для створення функцій зі змінною кількістю параметрів:"""

# def arbitrary_function(required_param, *args, **kwargs): # *args - кортеж; **kwargs - словник
#     print(f"Required parameter: {required_param}")
#     if args:
#         print(f"Additional positional arguments: {args}")
#     if kwargs:
#         print(f"Additional keyword arguments: {kwargs}")

# Function calls with different parameters
# arbitrary_function("Required")                              # Outputs: Required parameter: Required
# arbitrary_function("Required", 1, 2, 3)                      # Outputs: Required parameter: Required
                                                            #         Additional positional arguments: (1, 2, 3)
# arbitrary_function("Required", key1="value1", key2="value2") # Outputs: Required parameter: Required
                                                            #         Additional keyword arguments: {'key1': 'value1', 'key2': 'value2'}

"""Порядок обробки аргументів у Python
При виклику функції аргументи обробляються в такому порядку:

Позиційні аргументи: Аргументи, що передаються в тому ж порядку, в якому вони визначені у функції.
Іменовані аргументи: Аргументи, які передаються у вигляді ключ-значення.
Значення за замовчуванням: Якщо значення для аргументу не передане, використовується значення за замовчуванням, яке було визначене при створенні функції.
*args (позиційні аргументи довільної довжини): Ці аргументи дозволяють передавати змінну кількість позиційних аргументів.
**kwargs (іменовані аргументи довільної довжини): Ці аргументи дозволяють передавати змінну кількість іменованих аргументів.
Приклад з поясненням"""

# def example_function(a, b=2, *args, **kwargs):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")

# Виклики функції з різними аргументами
# example_function(1)                          # a: 1, b: 2, args: (), kwargs: {}
# example_function(1, 3)                       # a: 1, b: 3, args: (), kwargs: {}
# example_function(1, 3, 4, 5)                 # a: 1, b: 3, args: (4, 5), kwargs: {}
# example_function(1, 3, 4, 5, key1="value1")  # a: 1, b: 3, args: (4, 5), kwargs: {'key1': 'value1'}
"""Пояснення коду
Позиційні аргументи (a): Перший аргумент 1 прив'язується до параметра a.
Іменовані аргументи з значенням за замовчуванням (b=2): Другий аргумент 3 (якщо передано) прив'язується до параметра b, 
інакше використовується значення за замовчуванням 2.
*args (позиційні аргументи довільної довжини): Аргументи 4 та 5 прив'язуються до *args у вигляді кортежу (4, 5).
**kwargs (іменовані аргументи довільної довжини): Іменовані аргументи key1="value1" прив'язуються до 
**kwargs у вигляді словника {'key1': 'value1'}."""

"""Правила виклику функцій
Позиційні аргументи повинні передаватися першими.
Іменовані аргументи можуть передаватися в будь-якому порядку, але вони повинні йти після всіх позиційних аргументів.
*args збирає всі додаткові позиційні аргументи, що залишилися.
**kwargs збирає всі додаткові іменовані аргументи, що залишилися.
Приклад з повним набором аргументів"""

# def full_example(a, b=2, c=3, *args, **kwargs):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"c: {c}")
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")

# Виклик функції
# full_example(1, 4, 5, 6, 7, key1="value1", key2="value2")
# a: 1
# b: 4
# c: 5
# args: (6, 7)
# kwargs: {'key1': 'value1', 'key2': 'value2'}
"""Цей порядок аргументів дозволяє гнучко викликати функції з різними наборами параметрів, забезпечуючи зручність і читабельність коду."""

"""Довільна кількість параметрів функції"""
# def summa(*t): # всі позиційні аргументи будуть зібрані в кортеж
#     res = 0
#     for i in t:
#         res += i
#     return res
# print(summa(10, 20, 30))

"""Анонімні функції lambda() в Python часто називають "lambda-функції". Вони корисні для написання коротких, одноразових 
функцій без необхідності давати їм ім'я. В основі лежить ключове слово lambda."""
""" Створення lambda-функції для додавання двох чисел"""
# add = lambda x, y: x + y
# print(add(2, 3))  # Виведе: 5

""" Використання lambda для множення кожного елемента на 2"""
# numbers = [1, 2, 3, 4]
# doubled = map(lambda x: x * 2, numbers)
# print(list(doubled))  # Виведе: [2, 4, 6, 8]

""" Використання lambda для фільтрації парних чисел"""
# numbers = [1, 2, 3, 4, 5, 6]
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))  # Виведе: [2, 4, 6]

# from functools import reduce

""" Використання lambda для обчислення суми елементів списку"""
# numbers = [1, 2, 3, 4]
# total = reduce(lambda x, y: x + y, numbers)
# print(total)  # Виведе: 10

"""Функції-генератори в Python — це функції, які дозволяють створювати ітератори у більш простий і зручний спосіб. 
Вони використовують ключове слово yield замість return для повернення значення. Основна відмінність полягає в тому, 
що функція-генератор запам'ятовує свій стан між викликами і відновлює виконання з того місця, де було викликане yield."""

"""Ключове слово yield: Використовується для повернення значення і зупинки виконання функції. 
При наступному виклику генератора виконання продовжується з місця, де було зупинено.
Ліниве обчислення: Значення генеруються по мірі потреби, що дозволяє економити пам'ять.
Зручність для ітерацій: Ітерації над великими або нескінченними послідовностями стають більш ефективними."""

"""Генератор для створення послідовності чисел:"""
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1

# counter = count_up_to(5)
# for num in counter:
#     print(num)

"""Генератор для обробки файлів построчно:"""

# def read_file_in_chunks(file_name):
#     with open(file_name, 'r') as file:
#         while chunk := file.read(1024):  # Читаємо по 1024 байта
#             yield chunk

# for chunk in read_file_in_chunks('example.txt'):
#     print(chunk)

"""Переваги використання генераторів:
Ефективне використання пам'яті: Генератори створюють значення по мірі необхідності, що дозволяє працювати з великими 
даними,не завантажуючи всю послідовність у пам'ять.
Простота синтаксису: Легше реалізувати ітераційні алгоритми в порівнянні зі звичайними функціями та ітераторами.
Ліниве обчислення: Значення генеруються лише тоді, коли вони необхідні, що може покращити продуктивність."""



"""Декоратори в Python, function decorators — це спеціальні функції, які дозволяють змінювати або розширювати поведінку 
інших функцій або методів. Вони часто використовуються для додавання повторюваних шаблонів, таких як логування, 
контроль доступу, кешування тощо, до функцій без зміни їх коду."""

"""Переваги декораторів:
Повторне використання коду: Декоратори дозволяють багаторазово використовувати один і той же код для розширення функціональності різних функцій.
Зручність: Вони дозволяють змінювати поведінку функцій без зміни їх коду.
Читабельність: Код стає більш структурованим і легко читається."""

"""Основні випадки, де декоратори функцій використовуються найчастіше:
1. Логування та трасування (logging and tracing):
2. Кешування (caching):
3. Перевірка та валідація (validation):
4. Контроль доступу та аутентифікація (access control and authentication):
5. Обробка винятків (exception handling):
6. Мемоізація (memoization):
7. Аналіз продуктивності (performance profiling):
8. Модифікація поведінки функцій (modifying function behavior):"""

# створення функції декоратора
# def my_decorator(func):
#     def wrapper():
#         print("Something is doing before calling the function")
#         func()
#         print("Something is doing after calling the function")
#     return wrapper

# створення функції, яку будемо декорувати
# def say_hello():
#     print("Hi!")

# застосовуєм декоратор до функції
# decorated_function = my_decorator(say_hello)

# Тепер, коли ви викличете decorated_function, виконаються додаткові дії до і після виклику оригінальної функції say_hello:

# decorated_function()


"""Декоратор з аргументами"""
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is doing before calling the function")
#         result = func(*args, **kwargs)
#         print("Something is doing after calling the function")
#         return result
#     return wrapper

# @my_decorator
# def say_hi(name):
#     print(f'Hi, {name}!')
# say_hi('Jman')

"""Завдання: Декоратор для логування аргументів та результату функції"""

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Call function {func.__name__} with arguments {args} and {kwargs}')
#         result = func(*args, **kwargs)
#         print(f'Function {func.__name__} return {result}')
#         return result
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# result = add(5, 3)
# print(f'Result of add is : {result}')
#
# @log_decorator
# def multiply(x, y):
#     return x * y
#
# result = multiply(4, 7)
# print(f"Result of multiply is {result}")

"""Завдання: Перевірка параметрів аргументів функції"""

# def validate_arguments(func):
#     def wrapper(a, b):
#         if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#             raise TypeError("Arguments must be numeric")
#         if b == 0:
#             raise ValueError("Second argument cannot be zero")
#         return func(a, b)
#     return wrapper
# @validate_arguments
# def divide(a, b):
#     return a / b
# # Приклади викликів функції divide з різними аргументами:
# try:
#     result = divide(10, 2)
#     print("Result of division:", result)
#
#     result = divide("10", 2)  # Це викличе помилку TypeError
#     print("Result of division:", result)
#
#     result = divide(10, 0)  # Це викличе помилку ValueError
#     print("Result of division:", result)
#
# except TypeError as e:
#     print("Error:", e)
# except ValueError as e:
#     print("Error:", e)

"""Контроль доступу є важливою частиною багатьох веб-додатків, розглянемо приклад, де ми створимо декоратор для 
перевірки ролі користувача перед виконанням функції. У цьому прикладі ми припустимо, що у нас є система з двома ролями: 
"admin" і "user"."""


# def check_role(required_role):
#     def decorator(func):
#         def wrapper(user, *args, **kwargs):
#             if 'role' not in user or user['role'] != required_role:
#                 raise PermissionError(f"User does not have the required role: {required_role}")
#             return func(user, *args, **kwargs)
#
#         return wrapper
#
#     return decorator


# Приклад функції, доступної лише для адміністраторів
# @check_role('admin')
# def delete_user(user, user_id):
#     print(f"User {user_id} has been deleted by {user['name']}")


# Приклад функції, доступної лише для звичайних користувачів
# @check_role('user')
# def view_profile(user):
#     print(f"User {user['name']} is viewing their profile")


# Приклади викликів функцій з різними ролями користувачів:
# admin_user = {'name': 'Alice', 'role': 'admin'}
# regular_user = {'name': 'Bob', 'role': 'user'}

# try:
#     delete_user(admin_user, 123)  # Це спрацює
#     delete_user(regular_user, 123)  # Це викличе помилку PermissionError

#     view_profile(regular_user)  # Це спрацює
#     view_profile(admin_user)  # Це викличе помилку PermissionError
#
# except PermissionError as e:
#     print("Access denied:", e)

"""У цьому прикладі:

check_role – це декоратор, який приймає роль, необхідну для доступу до функції.
decorator – це функція, яка обгортає оригінальну функцію і перевіряє роль користувача перед її виконанням.
wrapper – перевіряє, чи має користувач необхідну роль. Якщо ні, викидає виняток PermissionError.
delete_user – функція, доступна лише для користувачів з роллю "admin".
view_profile – функція, доступна лише для користувачів з роллю "user".
Цей приклад демонструє, як за допомогою декораторів можна реалізувати контроль доступу до функцій залежно від ролі користувача."""

"""Recursion Рекурсія — це метод програмування, в якому функція викликає сама себе для розв'язання задачі. 
Важливою частиною рекурсії є наявність базового випадку, який зупиняє рекурсивні виклики, запобігаючи зацикленню."""

"""Факторіал числа"""

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Виведе: 120

"""Обхід файлів у директорії"""

# import os
#
# def list_files(directory):
#     for entry in os.listdir(directory):
#         path = os.path.join(directory, entry)
#         if os.path.isdir(path):
#             list_files(path)  # Рекурсивний виклик для піддиректорії
#         else:
#             print(path)  # Обробка файлу
#
# list_files('/path/to/directory')

"""В Python змінні можуть бути глобальними та локальними, залежно від того, де вони оголошені та де використовуються. 
Розглянемо ці поняття докладніше."""

# def my_function():
#     x = 10  # Локальна змінна
#     print("Inside the function, x =", x)

# my_function()
# print("Outside the function, x =", x)  # Це викличе помилку, оскільки x не існує поза функцією

# глобальна змінна
# x = 20

# def print_global_value():
#     print(x)

# print_global_value()

""" Пайтон шукає змінні по порядку з LEGB
L - локальні змінні, E - енклоуз, G - глобальні, B - білд-ін"""

"""Локальна область видимості (Local Scope): Змінні, визначені всередині функції. Вони доступні тільки в межах цієї функції.

Область замикання (Enclosing Scope): Застосовується до вкладених функцій. Це область видимості зовнішньої функції, 
яка охоплює внутрішню функцію.

Глобальна область видимості (Global Scope): Змінні, визначені на верхньому рівні модуля. Вони доступні у всьому модулі.

Вбудована область видимості (Built-in Scope): Вбудовані функції та об'єкти, які завжди доступні в Python."""
# def outer_function():
#     x = 20  # Змінна в області замикання

    # def inner_function():
    #     print("Inside inner_function, x =", x)  # Доступ до змінної з області замикання (Enclosing Scope)

    # inner_function()

# outer_function()

"""Вбудовані змінні (built-in variables) в Python — це змінні або константи, які доступні в будь-якому контексті 
виконання програми, оскільки вони вже визначені у мові Python. Ось кілька прикладів вбудованих змінних:"""

# print(__name__)  # Виведе "__main__" у головному модулі

# print(dir(__builtins__))  # Виведе список всіх вбудованих імен

# print(__package__)  # Виведе ім'я пакету поточного модуля

"""Вкладена функція в Python - це функція, яка визначена всередині іншої функції. 
Вона може бути використана лише всередині цієї зовнішньої функції і зазвичай використовується для організації логіки, 
яка специфічна лише для цієї частини програми."""

# def outer_function():
#     print("Це зовнішня функція")

    # def nested_function():
    #     print("Це вкладена функція")

    # nested_function()
# Виклик зовнішньої функції
# outer_function()


# def outer_function():
#     x = 10
#     def inner_function():
#         nonlocal x        # змінюємо х зовнішньої функції
#         x += 5
#     inner_function()
#     return x
# print(outer_function())  # Виведе: 15

"""# Приклад 1: Вкладена функція, яка використовує змінні зовнішньої функції
def outer_function():
    x = 10
    
    def inner_function():
        y = 5
        result = x + y
        return result
    
    return inner_function()

print(outer_function())  # Спробуйте зрозуміти, як працюють змінні x і y

# Приклад 2: Вкладеність функцій
def outer_function():
    def inner_function():
        print("Це вкладена функція")
    
    print("Це зовнішня функція")
    inner_function()

outer_function()  # Спостерігайте за порядком викликів функцій і їх відповіддю

# Приклад 3: Використання nonlocal для зміни змінної зовнішньої функції
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
    
    inner_function()
    print(x)  # Спробуйте передбачити, що буде виведено

outer_function()"""

"""Напишіть програму, яка обчислює суму елементів списку за допомогою вкладених функцій. 
Мета цього завдання - створити вкладену функцію для обробки списку та виводу результату."""

# def calculate_sum(numbers: list) ->int: # numbers аргумент, який приймається зовні
#     def sum_elements(nums): # nums = numbers
#         result = 0
#         for num in nums:
#             result += num
#         return result
#     return sum_elements(numbers)
# numbers_list = [1, 2, 3, 4, 5]
# print(f"Сума елементів списку {numbers_list} дорівнює {calculate_sum(numbers_list)}")

"""Напишіть програму, яка реалізує функцію, що повертає іншу функцію, яка підраховує кількість своїх викликів. 
Це приклад використання вкладених функцій та замикань."""
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# counter1 = make_counter()
# print(counter1()) # Виведе 1
# print(counter1()) # Виведе 2
# print(counter1()) # Виведе 3

# counter2 = make_counter()
# print(counter2())  # Виведе 1
# print(counter2())  # Виведе 2

"""Data annotation Функціональна анотація в Python дозволяє додавати метадані до параметрів функції та її повертаного значення. 
Анотації не впливають на виконання коду, але вони можуть бути корисними для документування, типізації і статичного 
аналізу коду."""

# def greet(name: str, age: int) -> str:
#     return f"Hello, {name}. You are {age} years old."

# message = greet("Alice", 30)  # message буде "Hello, Alice. You are 30 years old."

"""Використання анотацій з модулем typing
Модуль typing надає додаткові типи для анотацій:

List: Список значень певного типу.
Dict: Словник з ключами та значеннями певного типу.
Tuple: Кортеж з елементами певних типів.
Union: Комбінація кількох типів.
Optional: Тип, який може бути значенням або None."""

# from typing import List, Dict, Tuple, Union, Optional

# def complex_function(data: List[Union[int, str]], config: Dict[str, Union[str, int]], optional_value: Optional[int]) -> Tuple[int, str]:
#     Приклад обробки
#     count = len(data)
#     summary = ", ".join(map(str, data))
#     return count, summary

# data = [1, "two", 3, "four"]
# config = {"key1": "value1", "key2": 2}
# optional_value = None
# result = complex_function(data, config, optional_value)  # result буде (4, "1, two, 3, four")

"""Доступ до анотацій
Анотації зберігаються в атрибуті __annotations__ функції:"""
# def multiply(x: int, y: int) -> int:
#     return x * y

# print(multiply.__annotations__)
# Виведе: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

"""Moduls Модулі в Пайтоні - це файли з розширенням .py, які містять код на Python. Вони дозволяють структурувати програму, 
розділяючи її на логічні частини, та повторно використовувати код."""

"""Інструкція Import в Python використовується для завантаження модулів у ваш скрипт."""
""" 1.Імпорт усього модуля:"""
# import module_name
"""При цьому ви зможете звертатися до функцій та змінних модуля через префікс module_name."""
# import math
# print(math.sqrt(16))  # Викликає функцію sqrt з модуля math

"""2.Імпорт конкретних функцій або змінних з модуля:"""
# from module_name import function_name, variable_name

"""При цьому ви можете використовувати імпортовані функції або змінні без префіксу."""
# from math import sqrt
# print(sqrt(16))  # Викликає функцію sqrt без префіксу math

"""3.Імпорт з псевдонімом (alias):
Ви можете використовувати псевдонім для модуля або його частини, щоб скоротити запис або уникнути конфліктів імен."""
# import module_name as alias
# import numpy as np
# print(np.array([1, 2, 3]))  # Використання псевдоніму np для numpy

"""4.Імпорт усіх вмісту модуля (не рекомендується):"""

# from module_name import *
"""Це дозволяє імпортувати всі функції та змінні модуля, але може призвести до конфліктів імен і ускладнити відладку."""

# from math import *
# print(sqrt(16))  # Викликає функцію sqrt без префіксу

"""5.Імпорт всередині функцій:
Ви також можете імпортувати модулі всередині функцій. Це корисно, якщо модуль потрібен лише для певної частини коду, що може покращити продуктивність."""
# def my_function():
#     import math
#     print(math.sqrt(16))
# my_function()

"""Імпорт власних модулів:
Якщо ви створили свій модуль, просто збережіть його в тому ж каталозі, що й ваш скрипт, або у каталозі, який є у sys.path."""
# import my_module
# print(my_module.greet("Alice"))

"""функція getattr() - отримання атрибуту модуля"""

"""Щоб отримати значення атрибута модуля за допомогою функції getattr(), можна скористатися наступною процедурою:

Імпортуйте модуль.
Використовуйте функцію getattr(), щоб отримати значення атрибута.
Приклад
Припустимо, у нас є модуль my_module.py з наступним вмістом:"""

# my_module.py
# my_variable = 42
# def my_function():
#     return "Hello from my_function!"
"""Тепер, в іншому скрипті або в інтерактивній оболонці Python, ми можемо отримати значення атрибута цього модуля так:"""

# import my_module

# Отримання значення змінної my_variable
# variable_value = getattr(my_module, 'my_variable')
# print(variable_value)  # Виведе: 42

# Виклик функції my_function
# function_value = getattr(my_module, 'my_function')()
# print(function_value)  # Виведе: Hello from my_function!

# Використання значення за замовчуванням для неіснуючого атрибута
# non_existent = getattr(my_module, 'non_existent', 'Default Value')
# print(non_existent)  # Виведе: Default Value
"""Пояснення
Імпортування модуля: Ми імпортуємо модуль за допомогою import my_module.
Отримання значення атрибута: Використовуємо getattr(my_module, 'my_variable') для отримання значення змінної my_variable.
Виклик функції: Використовуємо getattr(my_module, 'my_function') для отримання функції my_function і викликаємо її.
Значення за замовчуванням: Використовуємо третій параметр getattr() для встановлення значення за замовчуванням, якщо атрибут не існує.
Цей підхід є універсальним і може бути використаний для отримання значень будь-яких атрибутів модулів, включаючи змінні, функції, класи тощо."""

"""Функція hasattr() в Python використовується для перевірки, чи існує атрибут з певним ім'ям у об'єкта. Вона повертає True, 
якщо атрибут існує, і False в іншому випадку. Це особливо корисно при динамічному доступі до атрибутів об'єктів, 
оскільки дозволяє уникнути винятків AttributeError"""
#Синтаксис
# hasattr(object, name)

"""Параметри
object: Об'єкт, в якому перевіряється наявність атрибута.
name: Ім'я атрибута у вигляді рядка.
Повертає
True, якщо атрибут з заданим ім'ям існує в об'єкті.
False, якщо атрибут не існує."""

# import math

# Перевірка наявності атрибута 'pi' у модулі 'math'
# print(hasattr(math, 'pi'))  # Виведе: True

# Перевірка наявності неіснуючого атрибута 'non_existent' у модулі 'math'
# print(hasattr(math, 'non_existent'))  # Виведе: False

"""Використання разом з getattr()"""

# class MyClass:
#     def __init__(self):
#         self.value = 42
#
#     def greet(self):
#         return "Hello!"
#
# obj = MyClass()
#
# # Перевірка наявності атрибута перед отриманням його значення
# if hasattr(obj, 'value'):
#     value = getattr(obj, 'value')
#     print(value)  # Виведе: 42
#
# # Перевірка наявності методу перед викликом
# if hasattr(obj, 'greet'):
#     greet_method = getattr(obj, 'greet')
#     print(greet_method())  # Виведе: Hello!

"""Уникнення винятків: Дозволяє безпечно перевірити наявність атрибута перед доступом до нього, що запобігає виникненню AttributeError.
Динамічність: Особливо корисно при роботі з динамічними або користувацькими об'єктами, де структура може бути невідомою заздалегідь."""

"""Псевдоніми в Пайтоні У Python псевдоніми (або аліаси) дозволяють використовувати інше ім'я для модулів, функцій або змінних. 
Це може бути корисно для скорочення довгих імен або уникнення конфліктів імен. Ось як можна створювати псевдоніми:"""

# import module_name as alias

# import numpy as np
# import pandas as pd

# Використання псевдоніму np для доступу до функцій модуля numpy
# array = np.array([1, 2, 3])
# print(array)

# Використання псевдоніму pd для доступу до функцій модуля pandas
# data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(data)

# from math import sqrt as square_root

# Використання псевдоніму square_root для функції sqrt
# result = square_root(16)
# print(result)  # Виведе: 4.0

# class MyClass:
#     def greet(self):
#         return "Hello!"

# Створення псевдоніму для методу greet
# MyClassAlias = MyClass

# obj = MyClassAlias()
# print(obj.greet())  # Виведе: Hello!

"""Інструкція from ... import ... в Python дозволяє імпортувати певні атрибути (функції, класи, змінні) з модуля без 
імпортування всього модуля. Це може бути корисним для зменшення обсягу коду і підвищення читабельності, особливо коли 
вам потрібні лише кілька елементів з великого модуля."""

# from math import sqrt, sin, cos

# Використання імпортованих функцій
# print(sqrt(16))  # Виведе: 4.0
# print(sin(0))    # Виведе: 0.0
# print(cos(0))    # Виведе: 1.0

"""Іноді можна імпортувати всі атрибути модуля за допомогою зірочки (*). Це не рекомендується робити часто, 
оскільки може призвести до конфліктів імен."""

# from math import *

# Використання функцій без префіксу модуля
# print(sqrt(16))  # Виведе: 4.0
# print(sin(0))    # Виведе: 0.0
# print(cos(0))    # Виведе: 1.0

"""Імпорт з власного модуля
Припустимо, у вас є файл my_module.py з наступним вмістом:"""

# my_module.py
# def greet(name):
#     return f"Hello, {name}!"

# PI = 3.14159
# Тепер ви можете імпортувати функцію і змінну з цього модуля:

# from my_module import greet, PI

# Використання імпортованих атрибутів
# print(greet("Alice"))  # Виведе: Hello, Alice!
# print(PI)  # Виведе: 3.14159


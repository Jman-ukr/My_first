"""Метод format() дозволяє форматувати рядки, вставляючи в них змінні або інші значення. Він замінює фігурні дужки {} у
рядку на значення, передані в метод format()."""
# Синтаксис
# "текст {ключ1} текст {ключ2}".format(ключ1=значення1, ключ2=значення2)

""" Вирівнювання:"""
""""< : вирівнювання вліво (за замовчуванням)
> : вирівнювання вправо
^ : вирівнювання по центру"""

# print("{:<10}".format("ліво"))   # Вирівнювання вліво
# print("{:>10}".format("право"))  # Вирівнювання вправо
# print("{:^10}".format("центр"))  # Вирівнювання по центру

"""Заповнення:
Символ, що використовується для заповнення порожніх місць"""

# print("{:*<10}".format("ліво"))   # Заповнення зліва '*'
# print("{:*>10}".format("право"))  # Заповнення справа '*'
# print("{:*^10}".format("центр"))  # Заповнення по центру '*'

"""Додаткові можливості
Метод format() також підтримує доступ до елементів списків та словників:"""

# data = {"ім'я": "Іван", "вік": 30}
# print("Ім'я: {ім'я}, Вік: {вік}".format(**data))
# Виведе: Ім'я: Іван, Вік: 30

# my_list = [1, 2, 3]
# print("Перший елемент: {0[0]}, Другий елемент: {0[1]}".format(my_list))
# Виведе: Перший елемент: 1, Другий елемент: 2

"""Напиши програму, яка виводить привітання з ім'ям користувача у верхньому регістрі, використовуючи метод format(). 
Ім'я повинно зчитуватися з консолі."""

# def greeting_user():
#     name = input("Write your name dude: ")
#     print("Hi, {}!".format(name).upper())
# greeting_user()

"""Напиши програму, яка приймає від користувача число і виводить його з двома знаками після коми."""

# def two_num():
#     num = float(input("Write a float number dude: "))
#     print("Number is: {:.2f}".format(num))
# two_num()

"""Напиши програму, яка виводить три рядки тексту з різними варіантами вирівнювання: лівим, правим та центруванням. 
Текст повинен бути довжиною 10 символів."""

# def leveling_text():
#     text = "I am the one!"
#     print("Ліве вирівнювання: {:<30}".format(text))
#     print("Праве вирівнювання: {:>30}".format(text))
#     print("Центрування: {:^30}".format(text))
# leveling_text()

"""Напиши програму, яка приймає від користувача ціле число і виводить його в десятковій, шістнадцятковій та двійковій 
системах числення."""

# def different_sys():
#     num = int(input("Write a number dude: "))
#     print("Hexadecimal number is: {:x}".format(num)) # Шістнадцяткове число
#     print("Binary number is: {:b}".format(num)) # двійкове число
#     print("Decimal number is: {:d}".format(num)) # десяткове число
# different_sys()

"""Напиши програму, яка виводить рядок "Python" з різними варіантами заповнення: зліва нулями, справа пробілами 
та символами "*"."""

# def filling():
#     text = "Python"
#     print("Filling by zeroes: {:05}".format(27)) # Для заповнення нулями слід використовувати числа, а не рядки.
#     print("Filling by symbols *: {:*^10}".format(text)) # заповнюється символами * до ширини 10 символів.
# filling()

"""Напиши програму, яка приймає від користувача словник з даними про людину (ім'я, вік, місто) і виводить ці дані, 
використовуючи метод format()."""

# def dictionary_format():
#     my_dict = {"name": "Jman", "Age": 44, "City": "Irpin"}
#     print("Name: {name}, Age: {Age}, City: {City}".format(**my_dict))
# dictionary_format()

"""Напиши програму, яка приймає від користувача список з трьох чисел і виводить ці числа у форматі 
"Число 1: x, Число 2: y, Число 3: z"."""
# def list_of_three_numbers():
#     list_num = list(input("Write three numbers dude: ").split())
#     print("First num: {0[0]}, Second num: {0[1]}, Third num: {0[2]}".format(list_num))
# list_of_three_numbers()

"""Напиши програму, яка приймає від користувача два числа і виводить їх у форматі "Перше число: x, Друге число: y", 
використовуючи індекси у методі format()."""
# def indexes():
#     num1 = int(input("Write first number:"))
#     num2 = int(input("Write second number:"))
#     print("first number: {0}, second number: {1}".format(num1,num2))
# indexes()

"""Функції та методи для роботи з рядками str()"""

"""Напишіть програму, яка зчитує рядок від користувача і виводить його довжину."""
# def len_str():
#     my_str = input("Write string dude: ")
#     print(len(my_str))
# len_str()

"""Напишіть програму, яка зчитує два рядки від користувача і об'єднує їх у один рядок."""
# def concat_str():
#     first_str = input("Write first string: ")
#     second_str = input("Write second string: ")
#     conc_str = first_str + " " + second_str
#     print(conc_str)
# concat_str()

"""Напишіть програму, яка зчитує рядок від користувача і перевіряє, чи складається він лише з букв."""

# V1
# def is_alpha():
#     my_str = input("Write string:")
#     for char in my_str.lower():
#         if not char.isalpha():
#             print("False")
#             return
#     print("True")
# is_alpha()

# V2
# def is_alpha():
#     my_str = input("Write string:")
#     if my_str.isalpha():
#         print("True")
#     else:
#         print("False")
#
# is_alpha()

"""Напишіть програму, яка зчитує рядок від користувача і замінює в ньому всі пробіли на символ підкреслення."""

# def resub():
#     my_str = input("Write string as always dude):")
#     new_str = my_str.replace(" ", "_")
#     print(new_str)
# resub()

"""Напишіть програму, яка зчитує список слів, розділених комами, від користувача і виводить їх у вигляді списку."""

# def split_str():
#     my_str = input("As always dude, plus including coma:")
#     new_split_str = my_str.split(", ")
#     print(new_split_str)
# split_str()

"""кортежі tuple(), imutable, можуть містити будь які типи даних як і списки"""
# my_tuple = ('Jman', 44, 'Irpin')
# print(my_tuple[0], my_tuple[1], my_tuple[2], sep='|', end=" ")

# def print_values(my_tuple):
#     for value in my_tuple:
#         print(value)
#
# # Створення кортежу
# fruits = ('apple', 'banana', 'cherry')
#
# # Виклик функції з кортежем у якості аргументу
# print_values(fruits)
"""Розпакування кортежу"""
# def print_fruit(a, b, c):
#     print("First fruit: {}".format(a))
#     print(f"Second fruit: {b}")
#     print(f"Third fruit: {c}")

# Створення кортежу
# fruits = ('apple', 'banana', 'cherry')
#
# # Розпакування кортежу і передача елементів як аргументів
# print_fruit(*fruits)

"""Використання кортежів у функціях"""
# def calculate_stats(numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     avg_num = sum(numbers) / len(numbers)
#     return min_num, max_num, avg_num
#
# # Створення кортежу з числами
# data = (10, 25, 14, 8, 32)
#
# # Виклик функції і отримання результатів у вигляді кортежу
# stats = calculate_stats(data)
# print("Min:", stats[0])
# print("Max:", stats[1])
# print("Average:", stats[2])

"""Множини set(), невпорядковані колекції унікальних елементів. 
Можуть містити тільки числа, рядки, булеві значення, кортежі, None, Frozenset, хешовані об'єкти"""

"""словники dictionaries"""

"""Напиши програму, яка аналізує даний текст і підраховує частоту кожного слова. Програма має вивести словник, 
де ключами є слова, а значеннями – їх частота в тексті."""

# V1
# text = """
# This is a simple text example. This example is meant to be simple, so we can analyze it easily.
# Let's see how many times each word appears in this text.
# """
# new_text = text.replace(".", "").replace(",", "").lower()
# words = new_text.split()
# dict_count = {}
# for word in words:
#     if word in dict_count:
#         dict_count[word] += 1
#     else:
#         dict_count[word] = 1
# print(dict_count)

# V2 За допомогою модуля string

# import string
#
# text = """
# This is a simple text example. This example is meant to be simple, so we can analyze it easily.
# Let's see how many times each word appears in this text.
# """
#
# # Видалення пунктуації та приведення тексту до нижнього регістру
# text = text.translate(str.maketrans('', '', string.punctuation)).lower()
#
# # Розбиття тексту на слова
# words = text.split()
#
# # Підрахунок частоти кожного слова
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(word_count)

"""Напиши функцію, яка приймає два словники та об'єднує їх. Якщо ключі в обох словниках однакові, значення мають бути додані. 
Якщо ключ присутній лише в одному з словників, його значення просто додається в результуючий словник."""
# def merge_dictionaries(dict1, dict2):
#     merged_dict = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged_dict:
#             merged_dict[key] += value
#         else:
#             merged_dict[key] = value
#     return merged_dict
#
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 25, 'c': 35, 'd': 45}
#
# merged_dict = merge_dictionaries(dict1, dict2)
# print(merged_dict)

"""Уяви, що у тебе є словник, де ключами є імена студентів, а значеннями – списки їх оцінок. Напиши функцію, 
яка перетворює цей словник у словник, де ключами є оцінки, а значеннями – списки студентів, які отримали цю оцінку."""
# def transform_grades(students_grades):
#     grades_students = {}
#     for student, grades in students_grades.items():
#         for grade in grades:
#             if grade not in grades_students:
#                 grades_students[grade] = []
#             grades_students[grade].append(student)
#     return grades_students
#
# students_grades = {
#     'Alice': [85, 90, 78],
#     'Bob': [90, 88, 92],
#     'Charlie': [78, 85, 85],
# }
#
# result = transform_grades(students_grades)
# print(result)

"""Напиши функцію, яка приймає список чисел і повертає всі можливі пари чисел з цього списку."""
# import itertools
#
# def find_pairs(numbers):
#     pairs = list(itertools.combinations(numbers, 2))
#     return pairs
#
# numbers = [1, 2, 3, 4]
# result = find_pairs(numbers)
# print(result)  # Виведе [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

"""Напиши функцію, яка приймає матрицю і повертає її транспоновану версію."""
# def transpose_matrix(matrix):
#     transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             transposed[j][i] = matrix[i][j]
#     return transposed
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# result = transpose_matrix(matrix)
# print(result)  # Виведе [[1, 4], [2, 5], [3, 6]]

"""Як створити словник, де ключами є числа від 1 до 5, а значеннями - квадрати цих чисел?"""
# my_dict = {}
# for i in range(1, 6):
#     my_dict[i] = i ** 2
# for key, value in my_dict.items():
#     print(key, value)
"""Як видалити всі пари ключ-значення зі словника inventory, які мають значення менше 10?"""
# filtered_inventory = {key: value for key, value in my_dict.items() if value >= 10}
# print(filtered_inventory)
"""Створіть словник чисел і використайте анонімну функцію для відфільтрування лише тих значень,
які задовольняють певну умову (наприклад, парні числа)."""
# start = 1
# end = 20
# my_dict = {num: num for num in range(start, end + 1)}
# print(my_dict)
# even_num_dict = filter(lambda x: x % 2 == 0, my_dict.values())
# print(list(even_num_dict))

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

"""Спробуйте написати функцію, яка приймає вкладений список з різними типами даних і повертає новий список, 
де всі числові значення подвоєні, а всі інші елементи залишаються без змін."""
# def double_numbers(nested_list):
#     result = []
#     for sublist in nested_list:
#         new_sublist = []
#         for item in sublist:
#             if isinstance(item, (int, float)):
#                 new_sublist.append(item * 2)
#             else:
#                 new_sublist.append(item)
#         result.append(new_sublist)
#     return result
#
# nested_list = [
#             [1, 2, 3],
#             ['a', 'b', 'c'],
#             [True, False, None],
#             [4.5, 5.6, 6.7]
#         ]
# new_list = double_numbers(nested_list)
# for sublist in new_list:
#     print(sublist)

"""Створи 1D масив NumPy з чисел від 0 до 9."""
# import numpy as np
# my_list = [n for n in range(0, 11)]
# np_array = np.array(my_list)
# array = np.arange(11)
# print(np_array, end=" ")
# print()
# print("Array: \n", array)


"""Створи 2D масив NumPy з будь-яких чисел."""
# nested_list = [
#             [1, 2, 3],
#             ['a', 'b', 'c'],
#             [True, False, None],
#             [4.5, 5.6, 6.7]
#         ]
# np_array_2 = np.array(nested_list)
# first_slice = np_array_2[0][:2]
# print(first_slice)

"""Витягти всі email адреси з тексту"""
# import re
#
# text = "Please contact us at support@example.com or sales@example.co.uk for more information."
# pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
#
# # Знайти всі email адреси
# matches = pattern.findall(text)
# print(matches)

"""Замінити всі цифри на символ "#"""
# import re
#
# text = "My phone number is 12345 and my zip code is 67890."
# pattern = re.compile(r"\d")
#
# # Замінити всі цифри на "#"
# result = pattern.sub("#", text)
# print(result)

"""Перевірити, чи містить рядок IP-адресу"""
# import re
#
# text = "The server is located at 192.168.1.1."
# pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
#
# # Шукати IP-адресу
# match = pattern.search(text)
# if match:
#     print(f"IP-адреса знайдена: {match.group()}")
# else:
#     print("IP-адресу не знайдено")

"""Чудово! Давай створимо клас, який моделює просту систему керування бібліотекою. У нас буде клас Book, який представляє книгу, і клас Library, який управляє колекцією книг.

Вимоги:
Клас Book:
Атрибути: title, author, year.
Метод display_info(), який виводить інформацію про книгу.

Клас Library:
Атрибут: список книг.
Метод add_book(book), який додає книгу до бібліотеки.
Метод remove_book(title), який видаляє книгу з бібліотеки за назвою.
Метод display_books(), який виводить інформацію про всі книги в бібліотеці."""

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def show_info_book(self):
#         print(f'Title:{self.title}, Author:{self.author}, Year:{self.year}')
#
# class Library:
#     def __init__(self):
#         self.book_list = []

#     def add_book(self, book):
#         self.book_list.append(book)
#
#     def remove_book(self, title):
#         for book in self.book_list:
#             if book.title == title:
#                 self.book_list.remove(book)
#                 break

# # або book_list = [book for book in self.book_list if book.title != title]

#     def display_books(self):
#         if not self.book_list:
#             print("No books in the library.")
#         else:
#             for book in self.book_list:
#                 book.show_info_book()
#
# # Створення об'єктів класу Book
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book3 = Book("1984", "George Orwell", 1949)
#
# # Створення об'єкту класу Library
# library = Library()
#
# # Додавання книг до бібліотеки
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Виведення всіх книг у бібліотеці
# print("Books in the library:")
# library.display_books()
#
# # Видалення однієї книги
# library.remove_book("To Kill a Mockingbird")
#
# # Виведення всіх книг у бібліотеці після видалення
# print("\nBooks in the library after removal:")
# library.display_books()

"""--Список використовується, коли важливий порядок елементів і можливість дублювання.
   --Словник використовується, коли швидко потрібен доступ до об'єктів за ключем.
   --Кортеж використовується, коли потрібна незмінювана послідовність об'єктів.
   --Множина використовується, коли потрібна унікальність елементів і порядок не має значення."""

""""""


    # def __str__(self):
    #     return f"{self.title} by {self.artist}, released in {self.year}"

# class MusicLibrary:
#     def __init__(self):
#         self.albums = {}  # словник для зберігання альбомів
#
#     def add_album(self, title, artist, year):
#         self.albums[title] = {'artist': artist, 'year': year}  # додавання альбому до словника
#
#     def remove_album(self, title):
#         if title in self.albums:
#             del self.albums[title]  # видалення альбому за назвою
#
#     def find_album(self, title):
#         return self.albums.get(title, None)  # повертає альбом або None, якщо альбом не знайдено
#
#     def display_albums(self):
#         for title, info in self.albums.items():
#             print(f"{title} by {info['artist']}, released in {info['year']}")

# Створимо музичну бібліотеку і додамо альбоми
# library = MusicLibrary()
# library.add_album("Abbey Road", "The Beatles", 1969)
# library.add_album("The Dark Side of the Moon", "Pink Floyd", 1973)
# library.add_album("Thriller", "Michael Jackson", 1982)

# Відобразимо всі альбоми
# print("All albums:")
# library.display_albums()

# Знайдемо альбом за назвою
# print("\nFinding 'Thriller':")
# found_album = library.find_album("Thriller")
# if found_album:
#     artist = found_album['artist']
#     year = found_album['year']
#     print(f"Thriller by {artist}, released in {year}")
# else:
#     print("Album not found")
#
# # Видалимо альбом за назвою
# print("\nRemoving 'Abbey Road'")
# library.remove_album("Abbey Road")
#
# # Відобразимо всі альбоми після видалення
# print("\nAll albums after removal:")
# library.display_albums()

"""Напиши свій клас, використовуючи ці поняття. Наприклад, створити клас Animal з атрибутами species, name, age та 
методом speak, який буде повертати рядок типу "{name} makes a sound"."""
# class Animal:
#     def __init__(self, species, name, age):
#         self.species = species
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f'{self.name} makes a sound')
#
# animal1 = Animal('Cat', 'Bazya', '5')
# animal1.speak()

"""Створити базовий клас Vehicle з атрибутами make, model та методом start().
Створити похідний клас Car, який успадковує від Vehicle і додає атрибут number_of_doors.
Перевизначити метод start() у класі Car, щоб він виводив повідомлення, що машина запускається.
Створити ще один похідний клас Bike, який успадковує від Vehicle і додає атрибут type_of_handlebar.
Перевизначити метод start() у класі Bike, щоб він виводив повідомлення, що велосипед запускається."""

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def start(self):
#         pass
# class Car(Vehicle):
#     def __init__(self, make, model, number_of_doors):
#         super().__init__(make, model)
#         self.number_of_doors = number_of_doors
#
#     def start(self):
#         return f"Car {self.model} in motion"
# class Bike(Vehicle):
#     def __init__(self, make, model, type_of_handlebar):
#         super().__init__(make, model)
#         self.type_of_handlebar = type_of_handlebar
#
#     def start(self):
#         return f"Bike {self.model} in motion"
# car1 = Car(make=1998, model='Tesla', number_of_doors=4)
# bike1 = Bike(make=2003, model='Hanson', type_of_handlebar='Right')
# print(car1.start())
# print(bike1.start())

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    def start_engine(self):
        return f"Engine {self.engine_type} is starting."
class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels
    def start_moving(self):
        return f"Vehicle with {self.number_of_wheels} wheels is moving."
class Car(Engine, Wheels):
    def __init__(self, brand, model, engine_type, number_of_wheels):
        super().__init__(engine_type)
        Wheels.__init__(self, number_of_wheels)
        self.brand = brand
        self.model = model
    def star(self):
        engine_start = self.start_engine()
        moving = self.start_moving()
        return f"{self.brand} {self.model}: {engine_start} {moving}"
car = Car(brand="Tesla", model='X', engine_type='electric', number_of_wheels=4)
print(car.star())
print(Car.__mro__)





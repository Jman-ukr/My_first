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
#     my_str = input("As always dude plus including coma:")
#     new_split_str = my_str.split(", ")
#     print(new_split_str)
# split_str()


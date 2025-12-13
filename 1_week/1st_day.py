"""# Day 1 — Python basics

# 1. Переменные
age = 20
height = 180.5
name = "Alex"
is_student = True

print(age, height, name, is_student)

# 2. Простые вычисления
a = 10
b = 3

print("Sum:", a + b)
print("Difference:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer division:", a // b)
print("Remainder:", a % b)

# 3. f-string
print(f"My name is {name}, I am {age} years old")

# 4. Ввод данных
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, next year you will be {user_age + 1}")"""
"""Посчитать площадь круга (радиус = 7)

Перевести минуты в часы и минуты

Найти среднее из 3 чисел

Вывести своё имя 5 раз

Поменять местами a и b"""
# radius = float(input("Enter a radius: "))
# area = (radius ** 2) * 3.14159
# print(f"The area is {area:.2f}")

# seconds = 7322
# hours = seconds // 3600
# print(hours)
# rem_seconds = seconds % 3600
# print(rem_seconds)
# minutes = rem_seconds // 60
# rem_seconds = rem_seconds % 60
# print()


a = int(input("First digit:"))
b = int(input("Second digit:"))
c = int(input("Third digit:"))
average = float((a+b+c)/ 3)
print(f'Average is {average:.2f}')
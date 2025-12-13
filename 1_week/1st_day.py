# Day 1 — Python basics

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

print(f"Hello {user_name}, next year you will be {user_age + 1}")

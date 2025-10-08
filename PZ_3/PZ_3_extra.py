# 1) Произведение чисел
a = input("Введите первое число: ")
b = input("Введите второе число: ")

while type(a) != int:
    try: a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

while type(b) != int:
    try: b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

p = a * b
result = p * 8 if p < 0 else p * 1.5
print(f"Результат: {result}")

# 2) Четность числа
num = input("Введите число: ")
while type(num) != int:
    try: num = int(num)
    except ValueError:
        print("Неправильно ввели!")
        num = input("Введите число: ")

result = num / 4 if num % 2 == 0 else num * 5
print(f"Результат: {result}")

# 3) Двухзначное число
num = input("Введите двухзначное число: ")
while type(num) != int:
    try: num = int(num)
    except ValueError:
        print("Неправильно ввели!")
        num = input("Введите двухзначное число: ")

s = num // 10 + num % 10
result = num + 2 if s % 2 == 0 else num - 2
print(f"Результат: {result}")

# 4) Положительное число
num = input("Введите число: ")
while type(num) != int:
    try: num = int(num)
    except ValueError:
        print("Неправильно ввели!")
        num = input("Введите число: ")

result = num + 20 if num > 0 else num - 5
print(f"Результат: {result}")

# 5) Сумма кратна 5
a = input("Введите первое число: ")
b = input("Введите второе число: ")

while type(a) != int:
    try: a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

while type(b) != int:
    try: b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

s = a + b
result = s + 1 if s % 5 == 0 else s - 2
print(f"Результат: {result}")
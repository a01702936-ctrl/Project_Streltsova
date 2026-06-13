# 2. В матрице найти минимальный элемент в предпоследней строке.

from random import randint
from functools import reduce

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[randint(-20, 30) for j in range(cols)] for i in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

if rows >= 2:
    a = matrix[-2]
    minimum = reduce(lambda a, b: a if a < b else b, a)
    print(f"Минимум в предпоследней строке: {minimum}")
else:
    print("Нет предпоследней строки")
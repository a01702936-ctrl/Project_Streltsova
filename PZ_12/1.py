#Вариант 15.
# 1. В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

from random import randint

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[randint(-20, 30) for j in range(cols)] for i in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

sums = list(map(lambda col: sum(col), zip(*matrix)))
print("Суммы столбцов:", sums)

if rows >= 2:
    matrix[1] = sums
    print("Матрица после замены:")
    for row in matrix:
        print(row)
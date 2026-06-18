#Вариант15.
#1.В последовательности на n целых чисел найти и вывести:
# 1). максимальный среди положительных
# 2). минимальный среди отрицательных
# 3). произведение элементов


import random
from functools import reduce

n = int(input("Введите количество чисел: "))

numbers = []
for _ in range(n):
    numbers.append(random.randint(-50, 50))

polozh = [x for x in numbers if x > 0]
max_polozh = max(polozh) if polozh else None

otric = [x for x in numbers if x < 0]
min_otric = min(otric) if otric else None

proizv = reduce(lambda a, b: a * b, numbers)

print("Сгенерированная последовательность:", numbers)
print("Максимальный среди положительных:", max_polozh)
print("Минимальный среди отрицательных:", min_otric)
print("Произведение всех элементов:", proizv)
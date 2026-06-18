import random

numbers = [random.randint(-30, 50) for i in range(10)]

f = open('chisla.txt', 'w', encoding='utf-8')
for x in numbers:
    f.write(str(x) + ' ')
f.close()

f = open('chisla.txt', 'r', encoding='utf-8')
s = f.read()
f.close()

a = [int(x) for x in s.split()]

min_val = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] <= min_val:
        min_val = a[i]
        min_index = i

first = a[0]
a2 = [x * first for x in a]

f = open('result.txt', 'w', encoding='utf-8')
f.write('Исходные данные: ' + s + '\n')
f.write('Количество элементов: ' + str(len(a)) + '\n')
f.write('Индекс последнего минимального элемента: ' + str(min_index) + '\n')
f.write('Умножаем все элементы на первый элемент: ')
for x in a2:
    f.write(str(x) + ' ')
f.close()

print('✅ Готово! Смотри файл result.txt')
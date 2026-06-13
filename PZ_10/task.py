
# Вариант 15.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:


vhod = input("Введите числа через пробел: ")

f = open('chisla.txt', 'w', encoding='UTF-8')
f.write(vhod)
f.close()

f = open('chisla.txt', encoding='UTF-8')
s = f.read()

a = [int(x) for x in s.split()]

min_val = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] <= min_val:
        min_val = a[i]
        min_index = i

first = a[0]
a2 = [x * first for x in a]

f2 = open('result.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ' + s + '\n')
f2.write('Количество элементов: ' + str(len(a)) + '\n')
f2.write('Индекс последнего минимального элемента: ' + str(min_index) + '\n')
f2.write('Умножаем все элементы на первый элемент: ')
for x in a2:
    f2.write(str(x) + ' ')
f2.close()

print('Готово! Смотри файл result.txt')
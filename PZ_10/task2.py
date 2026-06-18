# 2.	Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое, количество букв в нижнем регистре. 
# Сформировать новый файл, 
# в который поместить текст в стихотворной форме предварительно заменив символы нижнего регистра на верхний. 


f = open('PZ_10/text18-15.txt', 'r', encoding='utf-16')
stroki = f.readlines()
f.close()

print('Содержимое файла text18-15.txt:')
print()
for i in stroki:
    print(i, end='')
print()

bukvy = 0
for i in stroki:
    for j in i:
        if j.islower():
            bukvy += 1

print('Количество букв в нижнем регистре:', bukvy)

f2 = open('text18-15_new.txt', 'w', encoding='utf-16')
for i in stroki:
    f2.write(i.upper())
f2.close()

print('Новый файл создан: text18-15_new.txt')
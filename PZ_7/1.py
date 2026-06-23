text = input("Введите строку: ")
count = 0
for i in text:
    if 'a' <= i <= 'z':
        count += 1
    elif 'а' <= i <= 'я' or i == 'ё':
        count += 1
print("Количество строчных латинских и русских букв:", count)
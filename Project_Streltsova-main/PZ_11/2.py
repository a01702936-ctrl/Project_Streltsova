#Вариант15.
#2.Составить генератор (yield), который выводит из строки только буквы.
# Генератор, который выводит только буквы
# Генератор, который выводит только буквы
# Тот же генератор, но с filter и лямбдой
def tolko_bukvy(stroka):
    yield from filter(lambda x: x.isalpha(), stroka)

text = "Привет124!Меня283 зовут Арина230."
print("Исходная строка:", text)

print("Только буквы:", end=" ")
for bukva in tolko_bukvy(text):
    print(bukva, end="")
print()
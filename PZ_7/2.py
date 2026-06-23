text = input("Введите предложение на русском языке: ")
punctuation = ".,!?;:-()\"'«»"
count = 0
for i in text:
    if i in punctuation:
        count += 1
print("Количество знаков препинания:", count)
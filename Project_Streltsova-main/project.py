number = int(input("Введите трехзначное число: "))
units = (number //100) % 10
tens_hundreds = (number //10) % 10
print(f"Полученные цифры: {units} and {tens_hundreds}")
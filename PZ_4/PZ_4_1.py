#Вариант15.
#Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму
#1 + A + A2 + A3 + ... + AN
def calculate_geometric_series_compact():
# Вводим число А и число положительное N
    try:
        A = float(input("Введите вещественное число A: "))
        N = int(input("Введите целое положительное число N: "))
        if N <= 0:
            raise ValueError("N должно быть больше 0")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return

# Находим сумму.
    sum = 0
    power = 1

    for i in range(N + 1):
        sum += power
        power *= A

    # Результат.
    print(f"Сумма ряда 1 + A + A^2 + ... + A^{N} = {sum}")

# Вызов.
if __name__ == "__main__":
    calculate_geometric_series_compact()
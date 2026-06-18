#возвести в квадрат каждую цифру
#  числа и соеденить полученные результаты
# например, 9119 => 811181

from random import randint

n = randint(10, 9999)
print("Исходное число:", n)
result = "".join(map(lambda x: str(int(x) ** 2), str('9119')))
print("Результат:", result)

N = int(input("Введите размер списка: "))
A = []
for i in range(N):
    A.append(int(input(f"Введите элемент A[{i}]: ")))

print("Исходный список:", A)

result = []
left = 0
right = N - 1

while left <= right:
    if left == right:
        result.append(A[left])
    else:
        result.append(A[left])
        result.append(A[right])
    left += 1
    right -= 1

print("Результат:", result)
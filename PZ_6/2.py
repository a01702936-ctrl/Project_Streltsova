
N = int(input("Введите размер списка: "))
A = []
for i in range(N):
    A.append(int(input(f"Введите элемент A[{i}]: ")))

print("Исходный список:", A)

if N == 0:
    print("Список пуст")
else:
    count = 1 
    for i in range(1, N):
        if A[i] != A[i-1]:  
            count += 1
    
    print("Количество различных элементов:", count)
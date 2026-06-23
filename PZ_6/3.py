
N = int(input("Введите размер списка: "))
A = []
for i in range(N):
    A.append(int(input(f"Введите элемент A[{i}]: ")))

print("Исходный список:", A)

first = A[0]  
for i in range(N - 1):
    A[i] = A[i + 1] 
A[N - 1] = first  

print("После сдвига влево:", A)
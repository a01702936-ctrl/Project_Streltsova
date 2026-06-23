
d = {}
for i in range(7):
    d[i] = i * i

print("Исходный словарь:", d)

del d[2]
del d[3]

print("После удаления:", d)
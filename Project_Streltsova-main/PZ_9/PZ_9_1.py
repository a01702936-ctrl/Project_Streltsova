#Вариант 15.
voyag = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reynatour = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия", "Италия", "Канада"}

print("Италия и Канада есть в:")
if "Италия" in voyag and "Канада" in voyag:
    print("- Вояж")
if "Италия" in reynatour and "Канада" in reynatour:
    print("- РейнаТур")
if "Италия" in raduga and "Канада" in raduga:
    print("- Радуга")

reynatour.add("Индия")
print()
print("РейнаТур после добавления Индии:", reynatour)

vse_tury = voyag | reynatour | raduga
print()
print("Полный список всех туров:", vse_tury)
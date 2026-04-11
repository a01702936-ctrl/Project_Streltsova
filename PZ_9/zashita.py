
bolshoy = {"Лебединое озеро", "Щелкунчик", "Ромео и Джульетта"}
maly = {"Гамлет", "Щелкунчик", "Отелло"}

print("Большой театр:", bolshoy)
print("Малый театр:", maly)
print()

print("1. Спектакли из Большого, которых нет в Малом:",bolshoy - maly)
print()


print("2. Спектакли из Малого, которых нет в Большом:",maly - bolshoy)
print()


print("3. Одинаковые спектакли:",bolshoy & maly)
print()


print("4. Перечни равны?",bolshoy == maly)
print()

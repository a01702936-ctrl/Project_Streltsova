# Создайте класс "Животное", который содержит информацию о виде и возрасте 
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса 
# "Животное" и содержат информацию о породе. 

class Animal:

    def __init__(self, type_animal, age):
        self.type_animal = type_animal
        self.age = age

    def show_info(self):
        print(f"Вид животного {self.type_animal}")
        print(f"Возраст животного {self.age}")

class Dog(Animal):
    def __init__(self, type_animal, age, poroda):
        super().__init__(type_animal, age)
        self.poroda = poroda

    def show_info(self):
        super().show_info()
        print(f"Порода собаки: {self.poroda}")

    

class Cat(Animal):
    def __init__(self, type_animal, age, poroda):
        super().__init__(type_animal, age)
        self.poroda = poroda
    def show_info(self):
        super().show_info()
        print(f"Порода кошки: {self.poroda}")

dog = Dog("Собака", 5, "Аусси")
cat = Cat("Кошка", 3, "Сфинкс")
dog.show_info()
cat.show_info()
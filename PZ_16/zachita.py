#тема ооп.
#создать класс Group и 3 сотрудника. У каждого сотрудника есть параментры: имя,уровень квалификации
#и отдел. Вывести уровни квалификации сотрудников. НЕЛЬЗЯ ДЕЛАТЬ НОВЫЕ КЛАССЫ ОН ТОЛЬКО 1

class Group:

    def __init__(self,name, uroven, otdel):
        self.name = name
        self.uroven = uroven
        self.otdel = otdel

    def show_uroven(self):
        print(f"уровень квалификации {self.name} -{self.uroven}")
str1 = Group("Иван",3,1) 
str2 =Group("Мария",8,3) 
str3 =Group("Денис",6,2) 
str1.show_uroven()
str2.show_uroven()
str3.show_uroven()



    
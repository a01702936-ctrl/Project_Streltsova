import sqlite3

class RASHODY:
    def __init__(self):
        
        self.conn = sqlite3.connect('rashody.db')
        self.cursor = self.conn.cursor()
        
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS rashody (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            kod_producta INTEGER,
            name_producta TEXT,
            rashody REAL,
            summa REAL
        )''')
        self.conn.commit()
        print("База данных подключена, таблица готова")
    
    
    def add(self, data, kod, name, rashody, summa):
        self.cursor.execute('''INSERT INTO rashody (data, kod_producta, name_producta, rashody, summa) 
                                VALUES (?, ?, ?, ?, ?)''', (data, kod, name, rashody, summa))
        self.conn.commit()
        print(f"Добавлена запись: {data} | {kod} | {name} | {rashody} | {summa}")
    
    
    def show_all(self):
        self.cursor.execute('SELECT * FROM rashody')
        rows = self.cursor.fetchall()
        if rows:
            
            print("Все записи:")
            
            for row in rows:
                print(f"ID:{row[0]} | Дата:{row[1]} | Код:{row[2]} | Название:{row[3]} | Расходы:{row[4]} | Сумма:{row[5]}")
        else:
            print("Нет записей")
    
    
    def search(self, field, value):
        
        self.cursor.execute(f'SELECT * FROM rashody WHERE {field} = ?', (value,))
        rows = self.cursor.fetchall()
        if rows:
            print(f"\nРезультаты поиска по {field} = {value}:")
            for row in rows:
                print(f"ID:{row[0]} | Дата:{row[1]} | Код:{row[2]} | Название:{row[3]} | Расходы:{row[4]} | Сумма:{row[5]}")
            return rows
        else:
            print(f"Ничего не найдено по {field} = {value}")
            return []
    
    
    def delete(self, field, value):
        self.cursor.execute(f'DELETE FROM rashody WHERE {field} = ?', (value,))
        self.conn.commit()
        print(f"Удалены записи где {field} = {value}")
    
    
    def update(self, field, value, new_data, new_kod, new_name, new_rashody, new_summa):
        self.cursor.execute(f'''UPDATE rashody SET data=?, kod_producta=?, name_producta=?, rashody=?, summa=? 
                                WHERE {field} = ?''', (new_data, new_kod, new_name, new_rashody, new_summa, value))
        self.conn.commit()
        print(f"Обновлены записи где {field} = {value}")

    def close(self):
        self.conn.close()
        print("База данных закрыта")

db = RASHODY()

print("\n ДОБАВЛЕНИЕ 10 ЗАПИСЕЙ ")
db.add("2024-01-15", 101, "Мука", 50.5, 2500.0)
db.add("2024-01-15", 102, "Сахар", 30.0, 1800.0)
db.add("2024-01-16", 101, "Мука", 20.0, 1000.0)
db.add("2024-01-16", 103, "Масло", 10.0, 800.0)
db.add("2024-01-17", 104, "Яйца", 60.0, 1200.0)
db.add("2024-01-17", 101, "Мука", 40.0, 2000.0)
db.add("2024-01-18", 102, "Сахар", 25.0, 1500.0)
db.add("2024-01-18", 103, "Масло", 15.0, 1200.0)
db.add("2024-01-19", 105, "Соль", 10.0, 300.0)
db.add("2024-01-19", 104, "Яйца", 40.0, 800.0)

db.show_all()

print("ПОИСК")


print("\n1. Поиск по коду продукта 101:")
db.search("kod_producta", 101)

print("\n2. Поиск по названию 'Мука':")
db.search("name_producta", "Мука")

print("\n3. Поиск по дате '2024-01-17':")
db.search("data", "2024-01-17")

print("УДАЛЕНИЕ")


print("\n1. Удаление по коду продукта 105:")
db.delete("kod_producta", 105)

print("\n2. Удаление по названию 'Яйца':")
db.delete("name_producta", "Яйца")

print("\n3. Удаление по дате '2024-01-16':")
db.delete("data", "2024-01-16")

print("\nПосле удаления:")
db.show_all()

print("РЕДАКТИРОВАНИЕ")


print("\n1. Редактирование по коду 101 (меняем название на 'Мука высший сорт'):")
db.update("kod_producta", 101, "2024-01-20", 101, "Мука высший сорт", 50.0, 2500.0)

print("\n2. Редактирование по названию 'Сахар' (меняем сумму на 2000):")
db.update("name_producta", "Сахар", "2024-01-20", 102, "Сахар-песок", 30.0, 2000.0)

print("\n3. Редактирование по дате '2024-01-18' (меняем дату на 2024-01-21):")
db.update("data", "2024-01-18", "2024-01-21", 103, "Масло подсолнечное", 15.0, 1300.0)

print("\nИтоговая таблица:")
db.show_all()

db.close()
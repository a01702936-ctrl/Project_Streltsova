#напишите программу пна пайтон ,которая считывает текстовый файл с именем "text.txt", находит в нем все слова,начинающиеся
#с заглавной буквы,и выводит их в консоль, каждое на новой строке. Если файл не существует или не содержит 
#слов, начинающихся с заглавной буквы,программа должна выводить соответствующие сообщения 
# пример файла 'text.txt'
# Это пример текста. Здесь Есть слова, начинающиеся С заглавной буквы.
# Пример: Python, Regular, Expressions.

import re

def find_uppercase_words(filename):
    try:
       
        with open('zachita/text.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        
        pattern = r'\b[A-ZА-ЯЁ][a-zA-Zа-яА-ЯЁё]*\b'
        uppercase_words = re.findall(pattern, content)
        
        
        if uppercase_words:
            print("Найдены слова, начинающиеся с заглавной буквы:")
            for word in uppercase_words:
                print(word)
        else:
            print("В файле не найдено слов, начинающихся с заглавной буквы.")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не существует.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


find_uppercase_words("text.txt")
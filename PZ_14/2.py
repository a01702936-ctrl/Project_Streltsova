from tkinter import *

def show_digits():
    try:
        
        num = int(entry.get())
        
        if 100 <= abs(num) <= 999:
            
            last_digit = abs(num) % 10
           
            tens_digit = (abs(num) // 10) % 10
            
            result_label.config(text=f"Последняя цифра (единицы): {last_digit}\nСредняя цифра (десятки): {tens_digit}")
        else:
            result_label.config(text="Ошибка: введите ТРЕХЗНАЧНОЕ число!")
    except ValueError:
        result_label.config(text="Ошибка: введите ЦЕЛОЕ число!")

window = Tk()
window.title("Трехзначное число")
window.geometry("400x250")
window.resizable(False, False)

Label(window, text="Трехзначное число", font=("Arial", 14, "bold")).pack(pady=10)

Label(window, text="Введите трехзначное число:", font=("Arial", 10)).pack()
entry = Entry(window, width=20, font=("Arial", 12))
entry.pack(pady=5)

Button(window, text="Показать цифры", command=show_digits, bg="lightblue", font=("Arial", 10, "bold")).pack(pady=10)

result_label = Label(window, text="", font=("Arial", 11), fg="blue", justify="left")
result_label.pack(pady=10)

window.mainloop()
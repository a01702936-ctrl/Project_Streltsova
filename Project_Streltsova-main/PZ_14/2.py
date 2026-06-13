# Вариант 15. Дано трехзначное число. Вывести вначале его последнюю цифру
# (единицы), а затем — его среднюю цифру (десятки).

from tkinter import * 
from tkinter import messagebox

def show():
    num = entry.get()
    a = int(num)
    
    if 100 <= a <= 999:
        ed = a % 10
        des = (a // 10) % 10
        label.config(text=f"{ed} {des}")
    else:
        messagebox.showerror("Ошибка", "Введи трехзначное число!")

root = Tk()
root.title("Число")

label = Label(root, text="Введи трехзначное число", font=("Arial", 10))
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Показать", command=show)
button.pack()

label = Label(root, text="", font=("Arial", 20))
label.pack()

root.mainloop()
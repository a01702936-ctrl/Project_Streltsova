from tkinter import *
from tkinter import messagebox

def show_order():
    order_num = entry_num.get()
    product = entry_product.get()
    quantity = entry_quantity.get()
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    time_h = spin_hour.get()
    time_m = spin_min.get()
    
    text = f"Заказ №{order_num}\nТовар: {product}\nКол-во: {quantity}\nИмя: {name}\nEmail: {email}\nТелефон: {phone}\nАдрес: {address}\nВремя: {time_h}:{time_m}"
    
    messagebox.showinfo("Ваш заказ", text)

window = Tk()
window.title("Создайте заказ")
window.geometry("450x650")

Label(window, text="1. Информация о заказе", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,5))

Label(window, text="Номер заказа *", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_num = Entry(window, width=40)
entry_num.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text="Название товара", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_product = Entry(window, width=40)
entry_product.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text="Количество *", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_quantity = Entry(window, width=40)
entry_quantity.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text=" ", fg="gray").pack(pady=5)

Label(window, text="2. Контактная информация", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,5))

Label(window, text="Ваше имя", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_name = Entry(window, width=40)
entry_name.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text="Ваш email *", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_email = Entry(window, width=40)
entry_email.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text="Ваш телефон *", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_phone = Entry(window, width=40)
entry_phone.pack(anchor="w", padx=10, pady=(0,5))
Label(window, text="Формат: +7 (999) 999-99-99", fg="gray", font=("Arial", 8)).pack(anchor="w", padx=10)

Label(window, text="─────────────────────────────────────", fg="gray").pack(pady=5)

Label(window, text="3. Информация о доставке", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,5))

Label(window, text="Адрес *", font=("Arial", 10)).pack(anchor="w", padx=10)
entry_address = Entry(window, width=40)
entry_address.pack(anchor="w", padx=10, pady=(0,10))

Label(window, text="Время доставки", font=("Arial", 10)).pack(anchor="w", padx=10)

frame_time = Frame(window)
frame_time.pack(anchor="w", padx=10, pady=(0,10))

spin_hour = Spinbox(frame_time, from_=0, to=23, width=5, font=("Arial", 10))
spin_hour.pack(side=LEFT)

Label(frame_time, text=" : ", font=("Arial", 10)).pack(side=LEFT)

spin_min = Spinbox(frame_time, from_=0, to=59, width=5, font=("Arial", 10))
spin_min.pack(side=LEFT)

Button(window, text="Отправить заказ", command=show_order, bg="lightblue", font=("Arial", 10, "bold")).pack(pady=20)

window.mainloop()
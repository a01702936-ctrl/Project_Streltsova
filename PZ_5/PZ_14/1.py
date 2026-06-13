from tkinter import *

window = Tk()
window.title("Создание заказа")
window.geometry("550x650")
window.configure(bg='#f0f0f0')

Label(window, text="Создайте заказ", font="Arial 20 bold", bg='#f0f0f0').pack(pady=15)

frame1 = LabelFrame(window, text="1. Информация о заказе", font="Arial 12 bold", bg='#f0f0f0', padx=15, pady=15)
frame1.pack(fill="x", padx=20, pady=10)

Label(frame1, text="Номер заказа *", bg='#f0f0f0').grid(row=0, column=0, sticky="w", pady=5)
Entry(frame1, width=35).grid(row=0, column=1, padx=10, pady=5)

Label(frame1, text="Название товара", bg='#f0f0f0').grid(row=1, column=0, sticky="w", pady=5)
Entry(frame1, width=35).grid(row=1, column=1, padx=10, pady=5)

Label(frame1, text="Количество *", bg='#f0f0f0').grid(row=2, column=0, sticky="w", pady=5)
Entry(frame1, width=35).grid(row=2, column=1, padx=10, pady=5)

frame2 = LabelFrame(window, text="2. Контактная информация", font="Arial 12 bold", bg='#f0f0f0', padx=15, pady=15)
frame2.pack(fill="x", padx=20, pady=10)

Label(frame2, text="Ваше имя", bg='#f0f0f0').grid(row=0, column=0, sticky="w", pady=5)
Entry(frame2, width=35).grid(row=0, column=1, padx=10, pady=5)

Label(frame2, text="Ваш email *", bg='#f0f0f0').grid(row=1, column=0, sticky="w", pady=5)
Entry(frame2, width=35).grid(row=1, column=1, padx=10, pady=5)

Label(frame2, text="Ваш телефон *", bg='#f0f0f0').grid(row=2, column=0, sticky="w", pady=5)
Entry(frame2, width=35).grid(row=2, column=1, padx=10, pady=5)

Label(frame2, text="Формат: +7 (999) 999-99-99", font="Arial 8", fg="gray", bg='#f0f0f0').grid(row=3, column=1, sticky="w", pady=5)

frame3 = LabelFrame(window, text="3. Информация о доставке", font="Arial 12 bold", bg='#f0f0f0', padx=15, pady=15)
frame3.pack(fill="x", padx=20, pady=10)

Label(frame3, text="Адрес *", bg='#f0f0f0').grid(row=0, column=0, sticky="w", pady=5)
Entry(frame3, width=35).grid(row=0, column=1, padx=10, pady=5)

Label(frame3, text="Время доставки", bg='#f0f0f0').grid(row=1, column=0, sticky="w", pady=5)

time_frame = Frame(frame3, bg='#f0f0f0')
time_frame.grid(row=1, column=1, sticky="w", pady=5)

chasy = Spinbox(time_frame, from_=0, to=23, width=5)
chasy.pack(side="left", padx=2)
Label(time_frame, text="ч", bg='#f0f0f0').pack(side="left", padx=2)

minuty = Spinbox(time_frame, from_=0, to=59, width=5)
minuty.pack(side="left", padx=2)
Label(time_frame, text="мин", bg='#f0f0f0').pack(side="left", padx=2)

Button(window, text="ОФОРМИТЬ ЗАКАЗ", bg='green', fg='white', font="Arial 14 bold", padx=20, pady=10).pack(pady=25)

window.mainloop()


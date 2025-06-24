# дано двузначное число. Вывести число, полученное
# при перестановкe цифр исходного числа.


import tkinter as tk
from tkinter import messagebox

def reverse_number():
    try:
        num_str = entry.get()
        num = int(num_str)

        if 10 <= num <= 99:
            tens = num // 10
            units = num % 10
            reversed_num = units * 10 + tens
            result_label.config(text=f"Результат: {reversed_num}")
        else:
            messagebox.showerror("Ошибка", "Введите двузначное число (от 10 до 99)!")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число, а не текст!")


root = tk.Tk()
root.title("Перестановка цифр")
root.geometry("300x150")

tk.Label(root, text="Введите двузначное число:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Переставить цифры", command=reverse_number).pack(pady=5)

result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=5)


root.mainloop()
# gui_calculator.py
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Результат: " + str(result))
    except Exception as e:
        output.config(text="Ошибка: " + str(e))

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

btn = tk.Button(root, text="Вычислить", command=calculate, font=("Arial", 12))
btn.pack()

output = tk.Label(root, text="", font=("Arial", 14))
output.pack(pady=10)

root.mainloop()


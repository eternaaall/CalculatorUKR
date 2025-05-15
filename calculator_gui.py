import tkinter as tk
from tkinter import ttk
import math
import os

# Основне вікно
root = tk.Tk()
root.title("Науковий калькулятор")
root.geometry("400x450")

# Контейнер для вводу
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Поля вводу — створюємо, але не додаємо до інтерфейсу відразу
entry1 = tk.Entry(input_frame)
entry2 = tk.Entry(input_frame)

# Результат
label_result = tk.Label(root, text="Результат: ")
label_result.pack(pady=5)

# Історія
history_listbox = tk.Listbox(root, height=8)
history_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Операції
operation_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=operation_var, state="readonly")
combo['values'] = [
    "Додавання", "Віднімання", "Множення", "Ділення",
    "Степінь", "Корінь", "Синус", "Косинус"
]
combo.current(0)
combo.pack(pady=5)

# Функція для показу потрібних полів
def update_inputs(event=None):
    for widget in input_frame.winfo_children():
        widget.grid_forget()

    op = operation_var.get()
    if op in ["Синус", "Косинус", "Корінь"]:
        entry1.grid(row=0, column=0, padx=5)
        entry2.delete(0, tk.END)
    else:
        entry1.grid(row=0, column=0, padx=5)
        entry2.grid(row=0, column=1, padx=5)

combo.bind("<<ComboboxSelected>>", update_inputs)
update_inputs()

# Обчислення
def calculate():
    try:
        num1 = float(entry1.get())
        op = operation_var.get()

        if op in ["Синус", "Косинус"]:
            radians = math.radians(num1)
            result = math.sin(radians) if op == "Синус" else math.cos(radians)
            expression = f"{op}({num1}) = {result:.5f}"

        elif op == "Корінь":
            if num1 < 0:
                result = "Помилка: від'ємне число"
                expression = result
            else:
                result = math.sqrt(num1)
                expression = f"√{num1} = {result:.5f}"

        else:
            num2 = float(entry2.get())
            if op == "Додавання":
                result = num1 + num2
                expression = f"{num1} + {num2} = {result:.5f}"
            elif op == "Віднімання":
                result = num1 - num2
                expression = f"{num1} - {num2} = {result:.5f}"
            elif op == "Множення":
                result = num1 * num2
                expression = f"{num1} * {num2} = {result:.5f}"
            elif op == "Ділення":
                if num2 == 0:
                    result = "Помилка: ділення на нуль"
                    expression = result
                else:
                    result = num1 / num2
                    expression = f"{num1} / {num2} = {result:.5f}"
            elif op == "Степінь":
                result = num1 ** num2
                expression = f"{num1}^{num2} = {result:.5f}"

        label_result.config(text=f"Результат: {result}")
        if isinstance(result, (int, float)):
            history_listbox.insert(tk.END, expression)
    except Exception:
        label_result.config(text="Помилка введення")

# Очистити все
def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Результат: ")
    history_listbox.delete(0, tk.END)

# Кнопки
btn_calc = tk.Button(root, text="Обчислити", command=calculate)
btn_calc.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити все", command=clear_all)
btn_clear.pack(pady=5)

# Запуск
root.mainloop()

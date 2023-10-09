import tkinter as tk
import math

def on_button_click(character):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(character))

def on_equals_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_clear_click():
    entry.delete(0, tk.END)

def on_function_click(func):
    try:
        current_val = float(entry.get())
        if func == "sqrt":
            result = math.sqrt(current_val)
        elif func == "square":
            result = current_val ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora para Niños")

# Crear y colocar la entrada de texto
entry = tk.Entry(window, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Crear y colocar los botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x)
    if button == "=":
        tk.Button(window, text=button, command=on_equals_click, height=2, width=5, font=("Arial", 18), bg="light blue").grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, command=action, height=2, width=5, font=("Arial", 18), bg="light blue").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botón para borrar
tk.Button(window, text="C", command=on_clear_click, height=2, width=5, font=("Arial", 18), bg="red").grid(row=row_val, column=0)

# Botones de funciones
tk.Button(window, text="√", command=lambda: on_function_click("sqrt"), height=2, width=5, font=("Arial", 18), bg="yellow").grid(row=row_val, column=1)
tk.Button(window, text="x²", command=lambda: on_function_click("square"), height=2, width=5, font=("Arial", 18), bg="yellow").grid(row=row_val, column=2)

# Iniciar el bucle principal
window.mainloop()

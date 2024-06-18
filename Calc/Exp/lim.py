import tkinter as tk
from sympy import symbols, limit, sympify


def get_limit():
    expression = entry_expression.get()
    a_value = entry_a.get()
    x = symbols('x')

    try:
        f_x = sympify(expression)
        limit_value = limit(f_x, x, a_value)
        limit_label.config(text=f"lim f(x) as x -> {a_value} = {limit_value}")
        error_label.config(text="")
    except Exception as e:
        limit_label.config(text="")
        error_label.config(text=f"Error: {str(e)}")


root = tk.Tk()
root.title("Limit Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_expression = tk.Entry(frame, width=30)
entry_expression.pack(pady=5)

entry_a = tk.Entry(frame, width=10)
entry_a.pack(pady=5)

limit_label = tk.Label(frame, text="", fg="green")
limit_label.pack(pady=5)

error_label = tk.Label(frame, fg="red")
error_label.pack()

limit_button = tk.Button(frame, text="Calculate Limit", command=get_limit)
limit_button.pack(pady=5)

root.mainloop()

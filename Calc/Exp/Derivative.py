import tkinter as tk
from sympy import symbols, diff, simplify


def get_derivative():
    expression = entry_expression.get()
    x = symbols('x')

    try:
        f_x = simplify(expression)
        f_prime_x = diff(f_x, x)
        derivative_label.config(text=f"f'(x) = {f_prime_x}")
        error_label.config(text="")
    except Exception as e:
        derivative_label.config(text="")
        error_label.config(text=f"Error: {str(e)}")


root = tk.Tk()
root.title("Derivative Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_expression = tk.Entry(frame, width=30)
entry_expression.pack(pady=5)

derivative_label = tk.Label(frame, text="", fg="green")
derivative_label.pack(pady=5)

error_label = tk.Label(frame, fg="red")
error_label.pack()

derivative_button = tk.Button(frame, text="Calculate Derivative", command=get_derivative)
derivative_button.pack(pady=5)

root.mainloop()

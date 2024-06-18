import tkinter as tk
from sympy import symbols, integrate, sympify


def get_integral():
    expression = entry_expression.get()
    x = symbols('x')

    try:
        f_x = sympify(expression)
        integral = integrate(f_x, x)
        integral_label.config(text=f"The indefinite integral of f(x) is: {integral} + C")
        error_label.config(text="")
    except Exception as e:
        integral_label.config(text="")
        error_label.config(text=f"Error: {str(e)}")


root = tk.Tk()
root.title("Indefinite Integral Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_expression = tk.Entry(frame, width=30)
entry_expression.pack(pady=5)

integral_label = tk.Label(frame, text="", fg="green")
integral_label.pack(pady=5)

error_label = tk.Label(frame, fg="red")
error_label.pack()

integral_button = tk.Button(frame, text="Calculate Indefinite Integral", command=get_integral)
integral_button.pack(pady=5)

root.mainloop()

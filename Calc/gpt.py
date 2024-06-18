import tkinter as tk
from math import *

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def set_calculation_mode(mode):
    mode_label.config(text="Mode: " + mode)

def show_normal_mode():
    set_calculation_mode("Normal Mode")
    # Clear additional buttons
    button_div.grid_remove()
    button_mod.grid_remove()
    button_gcd.grid_remove()
    button_lcm.grid_remove()
    button_prime_factors.grid_remove()

def show_scientific_mode():
    set_calculation_mode("Scientific Mode")
    # Show additional buttons
    button_div.grid()
    button_mod.grid()
    button_gcd.grid()
    button_lcm.grid()
    button_prime_factors.grid()

def show_arithmetic_mode():
    set_calculation_mode("Arithmetic Mode")
    # Clear additional buttons
    button_ln.grid_remove()
    button_e.grid_remove()
    button_sin.grid_remove()
    button_cos.grid_remove()
    button_tan.grid_remove()
    button_arcsin.grid_remove()
    button_arccos.grid_remove()
    button_arctan.grid_remove()
    button_power.grid_remove()
    button_log.grid_remove()
    button_sqrt.grid_remove()
    button_n_root.grid_remove()
    button_log_n.grid_remove()
    button_pi.grid_remove()
    button_abs.grid_remove()
    # Show arithmetic buttons
    button_div.grid()
    button_mod.grid()
    button_gcd.grid()
    button_lcm.grid()
    button_prime_factors.grid()

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the input and output
entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=10, pady=5, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=10, pady=5, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=10, pady=5, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=10, pady=5, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=10, pady=5, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=10, pady=5, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=10, pady=5, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=10, pady=5, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=10, pady=5, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=10, pady=5, command=lambda: button_click(0))

# Create operator buttons
button_add = tk.Button(window, text="+", padx=10, pady=5, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=10, pady=5, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=10, pady=5, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=10, pady=5, command=lambda: button_click("/"))

# Create special buttons
button_open_paren = tk.Button(window, text="(", padx=10, pady=5, command=lambda: button_click("("))
button_close_paren = tk.Button(window, text=")", padx=10, pady=5, command=lambda: button_click(")"))
button_clear = tk.Button(window, text="C", padx=10, pady=5, command=button_clear)
button_equal = tk.Button(window, text="=", padx=10, pady=5, command=button_equal)
button_delete = tk.Button(window, text="<-", padx=10, pady=5, command=button_delete)

# Create mode menu
mode_menu = tk.Menu(window)
window.config(menu=mode_menu)

calculation_mode_menu = tk.Menu(mode_menu)
mode_menu.add_cascade(label="Calculation Mode", menu=calculation_mode_menu)
calculation_mode_menu.add_command(label="Normal Mode", command=show_normal_mode)
calculation_mode_menu.add_command(label="Scientific Mode", command=show_scientific_mode)
calculation_mode_menu.add_command(label="Arithmetic Mode", command=show_arithmetic_mode)

# Create mode label
mode_label = tk.Label(window, text="Mode: Normal Mode", padx=10, pady=5)
mode_label.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

# Create scientific mode buttons
button_ln = tk.Button(window, text="ln", padx=10, pady=5, command=lambda: button_click("log("))
button_e = tk.Button(window, text="e", padx=10, pady=5, command=lambda: button_click("e"))
button_sin = tk.Button(window, text="sin", padx=10, pady=5, command=lambda: button_click("sin("))
button_cos = tk.Button(window, text="cos", padx=10, pady=5, command=lambda: button_click("cos("))
button_tan = tk.Button(window, text="tan", padx=10, pady=5, command=lambda: button_click("math.tan("))
button_arcsin = tk.Button(window, text="sin^(-1)", padx=10, pady=5, command=lambda: button_click("asin("))
button_arccos = tk.Button(window, text="cos^(-1)", padx=10, pady=5, command=lambda: button_click("acos("))
button_arctan = tk.Button(window, text="tan^(-1)", padx=10, pady=5, command=lambda: button_click("atan("))
button_power = tk.Button(window, text="^", padx=10, pady=5, command=lambda: button_click("**"))
button_log = tk.Button(window, text="log", padx=10, pady=5, command=lambda: button_click("log10("))
button_sqrt = tk.Button(window, text="sqrt", padx=10, pady=5, command=lambda: button_click("sqrt("))
button_n_root = tk.Button(window, text="n-root", padx=10, pady=5, command=lambda: button_click("root("))
button_log_n = tk.Button(window, text="log_n", padx=10, pady=5, command=lambda: button_click("log_n("))
button_pi = tk.Button(window, text="π", padx=10, pady=5, command=lambda: button_click("pi"))
button_abs = tk.Button(window, text="abs", padx=10, pady=5, command=lambda: button_click("abs("))

button_div = tk.Button(window, text="div", padx=10, pady=5, command=lambda: button_click("//"))
button_mod = tk.Button(window, text="mod", padx=10, pady=5, command=lambda: button_click("%"))
button_gcd = tk.Button(window, text="gcd", padx=10, pady=5, command=lambda: button_click("gcd("))
button_lcm = tk.Button(window, text="lcm", padx=10, pady=5, command=lambda: button_click("lcm("))
button_prime_factors = tk.Button(window, text="Prime Factors", padx=10, pady=5, command=lambda: button_click("prime_factors("))

# Place buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_open_paren.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_close_paren.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_clear.grid(row=5, column=0)
button_delete.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

# Place scientific mode buttons on the grid (initially hidden)
button_ln.grid(row=1, column=4)
button_e.grid(row=2, column=4)
button_sin.grid(row=3, column=4)
button_cos.grid(row=4, column=4)
button_tan.grid(row=5, column=4)
button_arcsin.grid(row=1, column=5)
button_arccos.grid(row=2, column=5)
button_arctan.grid(row=3, column=5)
button_power.grid(row=4, column=5)
button_log.grid(row=5, column=5)
button_sqrt.grid(row=1, column=6)
button_n_root.grid(row=2, column=6)
button_log_n.grid(row=3, column=6)
button_pi.grid(row=4, column=6)
button_abs.grid(row=5, column=6)

# Place arithmetic mode buttons on the grid (initially hidden)
button_div.grid(row=1, column=4)
button_mod.grid(row=2, column=4)
button_gcd.grid(row=3, column=4)
button_lcm.grid(row=4, column=4)
button_prime_factors.grid(row=5, column=4)

# Hide scientific mode buttons by default
button_ln.grid_remove()
button_e.grid_remove()
button_sin.grid_remove()
button_cos.grid_remove()
button_tan.grid_remove()
button_arcsin.grid_remove()
button_arccos.grid_remove()
button_arctan.grid_remove()
button_power.grid_remove()
button_log.grid_remove()
button_sqrt.grid_remove()
button_n_root.grid_remove()
button_log_n.grid_remove()
button_pi.grid_remove()
button_abs.grid_remove()

# Hide arithmetic mode buttons by default
button_div.grid_remove()
button_mod.grid_remove()
button_gcd.grid_remove()
button_lcm.grid_remove()
button_prime_factors.grid_remove()

# Start the main event loop
window.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from sympy import symbols, sympify
import pandas as pd


def generate_table():
    expression = entry_expression.get()
    start_x = float(entry_start_x.get())
    end_x = float(entry_end_x.get())
    step_size = float(entry_step_size.get())

    x = symbols('x')
    try:
        f_x = sympify(expression)
        table_text.delete("1.0", tk.END)  # Clear previous table content

        table_text.insert(tk.END, f"{'x':<10}{'f(x)':<10}\n")
        table_text.insert(tk.END, "-" * 20 + "\n")

        current_x = start_x
        table_data = []
        while current_x <= end_x:
            f_x_value = f_x.subs(x, current_x)
            table_text.insert(tk.END, f"{current_x:<10.4f}{f_x_value:<10.4f}\n")
            table_data.append([current_x, f_x_value])
            current_x += step_size

        error_label.config(text="")
        return table_data
    except Exception as e:
        table_text.delete("1.0", tk.END)
        error_label.config(text=f"Error: {str(e)}")
        return None


def save_to_excel():
    table_data = generate_table()
    if table_data:
        df = pd.DataFrame(table_data, columns=["x", "f(x)"])
        df.to_excel("table_of_values.xlsx", index=False)
        save_label.config(text="Table saved to table_of_values.xlsx")
    else:
        save_label.config(text="Error: Cannot save table. Check input.")


root = tk.Tk()
root.title("Table of Values Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_expression = tk.Label(frame, text="f(x) expression:")
label_expression.pack()
entry_expression = tk.Entry(frame, width=30)
entry_expression.pack(pady=5)

label_start_x = tk.Label(frame, text="Start x:")
label_start_x.pack()
entry_start_x = tk.Entry(frame, width=10)
entry_start_x.pack(pady=5)

label_end_x = tk.Label(frame, text="End x:")
label_end_x.pack()
entry_end_x = tk.Entry(frame, width=10)
entry_end_x.pack(pady=5)

label_step_size = tk.Label(frame, text="Step size:")
label_step_size.pack()
entry_step_size = tk.Entry(frame, width=10)
entry_step_size.pack(pady=5)

# Create a scrolled text widget with a vertical scrollbar
table_text = scrolledtext.ScrolledText(frame, width=30, height=10)
table_text.pack()

error_label = tk.Label(frame, fg="red")
error_label.pack()

table_button = tk.Button(frame, text="Generate Table", command=generate_table)
table_button.pack(pady=5)

save_button = tk.Button(frame, text="Save to Excel", command=save_to_excel)
save_button.pack(pady=5)

save_label = tk.Label(frame, fg="blue")
save_label.pack()

root.mainloop()

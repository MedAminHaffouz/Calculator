import tkinter as tk


def solve_linear_system():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())

        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        if a2 * b1 - b2 * a1 == 0:
            solution_text.delete("1.0", tk.END)
            solution_text.insert(tk.END, "Error: Denominator is zero. Cannot solve the system.")
            return

        x = (b1 * c2 - b2 * c1) / (a2 * b1 - b2 * a1)
        y = c1 / b1 - (a1 * x) / b1

        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"x = {x}\n")
        solution_text.insert(tk.END, f"y = {y}\n")

    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


root = tk.Tk()
root.title("Solution of Linear System")

indice1 = tk.Label(root, text="{a1x+b1y=c1")
indice1.pack(padx=10)

indice2 = tk.Label(root, text="{a2x+b2y=c2")
indice2.pack(padx=10)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)


label_a1 = tk.Label(frame, text="Enter a1:")
label_a1.grid(row=0, column=0, padx=5)
entry_a1 = tk.Entry(frame, width=10)
entry_a1.grid(row=0, column=1, padx=5)

label_b1 = tk.Label(frame, text="Enter b1:")
label_b1.grid(row=0, column=2, padx=5)
entry_b1 = tk.Entry(frame, width=10)
entry_b1.grid(row=0, column=3, padx=5)

label_c1 = tk.Label(frame, text="Enter c1:")
label_c1.grid(row=0, column=4, padx=5)
entry_c1 = tk.Entry(frame, width=10)
entry_c1.grid(row=0, column=5, padx=5)


label_a2 = tk.Label(frame, text="Enter a2:")
label_a2.grid(row=1, column=0, padx=5)
entry_a2 = tk.Entry(frame, width=10)
entry_a2.grid(row=1, column=1, padx=5)

label_b2 = tk.Label(frame, text="Enter b2:")
label_b2.grid(row=1, column=2, padx=5)
entry_b2 = tk.Entry(frame, width=10)
entry_b2.grid(row=1, column=3, padx=5)

label_c2 = tk.Label(frame, text="Enter c2:")
label_c2.grid(row=1, column=4, padx=5)
entry_c2 = tk.Entry(frame, width=10)
entry_c2.grid(row=1, column=5, padx=5)

solve_button = tk.Button(frame, text="Solve Linear System", command=solve_linear_system)
solve_button.grid(row=2, columnspan=6, pady=10)

solution_text = tk.Text(frame, width=40, height=5)
solution_text.grid(row=3, columnspan=6, padx=5)

root.mainloop()

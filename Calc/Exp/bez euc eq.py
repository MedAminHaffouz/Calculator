import tkinter as tk
from sympy import symbols, Eq, diophantine, sympify


def solve_integer_system():
    u, v = symbols('u v', integer=True)

    equation_str = entry_equation.get()
    try:
        equation = Eq(sympify(equation_str), 0)

        # Rearrange the equation to fit the form 'ax + by = 0'
        lhs = equation.lhs
        rhs = equation.rhs
        rearranged_eq = Eq(lhs - rhs, 0)

        solutions = diophantine(rearranged_eq)

        solution_text.delete("1.0", tk.END)  # Clear previous solutions

        if not solutions:
            solution_text.insert(tk.END, "No integer solutions found.")
        else:
            for sol in solutions:
                sol_u = sol[u]
                sol_v = sol[v]
                solution_text.insert(tk.END, f"u = {sol_u}, v = {sol_v}\n")

    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


root = tk.Tk()
root.title("Integer Solution of au + bv = c")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_equation = tk.Label(frame, text="Enter the equation (au + bv = c):")
label_equation.pack()
entry_equation = tk.Entry(frame, width=30)
entry_equation.pack(pady=5)

solve_button = tk.Button(frame, text="Solve Integer System", command=solve_integer_system)
solve_button.pack(pady=5)

solution_text = tk.Text(frame, width=40, height=10)
solution_text.pack()

root.mainloop()

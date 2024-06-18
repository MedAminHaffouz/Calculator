import tkinter as tk
from sympy import symbols, Eq, solve, sympify


def solve_system():
    equations_str = entry_equations.get("1.0", tk.END)
    equations_list = [eq.strip() for eq in equations_str.splitlines() if eq.strip()]

    x, y = symbols('x y')
    try:
        equations = [Eq(sympify(eq), 0) for eq in equations_list]
        solutions = solve(equations, (x, y))
        solution_text.delete("1.0", tk.END)  # Clear previous solutions

        if len(solutions) == 0:
            solution_text.insert(tk.END, "No real solutions found.")
        else:
            for idx, sol in enumerate(solutions):
                solution_text.insert(tk.END, f"Solution {idx + 1}: x = {sol[x]}, y = {sol[y]}\n")
    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


root = tk.Tk()
root.title("System of Equations Solver")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_equations = tk.Label(frame, text="Enter the system of equations:")
label_equations.pack()
entry_equations = tk.Text(frame, width=40, height=5)
entry_equations.pack(pady=5)

solve_button = tk.Button(frame, text="Solve System", command=solve_system)
solve_button.pack(pady=5)

solution_text = tk.Text(frame, width=40, height=10)
solution_text.pack()

root.mainloop()

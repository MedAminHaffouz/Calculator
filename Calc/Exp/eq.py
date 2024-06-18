import tkinter as tk
from sympy import symbols, Eq, solve, sympify


def solve_equation():
    equation_str = entry_equation.get()
    x = symbols('x')
    try:
        equation = Eq(sympify(equation_str), 0)
        solutions = solve(equation, x)
        solution_text.delete("1.0", tk.END)  # Clear previous solutions
        if len(solutions) == 0:
            solution_text.insert(tk.END, "No real solutions found.")
        else:
            for idx, sol in enumerate(solutions):
                solution_text.insert(tk.END, f"Solution {idx + 1}: x = {sol}\n")
    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


floateq = tk.Tk()
floateq.title("Equations with float variables Solver")

frame = tk.Frame(floateq)
frame.pack(padx=10, pady=10)

label_equation = tk.Label(frame, text="Enter the equation:")
label_equation.pack()
entry_equation = tk.Entry(frame, width=30)
entry_equation.pack(pady=5)

solve_button = tk.Button(frame, text="Solve Equation", command=solve_equation)
solve_button.pack(pady=5)

solution_text = tk.Text(frame, width=40, height=10)
solution_text.pack()

floateq.mainloop()

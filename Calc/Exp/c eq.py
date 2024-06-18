import tkinter as tk
from sympy import symbols, solveset, Eq, sympify, S


def solve_complex_equation():
    z = symbols('z')
    equation_str = entry_equation.get()
    try:
        equation = Eq(sympify(equation_str), 0)
        solutions = solveset(equation, z, domain=S.Complexes)

        solution_text.delete("1.0", tk.END)  # Clear previous solutions

        if len(solutions) == 0:
            solution_text.insert(tk.END, "No complex solutions found.")
        else:
            for sol in solutions:
                solution_text.insert(tk.END, f"z = {sol}\n")

    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


ceqsolve = tk.Tk()
ceqsolve.title("Complex Equation Solver")

frame = tk.Frame(ceqsolve)
frame.pack(padx=10, pady=10)

label_equation = tk.Label(frame, text="Enter the complex equation:")
label_equation.pack()
entry_equation = tk.Entry(frame, width=30)
entry_equation.pack(pady=5)

solve_button = tk.Button(frame, text="Solve Complex Equation", command=solve_complex_equation)
solve_button.pack(pady=5)

solution_text = tk.Text(frame, width=40, height=10)
solution_text.pack()

root.mainloop()

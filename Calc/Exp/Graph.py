import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from math import *


def Graph():
    expression = entry_expression.get()
    try:
        def f(x):
            return eval(expression)

        x = np.linspace(-10, 10, 1000)
        y = f(x)

        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Graph of f(x)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")


root = tk.Tk()
root.title("Graphical Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_expression = tk.Entry(frame, width=30)
entry_expression.pack(pady=5)

error_label = tk.Label(frame, fg="red")
error_label.pack()

graph_button = tk.Button(frame, text="Graph", command=Graph)
graph_button.pack(pady=5)

root.mainloop()

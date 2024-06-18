import tkinter as tk


def open_window():
    root2 = tk.Toplevel(root)
    root2.title("Window 2")
    root2.configure(bg="yellow")


root = tk.Tk()
root.title("Window 1")
root.configure(bg="blue")

button = tk.Button(root, text="Open Window 2", command=open_window)
button.pack(padx=20, pady=10)

root.mainloop()

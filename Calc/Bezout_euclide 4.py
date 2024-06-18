from numpy import *

a = int(input("Donner a : "))
b = int(input("Donner b : "))

val_p = [0, 1]
val_r = [a, b]
val_q = ["(x)"]
p = 1
val_q.append(a // b)
while val_r[p] != 0:
    p = p + 1
    val_p.append(p)
    val_r.append((val_r[p - 2]) % (val_r[p - 1]))
    if val_r[p] != 0:
        val_q.append((val_r[p - 1]) // (val_r[p]))
    else:
        val_q.append("(x)")

val_u = [1, 0]
val_v = [0, 1]
for i in range(2, p + 1):
    val_u.append((val_u[i - 2]) - (val_q[i - 1]) * (val_u[i - 1]))
    val_v.append((val_v[i - 2]) - (val_q[i - 1]) * (val_v[i - 1]))

L = p + 2
T = empty((5, L), dtype=object)

T[0, 0] = "p"
T[1, 0] = "r"
T[2, 0] = "q"
T[3, 0] = "u"
T[4, 0] = "v"
for j in range(1, L):
    T[0, j] = val_p[j - 1]
    T[1, j] = val_r[j - 1]
    T[2, j] = val_q[j - 1]
    T[3, j] = val_u[j - 1]
    T[4, j] = val_v[j - 1]

for row in T:
    print("+", end="")  # Start the row with a vertical separator

    for cell in row:
        print("---+", end="")  # Print a horizontal line before each cell
    print()  # Move to the next line

    print("|", end="")  # Start a new row with a vertical separator

    for cell in row:
        print(f" {cell} |", end="")  # Print the cell with the desired formatting
    print()  # Move to the next line

print("+", end="")  # Print the bottom line
for _ in T[0]:
    print("---+", end="")
print()

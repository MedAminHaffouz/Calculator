import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^i
def f(x):
    return np.exp(1j * np.angle(x) * 1j)

# Create a meshgrid of complex numbers in the range -2 <= Re(x) <= 2, -2 <= Im(x) <= 2
x, y = np.meshgrid(np.linspace(-2, 2, 401), np.linspace(-2, 2, 401))
z = x + y * 1j

# Evaluate f(z) for each complex number z in the meshgrid
w = f(z)

# Plot the real part of f(z) as a contour plot
plt.contourf(x, y, np.real(w), levels=40)
plt.colorbar()

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 60, 40, 25]

plt.plot(x, y, color="orange", marker="o", label="My Data")

plt.title("Matplot chart")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.grid(True)
plt.legend()

plt.show()

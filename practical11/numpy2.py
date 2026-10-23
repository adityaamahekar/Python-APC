#array operations +, -, transpose

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Addition:")
print(a + b)

print("Subtraction:")
print(a - b)

print("Transpose of a:")
print(a.T)

print("Transpose of b:")
print(b.T)
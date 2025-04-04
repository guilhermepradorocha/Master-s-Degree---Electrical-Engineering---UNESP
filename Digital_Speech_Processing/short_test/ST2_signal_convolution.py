''''
Short Test (ST2):
1. define two discrete-time signals, i.e., a[·] and b[·], being the former
two-sample long and the latter four-sample long. Then, obtain the
resulting signal y[·] = a[·] ⇤ b[·].
2. convolve y[·], just obtained, with itself.
3. find a general equation to calculate the length of any resulting convolved 
signal from the lengths of both the input signals.

'''
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2])         # Two elements
b = np.array([3, 4, 5, 6])   # Four elements

# Convolve a[·] e b[·] to obtain y[·]
y = np.convolve(a, b)

print(f"y[·] = {y}")

# Convolve y[·] by itself
y_convolved = np.convolve(y, y)
print(f"y[·] * y[·] = {y_convolved}")

# Find the length signal resulted
M = len(a)
N = len(b)
L = M + N - 1
L_final = len(y) + len(y) - 1

print(f"length y[·]: {L} (M + N - 1)")
print(f"length  y[·] * y[·]: {L_final}")

# Plotar os sinais
plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.stem(a)
plt.title("Signal a[·]")

plt.subplot(3, 1, 2)
plt.stem(b)
plt.title("Signal b[·]")

plt.subplot(3, 1, 3)
plt.stem(y_convolved)
plt.title("Convolve y[·] by itself")

plt.tight_layout()
plt.show()

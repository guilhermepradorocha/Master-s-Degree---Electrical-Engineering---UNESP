'''

Short Test (ST1): Considering that the M-sample long signal s[·]
corresponds to a speech raw data, write either an algorithm or a
code in any programming language to reverse it in time.
 '''

import numpy as np
import matplotlib.pyplot as plt

M = 100  # Sample size
s = np.random.randn(M)  # Aleatory signal

# Reversing signal
s_reverso = s[::-1]

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(s, label='Original Signal')
plt.title('Original Signal')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(s_reverso, label='Reverse Signal', color='red')
plt.title('Reverse Signal')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
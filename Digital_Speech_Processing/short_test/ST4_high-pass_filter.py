'''
Design an FIR filter (g[n]) of order M = 5
to allow for frequencies above 1500 Hz to pass through, assuming
that the input signal to be filtered (x[n]) was sampled at 24000 samples
per second. Then, obtain the system transfer function, i.e., the
Z-Transform of g[n].
'''
#%%
import numpy as np
import math 

fs = 24000  # Sampling frequency (Hz)
fc = 1500   # Cutoff frequency (Hz) 
M = 5       # Filter order 
N = M + 1   # Filter length 

# Normalized cutoff frequency
wc = (2 * math.pi * fc) / fs 

# Index vectors for calculations
n_idx = np.arange(N)
k = n_idx - M / 2

# Calculate ideal low-pass coefficients h[n]

h = np.sin(wc * k) / (math.pi * k)

# Calculate coefficients for the windowed/shifted impulse d[n]
d = np.sin(math.pi * k) / (math.pi * k)

# Calculate high-pass coefficients g[n] = d[n] - h[n]
g = d - h

print(f"\nCalculated High-Pass Filter Coefficients g[n]:")
np.set_printoptions(precision=7, suppress=True) 
print(f"g = {g}")



# Build the G[z] polynomial string representation
terms = []
for i in range(N): 
    coeff_val = g[i]
    sign = "+" if coeff_val >= 0 else "-"
    if i == 0 and sign == "+":
        sign = ""
    coeff_str = f"{abs(coeff_val):.5f}" # 5 decimal places

    if i == 0:
        z_term = ""
    elif i == 1:
        z_term = f"*z^{{-1}}"
    else:
        z_term = f"*z^{{-{i}}}"

    if i == 0:
         terms.append(f"{sign}{coeff_str}")
    else:
         terms.append(f" {sign} {coeff_str}{z_term}")

Gz_str = "".join(terms)

print(f"The transfer function G[z] defined by coefficients g[n] is:")
print(f"G[z] = {Gz_str}")

# %%

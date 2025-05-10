#%%
'''
Today’s Short Test (ST5): Design an FIR filter (q[n]) of order M = 5
to cut-off frequencies within the range 2500 Hz ⇠ 3500 Hz, allowing
for all the others to pass through. Assume that the input signal to be
filtered (x[n]) was sampled at 10000 samples per second.
'''

import numpy as np
import math

M = 5
N = M + 1
fs = 10000  # Sampling frequency (Hz)
f_cA = 2500 # Cutoff for LPF component h[n] (Hz)
f_cB = 3500 # Cutoff for HPF component g[n] (Hz)

print(f"--- ST5: Band-Stop Filter Design ---")
print(f"Filter Order M = {M}, Filter Length N = {N}")
print(f"Sampling Frequency (fs) = {fs} Hz")
print(f"Stop-band: {f_cA} Hz to {f_cB} Hz")

# --- Normalized Cutoff Frequencies ---
wcA = (2 * math.pi * f_cA) / fs  # For LPF h[n]
wcB = (2 * math.pi * f_cB) / fs  # For HPF g[n] (used in its LPF component h'_LP)

print(f"Normalized cutoff for LPF h[n] (wcA): {wcA / math.pi:.4f} * pi rad/sample")
print(f"Normalized cutoff for HPF g[n] (wcB): {wcB / math.pi:.4f} * pi rad/sample")

# Index vector k for ideal response calculation (centered)
k_indices = np.arange(N) - M / 2 # k = n - M/2

# --- 1. Design Low-Pass Filter h[n] (cutoff wcA) ---
# h_ideal[k] = sin(wcA * k) / (pi * k)
h_n = np.sin(wcA * k_indices) / (math.pi * k_indices)
print(f"\n1. Low-Pass Filter Coefficients h[n] (cutoff {f_cA} Hz):")
np.set_printoptions(precision=7, suppress=True)
print(f"h_n = {h_n}")

# --- 2. Design High-Pass Filter g[n] (cutoff wcB) ---
# Method: g[n] = d[n] - h_prime_LP[n]
# d[n] is the windowed/shifted delta: d_ideal[k] = sin(pi * k) / (pi * k)
# h_prime_LP[n] is an auxiliary LPF with cutoff wcB: h_prime_LP_ideal[k] = sin(wcB * k) / (pi * k)

d_component = np.sin(math.pi * k_indices) / (math.pi * k_indices)
h_prime_LP_component = np.sin(wcB * k_indices) / (math.pi * k_indices)
g_n = d_component - h_prime_LP_component

print(f"\n2. High-Pass Filter Coefficients g[n] (cutoff {f_cB} Hz):")
print(f"g_n = {g_n}")

# --- 3. Calculate Band-Stop Filter q[n] = h[n] + g[n] ---
q_n = h_n + g_n

print(f"\n3. Band-Stop Filter Coefficients q[n] = h[n] + g[n]:")
print(f"q_n = {q_n}")
print(f"Sum of q_n coefficients (DC gain): {np.sum(q_n):.7f}")
print("--- ST5 Design Complete ---")
#%%

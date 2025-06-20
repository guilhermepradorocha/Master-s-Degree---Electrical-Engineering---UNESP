#%%
import numpy as np
import math

'''
Today’s Short Test (ST6): Design an FIR filter (q[n]), subtype I, of
order M = 4, to cut-off frequencies within the range 2500 Hz ⇠ 3500
Hz, allowing for all the others to pass through. Assume that the input
signal to be filtered (x[n]) was sampled at 10000 samples per second.
Normalize the filters’ coefficients in such a way that the filter presents
a gain of 0 dB in the pass-band. Lastly, write down the difference
equation to filter an input signal x[n] by using q[n].
'''

M = 4       # Filter order (results in N=5, odd length for Type I)
N = M + 1   # Filter length (number of taps)
fs = 10000  # Sampling frequency (Hz)

# Stop-band edges
f_cA = 2500  # Lower edge of stop-band (cutoff for LPF h_A[n]) in Hz
f_cB = 3500  # Upper edge of stop-band (cutoff for LPF h_B[n]) in Hz

# Normalized cutoff frequencies (radians/sample)
wcA = (2 * math.pi * f_cA) / fs
wcB = (2 * math.pi * f_cB) / fs

print(f"Normalized cutoff for LPF h_A[n] (wcA): {wcA / math.pi:.4f} * pi ({wcA:.7f} rad/sample)")
print(f"Normalized cutoff for LPF h_B[n] (wcB): {wcB / math.pi:.4f} * pi ({wcB:.7f} rad/sample)")

# Index vector k for ideal response calculation (centered around 0)
# M = 4, so M/2 = 2. For n = 0..4, k = n - 2 => [-2.0, -1.0, 0.0, 1.0, 2.0]
k_indices = np.arange(N) - (M / 2.0)
print(f"Indices k (for ideal response calculation): {k_indices}\n" + "-" * 50)

# Formula: h_ideal[k] = sin(wcA * k) / (pi * k); if k=0, h_ideal[0] = wcA / pi
h_A_n = np.zeros(N)
for i, k_val in enumerate(k_indices):
    if k_val == 0:
        h_A_n[i] = wcA / math.pi
    else:
        h_A_n[i] = math.sin(wcA * k_val) / (math.pi * k_val)

print(f"\nLow-Pass Filter Coefficients h_A[n] (cutoff {f_cA} Hz)")
np.set_printoptions(precision=7, suppress=True)
print(f"h_A_n = {h_A_n}")

# Formula: h_ideal[k] = sin(wcB * k) / (pi * k); if k=0, h_ideal[0] = wcB / pi
h_B_n = np.zeros(N)
for i, k_val in enumerate(k_indices):
    if k_val == 0:
        h_B_n[i] = wcB / math.pi
    else:
        h_B_n[i] = math.sin(wcB * k_val) / (math.pi * k_val)

print(f"\nLow-Pass Filter Coefficients h_B[n] (cutoff {f_cB} Hz)")
print(f"h_B_n = {h_B_n}")
# print(f"Sum of h_B_n coefficients: {np.sum(h_B_n):.7f}")

p_n = h_B_n - h_A_n

print(f"\nBand-Pass Filter Coefficients p[n] = h_B[n] - h_A[n]")
print(f"p_n = {p_n}")

# d_ideal[k] = sin(pi * k) / (pi * k); if k=0, d_ideal[0] = 1.0
d_n = np.zeros(N)
for i, k_val in enumerate(k_indices):
    if k_val == 0:
        d_n[i] = 1.0
    else:
        d_n[i] = math.sin(math.pi * k_val) / (math.pi * k_val)

print(f"\nShifted All-Pass (Impulse) Filter Coefficients d[n]")
print(f"d_n = {d_n}")

q_n = d_n - p_n

print(f"\nBand-Stop Filter Coefficients q[n] = d[n] - p[n]")
print(f"q_n (unnormalized) = {q_n}")
sum_q_n_initial = np.sum(q_n)
print(f"Sum of q_n coefficients (unnormalized): {sum_q_n_initial:.7f}")

if sum_q_n_initial == 0:
    print("\nWarning: Sum of initial q[n] coefficients is zero. Cannot normalize.")
    q_n_normalized = np.copy(q_n)
else:
    q_n_normalized = q_n / sum_q_n_initial

print(f"\nNormalized Band-Stop Filter Coefficients q_n_normalized")
print(f"q_n_normalized = {q_n_normalized}")
print(f"Sum of q_n_normalized coefficients (should be 1.0): {np.sum(q_n_normalized):.7f}")

print(f"\nDifference Equation for y[n] using q_n_normalized")

diff_eq_str = "y[n] = "
for i in range(N):
    coeff_val = q_n_normalized[i]
    sign_char = "+" if coeff_val >= 0 else "-" 
    
    if i == 0:
        current_term_sign_str = "" if sign_char == "+" else "-"
    else: # For subsequent terms, always include space and sign
        current_term_sign_str = f" {sign_char} "
        
    # Add coefficient and x[n-i] term
    if i == 0:
        diff_eq_str += f"{current_term_sign_str}{abs(coeff_val):.5f}*x[n]"
    else:
        diff_eq_str += f"{current_term_sign_str}{abs(coeff_val):.5f}*x[n-{i}]"

print(diff_eq_str)

# %%

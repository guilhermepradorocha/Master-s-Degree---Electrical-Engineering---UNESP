'''
Design an FIR filter (h[n]) of order M = 5
to allow for frequencies up to 1500 Hz to pass through, assuming that
the input signal to be filtered (x[n]) was sampled at 12000 samples
per second. Considering, as an example, that x[n] = {−1, 1, −2, 2, 2},
filter it by using h[n], obtaining the output signal.

'''

#%%
import numpy as np

s = 12000  #Sample
f = 1500   #Frequency
M = 5       # order
N = M + 1   # coeficiente

wc = (2 * np.pi * f) / s

n = np.arange(N)

k = n - M / 2

h = np.sin(wc * k) / (np.pi * k)


print("Coeficients:")
print(f"h[.] = {h}")

#input signal
x = np.array([-1, 1, -2, 2, 2])

y = np.convolve(x, h) #convolve filter and input signal

print("Output signal:")
print(y)



# %%

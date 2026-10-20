import numpy as np
import matplotlib.pyplot as plt

vals = np.linspace(0, 0.4, 1600, endpoint = False)
x = lambda t: np.sin(800 * np.pi * t)
a_vals = x(vals)

def sawtooth(t):
    return 2 * (t - np.floor(t + 1 / 2))

x = lambda t: sawtooth(240 * t)

c_vals = np.array([x(val) for val in vals])

sum_vals = a_vals + c_vals

fig, axs = plt.subplots(3, figsize = (8, 8))
axs[0].plot(vals, a_vals, color = 'purple')
axs[1].plot(vals, c_vals, color = 'red')
axs[2].plot(vals, sum_vals, color = 'green')
plt.savefig("Ex4.pdf")
plt.show()
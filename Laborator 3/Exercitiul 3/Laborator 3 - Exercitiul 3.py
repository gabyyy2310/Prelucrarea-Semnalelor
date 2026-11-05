import numpy as np
import matplotlib.pyplot as plt

f1 = 18
f2 = 77
f3 = 99

fs = 1000

x = lambda t: np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)

vals = np.linspace(0, 1, fs, endpoint = False)

omegas = np.arange(0, 101)
P = np.outer(omegas, vals)

X = np.sum(x(vals) * np.exp(-2j * np.pi * P), axis=1)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(vals, x(vals), color='purple')
axs[0].set_xlabel('Timp (s)')
axs[0].set_ylabel('x(t)')

axs[1].plot(omegas, np.abs(X), color='purple')
axs[1].set_xlabel('Frecventa (Hz)')
axs[1].set_ylabel('|X(omega)|')
plt.savefig('Ex3.pdf')
plt.show()

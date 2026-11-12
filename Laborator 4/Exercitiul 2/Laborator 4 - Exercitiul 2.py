import numpy as np
import matplotlib.pyplot as plt

x = lambda t: np.sin(2 * np.pi * 30 * t)
y = lambda t: np.sin(2 * np.pi * 14 * t)
z = lambda t: np.sin(2 * np.pi * 46 * t)

fs = 16

vals = np.linspace(0, 1, 1000, endpoint = False)
bad_vals = np.linspace(0, 1, fs, endpoint = False)

fig, axs = plt.subplots(3, figsize = (9, 9))
axs[0].plot(vals, x(vals), color = 'red')
axs[0].scatter(bad_vals, x(bad_vals), marker = 'x', color = 'green')
axs[1].plot(vals, y(vals), color = 'blue')
axs[1].scatter(bad_vals, y(bad_vals), marker = 'x', color = 'orange')
axs[2].plot(vals, z(vals), color = 'purple')
axs[2].scatter(bad_vals, z(bad_vals), marker = 'x', color = 'yellow')
plt.savefig("Ex2.pdf")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#exercitiul 1, a) - axa numerelor reale
vals = np.linspace(0, 1, 1000)
zero = np.zeros(1000)

plt.figure()
plt.grid()
plt.title("Axa numerelor reale")
plt.plot(vals, zero, color = 'red')
plt.savefig("Ex1-pct-a.pdf")
plt.show()

#exercitiul 1, b) de facut plot la urmatoarele semnale:
x = lambda t: np.cos(520 * np.pi * t + np.pi / 3)
y = lambda t: np.cos(280 * np.pi * t - np.pi / 3)
z = lambda t: np.cos(120 * np.pi * t + np.pi / 3)

vals = np.linspace(0, 0.1, 1000)
x_vals = x(vals)
y_vals = y(vals)
z_vals = z(vals)

fig, axs = plt.subplots(3)
fig.suptitle("Reprezentarea semnalelor x, y si z")
axs[0].plot(vals, x_vals, color = 'purple')
axs[1].plot(vals, y_vals, color = 'red')
axs[2].plot(vals, z_vals, color = 'blue')
plt.savefig("Ex1-pct-b.pdf")
plt.show()

#exercitiul 1, c)
#esantionam semnalele cu frecventa de 200Hz
x_esantionat = lambda t: np.cos(2.6 * np.pi * t + np.pi / 3)
y_esantionat = lambda t: np.cos(1.4 * np.pi * t - np.pi / 3)
z_esantionat = lambda t: np.cos(0.6 * np.pi * t + np.pi / 3)

vals = np.array(range(0, 30))
x_vals = x_esantionat(vals)
y_vals = y_esantionat(vals)
z_vals = z_esantionat(vals)

fig, axs = plt.subplots(3)
fig.suptitle("Reprezentarea semnalelor esantionate x, y si z")
axs[0].stem(vals, x_vals)
axs[1].stem(vals, y_vals)
axs[2].stem(vals, z_vals)
plt.savefig("Ex1-pct-c.pdf")
plt.show()

#observam ca gasim acelasi grafic (pentru ca 2pi e perioada ptr cos + cos e para)























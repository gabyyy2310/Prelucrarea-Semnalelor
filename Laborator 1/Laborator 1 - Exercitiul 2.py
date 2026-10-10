import numpy as np
import matplotlib.pyplot as plt

#exercitiul 2
#a) semnal sinusoidal de frecventa 400Hz si 1600 esantioane
vals = np.linspace(0, 0.4, 1600, endpoint = False)
x = lambda t: np.sin(800 * np.pi * t)
x_vals = x(vals)

fig, axs = plt.subplots(1, figsize = (5, 5))
fig.suptitle("Reprezentarea semnalului x")
axs.plot(vals, x_vals)
plt.savefig("Ex2-pct-a.pdf")
plt.show()

#b)semnal sinusoidal de frecventa 800Hz, care sa dureze 3 secunde
t = np.linspace(0, 3, 9000, endpoint = False)

x = lambda t: np.sin(1600 * np.pi * t)
vals = t
x_vals = x(vals)

fig, axs = plt.subplots(1)
fig.suptitle("Reprezentarea semnalului x")
axs.plot(vals, x_vals, color = 'purple')
plt.savefig("Ex2-pct-b.pdf")
plt.show()

#c)sawtooth signal cu frecventa 240Hz
def sawtooth(t):
    return 2 * (t - np.floor(t + 1 / 2))
    
vals = np.linspace(0, 0.1, 7200, endpoint = False)

x = lambda t: sawtooth(240 * t)

x_vals = np.array([x(val) for val in vals])

fig, axs = plt.subplots(1, figsize = (12, 5))
fig.suptitle("Reprezentarea semnalului x")
axs.plot(vals, x_vals, color = 'purple')
plt.savefig("Ex2-pct-c.pdf")
plt.show()


#d) square signal cu frecventa de 300Hz
def square(t):
    return np.sign(np.sin(2*np.pi*300*t))

vals = np.linspace(0, 0.02, 720)

x = lambda t: square(t)
x_vals = x(vals)

fig, axs = plt.subplots(1, figsize = (10, 5))
fig.suptitle("Reprezentarea semnalului x")
axs.plot(vals, x_vals, color = 'purple')
plt.savefig("Ex2-pct-d.pdf")
plt.show()

#e) semnal generat cu random
mat = np.random.rand(128, 128)

plt.imshow(mat, cmap = 'gray')
plt.savefig("Ex2-pct-e.pdf")
plt.show()

#f)semnal facut cum vreau eu
mat = np.zeros((128, 128))
for i in range(0, 128):
    for j in range(0, 128):
        if i * i + j * j <= 2000:
            mat[i][j] = 1

plt.imshow(mat)
plt.savefig("Ex2-pct-f.pdf")
plt.show()
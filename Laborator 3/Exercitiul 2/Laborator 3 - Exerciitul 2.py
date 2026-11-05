import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f = 7

x = lambda t: np.sin(2 * np.pi * f * t)

omegas = [1, 2, 4, 7]
vals = np.linspace(0, 1, fs, endpoint=False)

# Figura 1 : varianta statica
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

z = x(vals) * np.exp(-2j * np.pi * vals)
Ox = z.real
Oy = z.imag
dist = np.sqrt(Ox ** 2 + Oy ** 2)

axs[0].plot(vals, x(vals), color='purple')
axs[0].scatter(vals, x(vals), c=dist, cmap='magma', s=10)
axs[1].scatter(Ox, Oy, c=dist, cmap='magma', s=10)
axs[1].set_aspect('equal')
plt.savefig("Ex2_Fig1_Statica.pdf")
plt.show(block=True)


# Figura 2 : varianta statica
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs = axs.flatten()

for i in range(len(omegas)):
    omega = omegas[i]
    z = x(vals) * np.exp(-2j * np.pi * omega * vals)

    Ox = z.real
    Oy = z.imag
    dist = np.sqrt(Ox ** 2 + Oy ** 2)

    axs[i].scatter(Ox, Oy, c=dist, cmap='magma', s=10)
    axs[i].set_aspect('equal')
    axs[i].set_title(f'omega = {omega}')

plt.tight_layout()
plt.savefig("Ex2_Fig2_Statica.pdf")
plt.show(block=True)

#Figura 1 : varianta animata
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

z = x(vals) * np.exp(-2j * np.pi * vals)
Ox = z.real
Oy = z.imag
dist = np.sqrt(Ox ** 2 + Oy ** 2)

axs[0].set_xlim(0, 1)
axs[0].set_ylim(-1.1, 1.1)

axs[1].set_xlim(-1.1, 1.1)
axs[1].set_ylim(-1.1, 1.1)
axs[1].set_aspect('equal')

c1 = axs[0].scatter([], [], color='red', s=50)
c2 = axs[1].scatter([], [], color='red', s=50)

plt.show(block=False)

for k in range(0, fs, 10):
    j = min(k + 10, fs)

    axs[0].plot(vals[max(0, k-1):j], x(vals[max(0, k-1):j]), color='purple')
    axs[0].scatter(vals[k:j], x(vals[k:j]),c=dist[k:j], cmap='magma', vmin=0, vmax=1, s=10)
    axs[1].scatter(Ox[k:j], Oy[k:j], c=dist[k:j], cmap='magma', vmin=0, vmax=1, s=10)

    c1.remove()
    c2.remove()

    c1 = axs[0].scatter(vals[j-1], x(vals[j-1]), color='red', s=50)
    c2 = axs[1].scatter(Ox[j-1], Oy[j-1], color='red', s=50)

    plt.pause(0.05)

plt.show(block=True)

# Figura 2 animata
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs = axs.flatten()

curente = []

for i in range(len(omegas)):
    axs[i].set_xlim(-1.1, 1.1)
    axs[i].set_ylim(-1.1, 1.1)
    axs[i].set_aspect('equal')
    axs[i].set_title(f'omega = {omegas[i]}')
    c = axs[i].scatter([], [], color='red', s=50)
    curente.append(c)

plt.show(block=False)

for k in range(0, fs, 10):
    j = min(k + 10, fs)

    for i in range(len(omegas)):
        omega = omegas[i]
        z = x(vals[k:j]) * np.exp(-2j * np.pi * omega * vals[k:j])
        Ox = z.real
        Oy = z.imag
        dist = np.sqrt(Ox ** 2 + Oy ** 2)

        axs[i].scatter(Ox, Oy, c=dist, cmap='magma', vmin=0, vmax=1, s=10)
        curente[i].remove()
        curente[i] = axs[i].scatter(Ox[-1], Oy[-1], color='red', s=50)
    plt.pause(0.05)


plt.show(block=True)

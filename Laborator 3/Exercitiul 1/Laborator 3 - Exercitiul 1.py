import numpy as np
import matplotlib.pyplot as plt

n = 8

vals = np.arange(n)
P = np.outer(vals, vals)

F = np.exp(-2j * np.pi * P / n) / np.sqrt(n)
print(F)

F_H = F.conj().T

I = np.identity(n, dtype=complex)
print(np.allclose(F @ F_H, I))

fig, axs = plt.subplots(n, figsize=(n, 2 * n))
for i in range(n):
    axs[i].plot(vals, F[i].real, color='blue', label='Real')
    axs[i].plot(vals, F[i].imag, color='red', linestyle='--', label='Imaginar')
    axs[i].legend()
plt.savefig("Ex1.pdf")
plt.show()
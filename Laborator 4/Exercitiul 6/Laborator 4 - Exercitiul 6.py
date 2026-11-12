import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, x = wavfile.read("vocale.wav")

N = len(x)
dim_grup = int(N / 100)
pas = dim_grup // 2

grupuri = []

for i in range(0, N, pas):
    grup = x[i:i + dim_grup]
    F = np.fft.fft(grup, n=dim_grup)
    grupuri.append(np.abs(F[:dim_grup // 2]))

M = np.array(grupuri).T

fig, axs = plt.subplots(figsize=(10, 6))
axs.imshow(np.log1p(M), aspect = 'auto', origin = 'lower', extent = [0, N / fs, 0, fs / 2], cmap = 'inferno')
axs.set_xlabel('Timp (s)')
axs.set_ylabel('Frecventa (Hz)')
axs.set_ylim(0, 4000)
plt.savefig("Ex6.pdf")
plt.show()
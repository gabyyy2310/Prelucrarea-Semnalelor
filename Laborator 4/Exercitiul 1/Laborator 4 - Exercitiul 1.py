import numpy as np
import matplotlib.pyplot as plt
import time

def DFT(x):
    n = len(x)
    vals = np.arange(n)
    P = np.outer(vals, vals)

    F = np.exp(-2j * np.pi * P / n)
    return F @ x

def FFT(x):
    n = len(x)
    if n == 1:
        return x
    even_fft = FFT(x[ :: 2])
    odd_fft = FFT(x[1 :: 2])
    omega = np.exp(-2j * np.pi / n) #"prima" radacina primitiva de ord n a unitatii
    unities = omega ** np.arange(n // 2) #primele n/2 unitati
    
    return np.concatenate((even_fft + unities * odd_fft, even_fft - unities * odd_fft))

N = [128, 256, 512, 1024, 2048, 4096, 8192]
time_DFT = []
time_FFT = []
time_FFT_np = []

for n in N:
    x = np.random.rand(n)
    
    start = time.perf_counter()
    DFT(x)
    end = time.perf_counter()
    time_DFT.append(end - start)
    
    start = time.perf_counter()
    FFT(x)
    end = time.perf_counter()
    time_FFT.append(end - start)
    
    start = time.perf_counter()
    np.fft.fft(x)
    end = time.perf_counter()
    time_FFT_np.append(end - start)
    
fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(N, time_DFT, color = 'red', label = "Viteza DFT")
axs.plot(N, time_FFT, color = 'blue', label = 'Viteza FFT implemenata de noi')
axs.plot(N, time_FFT_np, color = 'purple', label = "Viteza FFT din numpy")
axs.set_yscale('log')
plt.legend()
plt.savefig("Ex1.pdf")
plt.show()
    
    


    
        
#aceeai amplitudine si frecventa; faza variabila

import numpy as np
import matplotlib.pyplot as plt

f = 200

x1 = lambda t: np.sin(2 * np.pi * f * t)
x2 = lambda t: np.sin(2 * np.pi * f * t + np.pi / 6)
x3 = lambda t: np.sin(2 * np.pi * f * t + np.pi / 4)
x4 = lambda t: np.sin(2 * np.pi * f * t + np.pi / 3)

vals = np.linspace(0, 0.1, 1000, endpoint = False)
vals_x1 = x1(vals)
vals_x2 = x2(vals)
vals_x3 = x3(vals)
vals_x4 = x4(vals)

fig, axs = plt.subplots(4, figsize = (8, 8))
axs[0].plot(vals, vals_x1, color = 'purple')
axs[1].plot(vals, vals_x2, color = 'blue')
axs[2].plot(vals, vals_x3, color = 'orange')
axs[3].plot(vals, vals_x4, color = 'red')
plt.savefig("Ex2-4faze.pdf")
plt.show()

z = np.random.normal(0, 1, 1000)

z_norm = np.linalg.norm(z)
x_norm = np.linalg.norm(vals_x1)

gamma = []

for snr in [0.1, 1, 10, 100]:
    gamma.append(x_norm / (z_norm * np.sqrt(snr)))
   
fig, axs = plt.subplots(4, figsize = (8, 8))
for i in range(len(gamma)):
    vals_x = vals_x1 + z * gamma[i]
    axs[i].plot(vals, vals_x, color = "red")
plt.savefig("Ex2-adaugare-zgomot.pdf")
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    

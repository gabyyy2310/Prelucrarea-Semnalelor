import numpy as np
import matplotlib.pyplot as plt

vals = np.linspace(-np.pi / 2, np.pi / 2, 1000)

fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(vals, np.sin(vals), color = 'red')
axs.plot(vals, vals, color = 'blue')
axs.set_title('Comportamentului functiilor sin si identitate in jurul lui 0')
plt.savefig("Ex8-aprox_sin(x)_cu_x.pdf")
plt.show()

err = lambda t: np.abs(np.sin(t) - t)

fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(vals, err(vals), color = 'purple')
axs.set_title('Reprezentarea erorii absolute pentru aproximarea lui sin(x) cu x')
plt.savefig("Ex8-eroarea_absoluta_sin(x)_x.pdf")
plt.show()

f = lambda t: (t - 7 * t ** 3 / 60) / (1 + t ** 2 / 20)
fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(vals, f(vals), color = 'red')
axs.plot(vals, np.sin(vals), color = 'blue')
axs.set_title("Comportamentul functiilor sin si f in jurul lui 0")
plt.savefig("Ex8-aprox_sin(x)_pade.pdf")
plt.show()

err_pade = lambda t: np.abs(np.sin(t) - f(t))

fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(vals, err_pade(vals), color = 'purple')
axs.set_title('Reprezentarea erorii absolute pentru aproximarea lui sin(x) cu f(x)')
plt.savefig("Ex8-eroarea_absoluta_sin(x)_pade.pdf")
plt.show()

fig, axs = plt.subplots(1, figsize = (8, 8))
axs.plot(vals, err(vals), color = 'purple')
axs.plot(vals, err_pade(vals), color = 'orange')
axs.set_title("Compararea erorilor folosind axa logaritmica")
axs.set_yscale('log')
plt.savefig("Ex8-compararea_erorilor_folosind_axa_logaritmica.pdf")
plt.show()








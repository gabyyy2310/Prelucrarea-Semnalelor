import numpy as np
import matplotlib.pyplot as plt

fs = 1000
x = lambda t: np.sin(200 * np.pi * t)

vals = np.linspace(0, 1, fs, endpoint = False)

vals_0 = np.array([vals[i] for i in range(fs) if i % 4 == 0])
vals_1 = np.array([vals[i] for i in range(fs) if i % 4 == 1])

x_vals = x(vals)
x0_vals = x(vals_0)
x1_vals = x(vals_1)

fig, axs = plt.subplots(2, figsize = (8, 8))
axs[0].plot(vals, x_vals, color = 'purple')
axs[0].set_title('Sinusoida cu frecventa de esantionare 1000Hz')
axs[1].plot(vals_0, x0_vals, color = 'blue')
axs[1].set_title('Sinusoida cu frecventa de esantionare decimata la 1/4')
plt.savefig("Ex7-primele_doua_ploturi.pdf")
plt.show()

#pt punctul a): perioada functiei sinusoidale se modifica (pt valoarea 100 a frecventei) de la 10 la 5
#in general, avem sin(pi*f*n/500) si sin(pi*f*k/125); perioadele se modifica tinand cont si de gct(f, 250)
#si gcd(f, 1000)
#daca f/125 ar fi irational, al doilea semnal al fi dens
#deci daca am lua un sir f_n cu f_n/125 -> un numar irational, am observa ca se acopera din ce in ce mai bine spatiul


fig, axs = plt.subplots(3, figsize = (8, 8))
axs[0].plot(vals, x_vals, color = 'purple')
axs[0].set_title('Sinusoida cu frecventa de esantionare 1000Hz')
axs[1].plot(vals_0, x0_vals, color = 'blue')
axs[1].set_title('Sinusoida cu frecventa de esantionare decimata la 1/4')
axs[2].plot(vals_1, x1_vals, color = 'pink')
axs[2].set_title('Sinusoida cu frecventa de esantionare decimata la 1/4, incepand cu al doilea termen')
plt.savefig("Ex7-toate_ploturile.pdf")
plt.show()

#diferenta intre ultimele doua plot-uri este punctul de pornire -> difera faza
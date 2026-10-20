import numpy as np
import matplotlib.pyplot as plt

fs = 400

x = lambda t: np.sin(fs * np.pi * t)
y = lambda t: np.sin(fs *np.pi * t / 2)
z = lambda t: np.sin(0 * t)

vals = np.linspace(0, 1, fs, endpoint = False)
x_vals = x(vals)
y_vals = y(vals)
z_vals = z(vals)

fig, axs = plt.subplots(3, figsize = (8, 8))
axs[0].plot(vals, x_vals, color = 'green')
axs[1].plot(vals, y_vals, color = 'orange')
axs[2].plot(vals, z_vals, color = 'blue')
plt.savefig("Ex6.pdf")
plt.show()

#teoretic, primul semnal e sin(400pi * n/400)=sin(n*pi)=0
#totusi pe grafic se vad mici oscilatii, mai mici decat 1e-13 -> erori de calcul ale calculatorului din cauza
#modului in care se efectueaza calcului si aprox lui pi
#la al doilea semnal e sin(n*pi/2) care ia valoei egale cu 0, 1 sau -1 in functie de restul mod 4 al lui n
#ultimul semnal e constant egal cu 0
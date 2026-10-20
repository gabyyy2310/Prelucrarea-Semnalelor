#semnal sinusoidal cu amplitudine, faza si frecventa alese de noi
#semnal de tip cosinus a i pe orizontul de timp ales sa fie egal cu cel de tip sinus

import numpy as np
import matplotlib.pyplot as plt

a = 2 #amplitudinea
phi = 0 #faza
f = 200 #frecventa fundamentala

semnal_sin = lambda t: a * np.sin(2 * np.pi * t * f + phi)
semnal_cos = lambda t: a * np.cos(2 * np.pi * t * f + phi - np.pi / 2)

vals = np.linspace(0, 0.1, 1000, endpoint = False)
sin_vals = semnal_sin(vals)
cos_vals = semnal_cos(vals)

fig, axs = plt.subplots(2, figsize = (5, 5))
axs[0].plot(vals, sin_vals, color = "purple")
axs[1].plot(vals, cos_vals, color = "blue")
plt.savefig("Ex1.pdf")
plt.show()
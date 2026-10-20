import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

vals = np.linspace(0, 0.4, 1600, endpoint = False)
x = lambda t: np.sin(400 * np.pi * t)
a_vals = x(vals)

y = lambda t: np.sin(2000 * np.pi * t)
b_vals = y(vals)

final_vals = np.concatenate((a_vals, b_vals))

sd.play(final_vals, 4000)

#semnalul cu frecventa mai mare e mai ascutit, iar cel cu frecventa mai mica e mai grav
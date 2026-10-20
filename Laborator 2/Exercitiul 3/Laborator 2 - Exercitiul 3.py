import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy as sp
from scipy.io import wavfile

#exercitiul 2
#a) semnal sinusoidal de frecventa 400Hz si 1600 esantioane
vals = np.linspace(0, 0.4, 1600, endpoint = False)
x = lambda t: np.sin(800 * np.pi * t)
a_vals = x(vals)


sd.play(a_vals, 4000)
sd.wait()

#b)semnal sinusoidal de frecventa 800Hz, care sa dureze 3 secunde
t = np.linspace(0, 3, 9000, endpoint = False)

x = lambda t: np.sin(1600 * np.pi * t)
vals = t
b_vals = x(vals)

sd.play(b_vals, 3000)
sd.wait()

#pentru c si d am crescut durata (fata de lab 1) ca sa le pot auzi
#c)sawtooth signal cu frecventa 240Hz
def sawtooth(t):
    return 2 * (t - np.floor(t + 1 / 2))
    
vals = np.linspace(0, 1, 72000, endpoint = False)

x = lambda t: sawtooth(240 * t)

c_vals = np.array([x(val) for val in vals])

sd.play(c_vals, 72000)
sd.wait()

#d) square signal cu frecventa de 300Hz
def square(t):
    return np.sign(np.sin(2*np.pi*300*t))

vals = np.linspace(0, 0.2, 7200, endpoint = False)

x = lambda t: square(t)
d_vals = x(vals)

sd.play(d_vals, 36000)
sd.wait()

#salvam ca wav semnalul c
rate = 72000

wavfile.write("Ex3-semnal_c.wav", rate, c_vals.astype(np.float32))

rate, x = wavfile.read("Ex3-semnal_c.wav")










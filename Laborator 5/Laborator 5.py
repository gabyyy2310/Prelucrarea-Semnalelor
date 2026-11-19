import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#a)
#Stim ca N = nr esantioane = 18288, observate din ora in ora
#Vrem sa aflam frecventa de esantionare
#intervalul dintre doua esantioane este de o ora, adica 3600 secunde
#deci frecventa de esantionare este fs = 1 / 3600


#b)
#Ce interval de timp acopera cele N = 18288 esantioane
#intr-o zi sunt observate 24 de esantioane (din ora in ora)
#18288:24 = 762 => 762 zile
#un an = 365 zile => 2 ani = 730 zile (aprox)
#deci esantioanele corespund la 762 de zile (aprox 2 ani si 32 de zile)

#c)
#vrem sa aflam frecventa maxima prezenta in semnal
#cu teorema Nyquist-Shannon avem ca frecventa maxima este egala cu fs / 2 = 1 / 7200

#d)
x = np.genfromtxt("Train.csv", delimiter = ",", skip_header = 1, usecols = 2)
N = len(x)
fs = 1 / 3600
X = np.fft.fft(x)

modul_X = np.abs(X / N)
modul_X = modul_X[ : N // 2]

f = fs * np.linspace(0, N / 2, N // 2, endpoint = False) / N

fig, axs = plt.subplots(1, 2, figsize = (16, 8))
axs[0].plot(x)
axs[0].set_xlabel("Esantioane")
axs[0].set_ylabel("Numar de masini")
axs[0].set_title("Semnalul original")
axs[1].plot(f, modul_X)
axs[1].set_title("Modulul Transformatei Fourier")
plt.savefig("Ex1_d.pdf")
plt.show()

#e) Avem componenta continua?
#In graficul din dreapta observam un spike in valoarea 0 
#Valoarea in 0 din acel grafic este componenta continua a semnalului
#notam componenta continua cu x0

x0 = X[0] / N

#ca sa o eliminam trebuie sa o scadem din semnal
#consideram y semnalul x din care am scazut valoarea x0

y = x - x0.real

#f)
modul_Y = modul_X.copy()
modul_Y[0] = 0

indici_max = np.argsort(modul_Y)[-4:][::-1]
print(f"{'Modul':<15} {'Frecventa (Hz)':<22} {'Perioada (zile)':<20}")
for i in indici_max:
    perioada = 1 / (f[i] * 3600 * 24)
    print(f"{modul_Y[i]:<15.8f} {f[i]:<22.8e} {perioada:<20.2f}")
    
#obervam ca perioadele corespunzatoare sunt T = 762 zile, T/2, 1 zi si T/3
#Componenta cu perioada de o zi corespunde variatiei zilnice a traficului

#g)
#from datetime import datetime
date = np.genfromtxt("Train.csv", delimiter=",", skip_header=1, usecols=1, dtype=str)
for s in range(1001, N):
    data = datetime.strptime(date[s], "%d-%m-%Y %H:%M")
    if data.weekday() == 0 and data.hour == 0:
        break

print("Esantion de start:", s)
print("Data:", date[s])
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
axs[0].plot(x)
axs[0].set_title("Semnalul complet")
axs[0].set_xlabel("Esantioane")
axs[0].set_ylabel("Numar de masini")
axs[1].plot(np.arange(s, s + 30 * 24), x[s:s + 30 * 24])
axs[1].set_title("Traficul pe o luna")
axs[1].set_xlabel("Esantioane")
axs[1].set_ylabel("Numar de masini")
plt.savefig("Ex1_g.pdf")
plt.show()

#h)
#Pentru a estima ziua vom proceda in felul urmator:
#grupam esantioanele cate 24 (practic, grupam pe zile) si calculam media numarului de masini pentru fiecare zi
#in material e specificat ca in weekend traficul e mai redus
#incercam sa gasim doua zile conscutive care pare ca au medii semnificativ mai mici ca restul, le etichetam ca Sambata si Duminica
#restul zileleor se completeaza automat

#Putem proceda analog si pentru luna, grupand esantioanele cate (aprox) 30 * 24
#aici e o problema: numarul variabil de zile al unei luni
#am pitea folosi gruparea si eventuale tendinte/luna pt a estima aproximativ (diferentele de +/- o zi nu ar fi foarte relevante)

#Anul e dificil de aflat; nu pare ca sunt sanse sa se gaseasca aspecte specifice anumitor ani

#In aceasta metoda ar fi cateva probleme:
    #anumite sarbatori legale, zile libere etc ar putea produce neconcordante
    #spre exemplu am avea o saptamana care s-ar termina cu sambata-duminica, iar din analiza, urmatoarele doua zile ar 
    #avea tot numar mici de masini si ar fi tot sambata si duminica, ceea ce nu e corect

#i)
#Eliminam componentele de frecventa inalta
#Alegem sa pastram frecventele corespunzatoare unor perioade de cel putin 8 ore

fc = 1 / (8 * 3600)

freq = np.fft.fftfreq(N, d = 3600)

X_filtrat = X.copy()
X_filtrat[np.abs(freq) > fc] = 0

x_filtrat = np.fft.ifft(X_filtrat).real

fig, axs = plt.subplots(1, 2, figsize = (16, 6))
axs[0].plot(x[s:s + 30 * 24])
axs[0].set_title("Semnalul original")
axs[0].set_xlabel("Esantioane")
axs[0].set_ylabel("Numar de masini")
axs[1].plot(x_filtrat[s:s + 30 * 24])
axs[1].set_title("Semnalul filtrat")
axs[1].set_xlabel("Esantioane")
axs[1].set_ylabel("Numar de masini")
plt.savefig("Ex1_i.pdf")
plt.show()




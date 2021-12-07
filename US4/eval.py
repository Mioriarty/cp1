# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time
from lu_crout import myLU
from lu_crout import elimination

# Initialisiere gemeinsame Parameter
# Matrix A des aufgestellten Grundstoff-Gleichungssystems
A = np.array([[1, 1, 0], [4, 0, 2], [0, 2, 1]])

# Inhomogenitätenvektoren für diverse Glühweinzutaten
ingredients = {
    "Fruktose": [6, 12, 6],
    "Ethanol": [2, 6, 1],
    "Weinsäure": [4, 6, 6],
    "Zitronensäure": [6, 8, 7]
}


# Beispiel 1: Glühweinproduktion
# Zerlege Matrix A

L, U = myLU(A)

# Berechne für jede Glühweinzutat die nötige Menge an Grundstoffen
# Konsolenausgabe
for n in range(1, 5):
    print(f"\nN={n}:")
    for name, quantities in ingredients.items():
        sol = elimination(L, U, n * np.array(quantities))
        print(f"{name}: C{sol[0]} H{sol[1]} O{sol[2]}")


# Beispiel 2: Laufzeit der LU-Zerlegung in Abhängigkeit von der Matrixgröße
ns = np.arange(2, 50, 1)
times = np.zeros(len(ns))

def calcTime(i):
    A = np.random.rand(ns[i], ns[i])
    start = time.perf_counter()
    myLU(A)
    times[i] = (time.perf_counter() - start)
    print(ns[i])

import multiprocessing.dummy as mp
p = mp.Pool(8)
p.map(calcTime, range(len(ns)))
p.close()
p.join()


# Darstellung
fig, ax = plt.subplots()
ax.set_title("Berechnungsdauer in Abh. von der Matrixgröße")
ax.set_xlabel("Matrixgröße N")
ax.set_ylabel("Berechnungsdauer t in s")
ax.plot(ns, times, label="Gemessene t(N)")

cube = lambda x : 2.5e-7*x**3
ax.plot(ns[3:], cube(ns[3:]), label="t(N) ~ N³")
ax.legend(loc='best')
plt.show()

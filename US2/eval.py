# -*- coding: utf-8 -*-
""" Dieses Skript führt die Funktion 'intrect' aus.

Die numerische Integration nach der Rechteckregel wird an den Funktionen
f(x) = x, f(x) = x^2 und f(x) = exp(x) durchgeführt. Anhand der berechneten
Stammfunktionen und Flächeninhalte wird das Konvergenzverhalten zum jeweiligen
analytischen Ergebnis verglichen.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from intrect import intrect

# Berechnung der exakten Flächeninhalte

linArea = 1/2 * 10**2
quadArea = 1/3 * 10**3
expArea = np.exp(10) - 1

# Integrationsfehler in Abhängingkeit von der Schrittweite der Teilintervalle
# logarithmisch äquidistanter Vektor der Schrittweiten
hs = np.logspace(-4, -1, 400)

# Initialisierung der arrays
linErrors  = []
quadErrors = []
expErrors  = []

# Definition der Funktionen (vgl. MatLab function handles)
lin = lambda x : x
quad = lambda x : x**2
exp = np.exp

a = 0
b = 10

# Schleife über alle h zur Berechnung von Integral und dessen Fehler

for h in hs:
    linErrors.append(abs(linArea - intrect(lin, a, b, h)[0]))

    quadErrors.append(abs(quadArea - intrect(quad, a, b, h)[0]))

    expErrors.append(abs(expArea - intrect(exp, a, b, h)[0]))


# logarithmischer Plot Fehler vs. Schrittweite h
# Darstellung als Linienplot

fig, ax = plt.subplots()
ax.set_title("Integrationsfehler in Abh. vom Stützstellenabstand h")
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Stützstellenabstand h')
ax.set_ylabel('Integrationsfehler E')
ax.plot(hs, linErrors, label="f(x) = x")
ax.plot(hs, quadErrors, label="f(x) = x²")
ax.plot(hs, expErrors, label="f(x) = exp(x)")


# Plotbeschriftung
ax.legend(loc='best')
fig.tight_layout()

plt.show()


# Abhaengigkeit der Integrationskonstante vom linken Intervallrand
# am Bsp. der Stammfunktion F von x^2

# rechte Intervallgrenze fest
b = 4

# linke Intervallgrenze mit verschiedenen Werten
aas = [0, 0.5, 1, 1.5, 2, 3]
h = 1e-2

fig, ax = plt.subplots()

for a in aas:
    # Auswertung des numerischen Integrals
    _, xVals, yVals = intrect(quad, a, b, h)

    # Darstellung als Linienplot
    ax.plot(xVals, yVals, label="a=%.1f" % a)


# Plotbeschriftung für alle Graphen im selben Plot
ax.legend(loc='best')
ax.set_title("Stammfunktion in Abh. vom linken Intervallrand a")
ax.set_xlabel("Parameter x")
ax.set_ylabel("Funktswert der Stammfunktion F(x)")
plt.show()
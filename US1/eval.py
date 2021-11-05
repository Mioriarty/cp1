""" Dieses Skript führt die Funktion 'diffquot' aus.

Es wird die numerische Ableitung der Funktion sin(x) mittels rechtsseitigem
Differenzenquotienten berechnet und mit ihrer analytischen Ableitung, cos(x),
verglichen. Dabei wird insbesondere das Verhalten der Differenz aus beiden
untersucht.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.lib import hsplit
from diffquot import diffquot

# Aufruf der Ableitungsfunktion und Speichern des Ergebnis in zwei Variablen.
# Wir nutzen hier die Werte für den Beispielaufruf der Funktion diffquot.
fhandle = np.sin  # Definition der input-Funktion
a = -50           # untere Intervallgrenze
b = 50            # obere Intervallgrenze
h = 0.1           # Schrittweite

xwerte, ableitung = diffquot(fhandle, a, b, h)

# Darstellung der Funktion und ihrere Ableitung in einem Plot
fig, ax = plt.subplots()
ax.plot(xwerte, np.sin(xwerte), label='sin(x)')
ax.plot(xwerte, ableitung, label='num. diff.')
ax.set_title('Funktion und ihre Ableitung')
ax.legend(loc='best')
fig.tight_layout()
plt.show()


anzahl_h = 50
h_min = 0.001
h_max = 3

# äquidistanter Vektor im Intervall [h_min, h_max] der Länge anzahl_h
hs = np.linspace(h_min, h_max, anzahl_h)

# Intialisierung des Gesamtfehler-Vektors
errors = []

for h in hs:

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h)

    # berechne die analytische Ableitung
    analytAbleitung = np.cos(xwerte)

    # berechne den Gesamtfehler für jedes h
    error = np.sum(h * np.abs(ableitung - analytAbleitung) )
    errors.append(error)


# Darstellung als Linienplot
fig, ax = plt.subplots()
ax.set_title("Gesamtfehler in Abhängigkeit von h")
ax.set_xlabel("Quantisierungsabstand h")
ax.set_ylabel("Gesamtfehler")
ax.plot(np.array(hs), np.array(errors), label="Fehler")
plt.show()

# lokaler Fehler für feste Schrittweiten

# überschreibe h erneut

hs = [0.1, 1, 3]

fig, ax = plt.subplots()

for h in hs:

    # Aufruf von diffquot für jeden Wert von h
    xwerte, ableitung = diffquot(fhandle, a, b, h)

    # berechne die analytische Ableitung
    analytAbleitung = np.cos(xwerte)

    # Darstellung des Betrags der Differenz beider Ableitungen als Linienplot
    ax.plot(xwerte, ableitung - analytAbleitung ,label='h=%.1f' % h)

# Plotbeschriftung
ax.legend(loc='best')
ax.set_xlabel('Koordinate x')
ax.set_ylabel('lokaler Fehler')
ax.set_title('Lokaler Fehler')
fig.tight_layout()
plt.show()

# mein eigener plot
xwerte, ableitung = diffquot(fhandle, -5, 5, 0.2)
analytAbleitung = np.cos(xwerte)

fig, ax = plt.subplots()
ax.set_title("Vergleich numerische und analytische Ableitung")
ax.plot(xwerte, analytAbleitung, label="analytisch")
ax.plot(xwerte, ableitung, label="numerisch")
ax.legend(loc='best')
fig.tight_layout()
plt.show()
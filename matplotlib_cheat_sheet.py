
# =============================================================================
# Computational Physics 1 - WS 2020/2021
# Seminar 03
# =============================================================================


#########################################################
#                                                       #
#                   Numpy                               #
#                                                       #
#########################################################

import numpy as np
from numpy.core.function_base import linspace
from numpy.lib.function_base import sinc

# Definition eines Vektors (direkt)
#     /1\         /4\
# x = |2| und y = |5|
#     \3/         \6/

x = np.array([1,2,3])
y = np.array([4,5,6])


# Vektoraddition:
#         /1\   /4\   /1 + 4\   /5\
# X + Y = |2| + |5| = |2 + 5| = |7|
#         \3/   \6/   \3 + 6/   \9/


print(x + y)


# Skalar-Produkt (inneres Produkt): 
#         /1\   /4\
# X . Y = |2| . |5| = 1*4 + 2*5 + 3*6 = 32
#         \3/   \6/

print(np.dot(x, y))

# Skalierung: c * x
#             /1\   /2 * 1\   /2\
# c * X = 2 * |2| = |2 * 2| = |4|
#             \3/   \2 * 3/   \6/

print(2 * x)

# Hadamard Produkt (elementenweise Multiplikation):
#     /1\         /4\            /1 * 4\   /4 \
# X = |2| und Y = |5| -> X * Y = |2 * 5| = |10|
#     \3/         \6/            \3 * 6/   \18/

print(x * y)

# Kreuzprodukt:
#     /1\         /4\            /2*6 - 3*5\   /-3 \
# X = |2| und Y = |5| -> X x Y = |3*4 - 1*6| = | 6 |
#     \3/         \6/            \1*5 - 2*4/   \-3 /

print(np.cross(x, y))

# Dyadisches Produkt (Äußeres Produkt):
#     /1\         /4\T            /1*4 1*5 1*6\   /4  5  6 \
# X = |2| und Y = |5|  -> X o Y = |2*4 2*5 2*6| = |8  10 12|
#     \3/         \6/             \3*4 3*5 3*6/   \12 15 18/

print(np.outer(x, y))

# Deklaration einer Matrix:
#     /1 2 3\
# M = |4 5 6|
#     \7 8 9/

m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


# Matrixmultiplikation:
#     /1 2 3\        /11 22 33\
# M = |4 5 6| und G =|44 55 66|  
#     \7 8 9/        \77 88 99/
#         /1*11 + 2*44 + 3*77 ...\   /330 ... ...\
# M . G = |...                   | = |... ... ...|
#         \...                   /   \... ... .../


g = np.array([ [11,22,33],
               [44,55,66],
               [77,88,99]])


print(np.dot(m, g))

# Direktzugriff auf die Elemente:

s = np.array([1,2,3,4,5,6,7])
print(s[0])


# Interval der Elemente:

s = np.array([1,2,3,4,5,6,7,8,-9,10])
print(s[1:3])
print(s[1::2])


# Elemente nach einer Bedingung:
# wtf
print(s[(s>3) & (s < 7)])

 
# Direktzugriff zur Elementen einer Matrix:
#     /1  5 3\
# I = |2  8 0|
#     \10 5 9/

print(m[1, 2]) # Zeile, Spalte


# Submatrix:
#     /1  5 3\         /5\                      /5 3\
# I = |2  8 0| -> IV = |8| -> IH = [2 8 0] IB = |8 0|
#     \10 5 9/         \5/                      \5 9/

print(m[:, 1:3])



#########################################################
#                                                       #
#                   MATPLOTLIB                          #
#                                                       #
#########################################################

# Im Folgenden Dokument werden wir anhand von Beispielen die 
# graphische Ausgabe "matplotlib" näher kennenlernen.
# Dafür ist es wichtig, dass das entsprechende Modul eingebunden wurde:
# import matplotlib.pyplot as plt


import matplotlib.pyplot as plt


# 100 x-Werte zwischen -20 und 20
# y-Werte (z.B. sinc(x))
"""
x = np.linspace(-20, 20, 100)
y = 0.5 * np.sin(x) / x

plt.figure()
plt.plot(x, y)

plt.axhline(np.mean(y), color='r', ls='--')

plt.title("sinc(x) = sin(x) / x")
plt.show()

"""



# Aufruf der ersten Grafik
# Plottet Datenpunkte über Zähler

# Gesamt-Mittelwert wird horizontal eingefügt
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html

# Titel der Graphik

# Ausgabebefehl

# =============================================================================
# TIPP:
# Grafik in einem separaten Fenster:
#    Voreinstellungen - IPython Konsole - Grafik - Backend: AUTOMATISCH
#   (Spyder Neustart erforderlich!)
# =============================================================================


#########################################################
#                                                       #
#  Mehrfach Diagramme                                   #
#                                                       #
#########################################################


# Anwendung der matplotlib-Interface zur Erzeugung von Subplots

"""
x = linspace(-8, 8, 50)
y1 = np.sin(2*x)
y2 = np.cos(x)
y3 = x**2
y4 = np.tan(x)

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0, 0].plot(x, y1)
ax[0, 0].set_title("Sinus")

ax[1, 0].scatter(x, y2)
ax[1, 0].set_title("Cosinus")

ax[0, 1].bar(x, y3)
ax[0, 1].set_title("Quadratische Fkt")

ax[1, 1].plot(x, y4)
ax[1, 1].set_title("Tangenz")

plt.savefig("plot1.png", dpi=699)

plt.show()

"""


#erstellen eines Graphikobjektes mit 2x2 Untergraphiken

# 20 x-Werte zwischen -8 und 8
# Berechnung y-Werte
# y1-Werte
# y2-Werte
# y3-Werte
# y4-Werte

# erste Untergraphik, Position 0,0 -> oben links, Kurve
#Titel
# Punktewolke
#Titel
# Balkendiagramm
#Titel

#Titel#Titel

# Grafik speichern - transparent für Hintergrund

# Ausgabebefehl





#########################################################
#                                                       #
#              Anpassung der Achsen und Markierungen    #
#                                                       #
#########################################################

fig, ax = plt.subplots()

x = np.linspace(-8, 8, 200)
y = np.sin(2*x)

ax.plot(x, y, label="sin(2x)", color="b")
ax.set_xlabel("Gemeinsame x-Achse")
ax.set_ylabel("y1")

ax2 = ax.twinx()
ax2.plot(x-0.5, 3*y, label="sin(6x)")
ax2.set_ylabel("y2", fontsize = 20)

plt.show()


# =============================================================================
# Zeichen       Beschreibung
# =============================================
# axis      [‘x’ | ‘y’ | ‘both’] - verwendte Achse; default: ‘both’.
# reset     [True | False] - setzt alle Parameter zurück, default: False
# which     [‘major’ | ‘minor’ | ‘both’] Haupt-,/Hilfs-gitter default: ‘major’
# direction [‘in’ | ‘out’ | ‘inout’] - Orientierung der Marken
# length    Länge der Markierung
# width     Dicke der Markierung
# color     Farbe der Markierung (mpl color)
# pad       Abstand zwischen Markierung und Beschriftung
# labelsize Beschriftungsgröße in px oder string (‘large’)
# labelcolor Beschriftungsfarbe (mpl color)
# colors    Farbe der Markierung und Beschriftung auf einen Wert (mpl color)
# zorder    Tick and label zorder.
# bottom, top, left, right - [bool | ‘on’ | ‘off’] - entsprechende Markierungen zeichnen
# labelbottom, labeltop, labelleft, labelright - Boolean or [‘on’ | ‘off’], entsprechende Beschriftung


#########################################################
#                                                       #
# Legenden plotten                                      #     
#                                                       #
#########################################################


#erstellen eines Graphikobjektes

fig, ax = plt.subplots()

x = np.linspace(0, 10, 100)# 100 x-Werte zwischen 0 und 10
y = x*3.0+x**2-0.1*x**3# y-Werte
ymeas = y + 0.5*np.random.randn(y.size)# ymeas-Werte welche sich randomisiert um y-Werte befinden

ax.plot(x, ymeas, 'rx', label = 'measurement')# Plot der ymeas-Werte
ax.plot(x,y, 'k-', label = 'theory')# Plot der y-Werte

#ax.legend(loc="upper left") # lower left, upper right, ...

ax.legend(loc = 'best')

plt.show()

# Achsen einzeln ansprechen und Legende manuell erzeugen.
#erstellen eines Graphikobjektes

fig, ax = plt.subplots()
 
li1, = ax.plot(x, ymeas, 'rx', label = 'measurement') # Plot der ymeas-Werte
li2, = ax.plot(x,y, 'k-', label = 'theory')# Plot der y-Werte#li1: ymeas als individuelles Plot Objekt
#li2: y als individuelles Plot Objekt
 
# Legende manuell
ax.legend([li1, li2],['measurement', 'theory'])


#########################################################
#                                                       #
#              Colormesh für 2D-Plots                   #
#                                                       #
#########################################################


dx = 0.01# Schrittweite
dy = 0.01
x = np.arange(1, 5, dx)
y = np.arange(1, 5, dy)

X, Y = np.meshgrid(x,y)
#TIPP: meshgrid dreht die Spalten und Reihen automatisch. Eingriff: X, Y = np.meshgrid(x, y, indexing="ij")
Z = np.sin(X)**10+np.cos(10+Y*X)*np.cos(X)# Berechnung der Z-Werte

fig, ax0 = plt.subplots()
cmap = plt.get_cmap('PiYG')# Festlegung der Farb-Tafel
# Alternative Farben: https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html

im = ax0.pcolormesh(X,Y,Z, cmap = cmap) # Erzeugung des Farbgitters mit Farbauswahl

fig.colorbar(im, ax = ax0) # Farblegende

# Überschrift
ax0.set_title('Science Stuff')




#########################################################
#                                                       #
#  Quiver für 2D-Plots mit Pfeilen (Vektorfeld)         #
#                                                       #
#########################################################

'quiver(X, Y, U, V, C) - 2D-Feld von Pfeilen'
# X,Y: Position der Pfeile; 
# U, V: x- und y-Komponenten der Vektoren; 
# C: optionaler Wert zum Einfärben (z.B. Intensität)

x = y = np.arange(-2, 2.2, 0.2)
X, Y = np.meshgrid(x,y)

z = X*np.exp(-X**2-Y**2)

DX, DY = np.gradient(z)
C = np.sqrt((DX/2)**2+(DY/2)**2)# Array zur Einfärbung (z.B. Gauß-Funktion)

fig, ax = plt.subplots()
ax.quiver(x,y,DX,DY,C)


plt.show()





#########################################################
#                                                       #
#               Stream (Feldlinien)                     #
#                                                       #
#########################################################


' Elektrische Feldlinien (+ und -)'

x = y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(x,y)


# Coulomb-Gesetz
Ex = (X + 1)/((X+1)**2 + Y**2) - (X - 1)/((X-1)**2 + Y**2)
Ey = Y/((X+1)**2 + Y**2) - Y/((X-1)**2 + Y**2)

fig, (ax_pn, ax_pp) = plt.subplots(ncols = 2)

ax_pn.streamplot(X,Y,Ex,Ey, density = 1.5)

ax_pn.set_aspect('equal')

ax_pn.plot(-1,0,'or')#Positive elektrische Ladung
ax_pn.plot(1,0,'ob')#Negative elektrische Ladung

ax_pn.set_title('E-Feldlinien\n positive und negative Ladungen')

' Elektrische Feldlinien (+ und +)'

# Coulomb-Gesetz
Ex = (X + 1)/((X+1)**2 + Y**2) + (X - 1)/((X-1)**2 + Y**2)
Ey = Y/((X+1)**2 + Y**2) + Y/((X-1)**2 + Y**2)

ax_pp.streamplot(X,Y,Ex,Ey, density = 1)

ax_pp.set_aspect('equal')

ax_pp.plot(-1,0,'or')#Positive elektrische Ladung
ax_pp.plot(1,0,'or') #positive elektrische Ladung

ax_pp.set_title('E-Feldlinien\n positive und positive Ladungen')




# =============================================================================
# TIPP:
#  Beispiele: https://matplotlib.org/3.1.0/gallery/index.html
# =============================================================================

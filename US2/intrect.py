import numpy as np
from numpy.core.fromnumeric import cumsum

def intrect(fhandle, a, b, h):
    """ Numerische Integration einer beliebigen integrierbaren Funktion mittels
    der Rechteckregel.

    Argumente
    ---------
    fhandle : function
        die zu integrierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Teilintervalle

    Output: 3-Tupel
    ---------------
    area : float
        Berechnete Fläche
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    stamm_funk : float
        Berechnete Funktionswerte der Stammfunktion (1-d array)

    Funktionsaufruf
    ---------------
        area, xwerte, stamm_funk = intrect(fhandle, a, b, h)

    Beispiel
    --------
        area, xwerte, stamm_funk = intrect(np.exp, 0, 10, 0.01)
    """


    # Mittelpunkte der Intervalle ermitteln
    # --> Vektor der Intervall-Mittelpunkte durch Verschiebung um h/2
    xVals = np.arange(a + h, b, h)

    # Funktionswerte an den Intervallmittelpunkten
    yVals = fhandle(xVals - h/2)

    # Aufsummierung von Teilintervallen durch cumsum
    yIntVals = cumsum(yVals) * h

    # Berechnung der Fläche
    area = yIntVals[-1] - yIntVals[0]

    # Berechnung der xwerte für Darstellung der Stammfunktion, jeweils am
    # rechten Rand des Teilintervalls

    # linke Intervallgrenze hinzufügen
    xVals = np.concatenate([[ a ], xVals])
    yIntVals = np.concatenate([[ fhandle(a) * h ], yIntVals])

    return area, xVals, yIntVals

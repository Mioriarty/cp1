def diffquot(fhandle, a, b, h):
    """ Berechne den rechtseitigen Differenzenquotienten.

    Argumente
    ---------
    fhandle : function
        die zu differenzierende Funktion
    a : int
        unter Intervallgrenze
    b : int
        obere Intervallgrenze
    h : float
        Schrittweite der Differentiation

    Output: 2-Tupel
    ------
    xwerte : float
        Definitionsbereich der Funktion (1-d array)
    ableitung : float
        Ergebnisvektor mit der numerischen Ableitung (1-d array)

    Funktionsaufruf
    ---------------
        xwerte, ableitung = diffquot(fhandle, a, b, h)

    Beispiel
    --------
        xwerte, ableitung = diffquot(np.sin, -10, 10, 0.1)
    """

    import numpy as np

    if(b <= a):
        raise ValueError("a must be smaller than b")

    # Bestimmung des Definitionsbereichs der Funktion
    numVals = abs(int((b - a) / h))
    x = np.linspace(a, b, numVals)

    # Evaluierung der Funktion 'fhandle'
    values = fhandle(x)

    # Berechung der numerischen Ableitung mittels des rechtsseitigen
    # Differenzenquotienten
    # ich mache das so, um die Anzahl an potentiell teuren Funktionsaufruf zu reduizieren
    derivative = (values[1:] - values[:-1]) / h


    return (x[:-1], derivative)

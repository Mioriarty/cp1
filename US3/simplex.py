# -*- coding: utf-8 -*-
import numpy as np

def simplex(fhandle, x_start, N_max, p):
    """ SIMPLEX Minimumssuche mittels des Downhill-Simplex Verfahrens.

    Beispiel
    --------

    fhandle = himmelblau
    x_start = [0 0]
    N_max   = 1e3
    p       = 1e-15
    x_min, f_min, N = simplex(fhandle, x_start, N_max, p)

    Argumente
    ---------
    fhandle : function
        Die zu minimierende Funktion

    x_start : float
        Startpunkt des Simplex

    N_max : int
        Maximale Anzahl an Iterationen

    p : float
        Genauigkeit in x oder f

    Output
    ------
    x_min : float
        Punkt (x,y) des Funktionsminimums (2-tupel)

    f_min : float
        Funktionsminimum

    N : int
        Anzahl der benötigten Schritte
    """

    simplex = [
        np.array(x_start),
        np.array([x_start[0]+lambda_, x_start[1]]),
        np.array([x_start[0], x_start[1]+lambda_])
    ]

    yVals = [
        fhandle(simplex[0]),
        fhandle(simplex[1]),
        fhandle(simplex[2])
    ]
    
    

    for N in range(N_max+1):
        # best, middle, worst
        indexOrder = [yVals.index(y) for y in sorted(yVals)]

        if calcSimplexSize(simplex) < p and calcVariance(yVals) < p:
            return simplex[indexOrder[0]], yVals[indexOrder[0]], N

        # mirror the simplex
        movedPoint = movedSimplexPoint(simplex, indexOrder[2], alpha_)
        movedPointYVal = fhandle(movedPoint)

        if movedPointYVal < yVals[indexOrder[0]]:
            # better than bast point
            # expansion
            expandedPoint = movedSimplexPoint(simplex, indexOrder[2], gamma_)
            expandedPointYVal = fhandle(expandedPoint)

            if expandedPointYVal < movedPointYVal:
                simplex[indexOrder[2]] = expandedPoint
                yVals[indexOrder[2]] = expandedPointYVal
            else:
                simplex[indexOrder[2]] = movedPoint
                yVals[indexOrder[2]] = movedPointYVal
            
        
        elif movedPointYVal < yVals[indexOrder[1]]:
            # better than middle point
            # keep mirror
            simplex[indexOrder[2]] = movedPoint
            yVals[indexOrder[2]] = movedPointYVal

        
        else:

            if movedPointYVal < yVals[indexOrder[2]]:
                # at least better than worst point
                # no need to change the index order
                simplex[indexOrder[2]] = movedPoint
                yVals[indexOrder[2]] = movedPointYVal

            contractedPoint = movedSimplexPoint(simplex, indexOrder[2], beta_)
            contractedPointYVal = fhandle(contractedPoint)

            if contractedPointYVal < yVals[indexOrder[2]]:
                simplex[indexOrder[2]] = contractedPoint
                yVals[indexOrder[2]] = contractedPointYVal
            else:
                # compress
                simplex[(indexOrder[0] + 1) % 3] = (simplex[(indexOrder[0] + 1) % 3] + simplex[indexOrder[2]]) / 2
                simplex[(indexOrder[0] + 2) % 3] = (simplex[(indexOrder[0] + 2) % 3] + simplex[indexOrder[2]]) / 2

    indexOrder = [yVals.index(y) for y in sorted(yVals)]
    return simplex[indexOrder[0]], yVals[indexOrder[0]], N_max
        

def calcVariance(values : list) -> float:
    return np.std(values)

def calcSimplexSize(simplex : list) -> float:
    return abs(simplex[0][0] * (simplex[1]-simplex[2])[1] + simplex[1][0] * (simplex[2] - simplex[0])[1] + simplex[2][0] * (simplex[0] - simplex[1])[1]) / 2
    

def movedSimplexPoint(simplex : list, pointIndex : int, scale : float) -> list:
    p1 = simplex[(pointIndex + 1) % 3]
    p2 = simplex[(pointIndex + 2) % 3]

    middle = (p1 + p2) / 2

    return (1 + scale) * (middle - simplex[pointIndex]) + simplex[pointIndex]
    

#==================================================
# Initialisierung
#==================================================

# Die Skalierungsfaktoren des Downhill-Simplex Verfahrens
alpha_  = 1.0  # empfohlener Faktor für die Spiegelung
beta_   = 0.5  # empfohlener Faktor für die Kontraktion
gamma_  = 2.0  # empfohlener Faktor für die Expansion
lambda_ = 0.1  # empfohlene Größe des Startsimplex

# -*- coding: utf-8 -*-

import numpy as np

def checkSquareMatrix(A):
    if not (len(A.shape) == 2 and A.shape[0] == A.shape[1]):
        raise ValueError("Matrices musst be square")

def elimination(L, U, b):
    '''Löst ein Gleichungssystem A*x=b durch Vorwärts- und Rückwärtselimination
    für die LU-Zerlegung von A=L*U.

    Beispiel
    --------
    x = elimination(L, U, b)

    Eingabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix

    b : float (vector)
        Inhomogenitätsvektor des Gleichungssystems

    Ausgabe
    -------
    x : float (vector)
        Lösungsvektor
    '''

    checkSquareMatrix(L)
    checkSquareMatrix(U)
    if U.shape[0] != L.shape[0]:
        raise ValueError("L and U has to have the same shape")
    
    if L.shape[0] != b.shape[0]:
        raise ValueError("The ")

    n = L.shape[0]

    # Vorwärtselimination
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i-1))

    # Rückwärtselimination
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (1 / U[i, i]) * (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n)))

    return x


def myLU(A):
    '''LU-Zerlegung einer Matrix A=L*U mittels Crout-Algorithmus.

    Beispiel
    --------
    L, U = myLU(A)

    Eingabe
    -------
    A : float (2d array)
        Die zu zerlegende Matrix

    Ausgabe
    -------
    L : float (2d array)
        Obere Dreiecksmatrix

    U : float (2d array)
        Untere Dreiecksmatrix
    '''
    
    checkSquareMatrix(A)

    n = A.shape[0]

    L = np.identity(n)
    U = A

    for j in range(n):
        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j]
            U[i, j] = 0

            for k in range(j+1, n):
                U[i, k] = U[i, k] - L[i, j]* U[j, k]

    return L, U

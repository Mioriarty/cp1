from simplex import simplex
from himmelblau import himmelblau

import numpy as np
import matplotlib.pyplot as plt


print(simplex(himmelblau, [0, 0], 1000, 1e-13))
print(simplex(himmelblau, [-4, 3], 1000, 1e-13))
print(simplex(himmelblau, [-4, -3], 1000, 1e-13))
print(simplex(himmelblau, [5, 5], 1000, 1e-13))


xs = np.linspace(-5, 5, 50)
ys = np.linspace(-5, 5, 50)

def inRange(p1, p2):
    EPSILON = 0.01
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 < EPSILON

def getFinalValIndex(x, y):
    
    p, val, N = simplex(himmelblau, [x, y], 250, 1e-15)

    if inRange(p, np.array([3, 2])):
        return 1
    elif inRange(p, np.array([-2.80511808695274485, 3.13131251825057297])):
        return 2
    elif inRange(p, np.array([-3.77931025337774689, -3.28318599128616941])):
        return 3
    elif inRange(p, np.array([3.58442834033049174, -1.84812652696440355])):
        return 4
    else:
        print([x, y], p, val, N)
        return 0
    

finalIndices = np.array([[getFinalValIndex(x, y) for x in xs] for y in ys[::-1]])

fig = plt.figure()
plt.imshow(finalIndices, extent=(-5, 5, -5, 5))
plt.title("Gefundenes Minimum in Abh. vom Startwert")
plt.xlabel("x - Koordinate")
plt.ylabel("y - Koordinate")
plt.show()


Ns = np.arange(10, 950, 1)

dists = [np.linalg.norm(simplex(himmelblau, (-1, -1), N, 0)[0] - np.array([-3.77931025337774689, -3.28318599128616941])) for N in Ns]

fig, ax = plt.subplots()
ax.set_title("Abstand vom Minimum in Abh. vom den maximalen Schritten")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Anzahl der maximalen Schritten")
ax.set_ylabel("Abstand vom Minimum")
ax.plot(Ns, dists)

plt.show()

fig = plt.figure()
yVals = np.array([[himmelblau(np.array([x, y]))**(0.6) for x in xs] for y in ys[::-1]])
plt.imshow(yVals, extent=(-5, 5, -5, 5), cmap="cividis")
plt.title("Höhenkarte der Himmelblaufunktion")
plt.xlabel("x - Koordinate")
plt.ylabel("y - Koordinate")
plt.colorbar()
plt.show()
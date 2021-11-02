from numpy import linspace, sin, pi

h = 0.001
x = linspace(0, 2*pi, int(2*pi/h))
y = sin(x)

print(y)
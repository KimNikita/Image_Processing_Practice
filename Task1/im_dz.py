import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.linspace(-m.pi*4, m.pi*4, 100)
y = [m.sin(xi)/xi for xi in x]
plt.title("sin(x)/x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

x1 = np.linspace(-10, -0.1, 100)
x2 = np.linspace(0.1, 10, 100)
y1 = [(xi**3-6*xi**2+3*xi)/abs(xi) for xi in x1]
y2 = [(xi**3-6*xi**2+3*xi)/abs(xi) for xi in x2]
plt.title("(x^3-6x^2+3x)/|x|")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x1, y1, "b", x2, y2, "b")
plt.show()

x = np.linspace(-10, 10, 100)
y = [xi**2-2*xi-4-abs(xi**2+xi-2) for xi in x]
plt.title("x^2-2x-4-|x^2+x-2|")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

x1 = np.linspace(-10, 1.9, 100)
x2 = np.linspace(2.1, 10, 100)
y1 = [1/(xi-2)+1 for xi in x1]
y2 = [1/(xi-2)+1 for xi in x2]
plt.title("1/(x-2)+1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x1, y1, "b", x2, y2, "b")
plt.show()

x = np.linspace(0, 1, 100)
y = [m.sqrt(xi)*m.sqrt(1-xi) for xi in x]
plt.title("x^0.5*(1-x)^0.5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)
plt.show()

x = np.linspace(-m.pi, m.pi, 100)
y1 = [2**m.sin(xi) for xi in x]
y2 = [2**xi for xi in x]
plt.title("2^sin(x) && 2^x")
plt.xlabel("x")
plt.ylabel("y1, y2")
plt.grid()     
plt.plot(x, y1, x, y2)
plt.show()
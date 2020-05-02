import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

origin = 0


class phase:

    def __init__(self, mag, ang):
        self.mag = mag
        self.ang = ang

    def deg_car(self):
        self.mag = self.mag * math.cos(self.ang)
        self.ang = self.mag * math.sin(self.ang)


phaseA = phase(1, 0)
phaseB = phase(1, 120)
phaseC = phase(1, 240)

print(phaseA.mag)
print(phaseA.ang)

# phaseA.deg_car() #calls the method in the class that convertes from polar to rectangular

# print(phaseA.mag) #prints the polar to rectangular after the method is called
# print(phaseA.ang) #prints the polar to rectangular after the method is called


# print(phaseB)
# print(phaseC)

# a operator 1<120
a = complex(-0.5+0.866j)
# Symmetrical Components Matrix
A = np.array([[1, 1, 1],
              [1, a**2, a],
              [1, a, a**2]], dtype=complex)

# print(A)

Ainv = np.linalg.inv(A)  # calculates the inverse of a matrix
# creates a 1x3 matrix
sys = np.array([[1.13+1.2j], [0.52-1.22j], [-0.803-1.33j]])
sym = Ainv.dot(sys)
# print(sym[1])
# print(cmath.polar(sym[1]))


# def car_pol(x, y):  # x is the axis and y is the y axis
#     cn = complex(x, y)
#     a = abs(cn)
#     b = np.angle(cn, deg=True)

#     return(a, b)

ax = plt.subplot(111, projection='polar')
plt.arrow(math.radians(phaseA.ang), origin, 0, phaseA.mag, width=0.015,
          edgecolor='red', lw=2, zorder=5)
plt.arrow(math.radians(phaseB.ang), origin, 0, phaseB.mag, width=0.015,
          edgecolor='yellow', lw=2, zorder=5)
plt.arrow(math.radians(phaseC.ang), origin, 0, phaseC.mag, width=0.015,
          edgecolor='blue', lw=2, zorder=5)


ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Symmetrical Components", va='bottom')
plt.show()

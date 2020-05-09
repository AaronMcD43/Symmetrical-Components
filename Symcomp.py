import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

#Input Values
phaseA = [1.65, 46.8]
phaseB = [1.32, -67]
phaseC = [1.56, -121]

#Function takes two arguments as magnitude and angle and converts them to a complex number
def deg_car(mag, ang):                    
    x = mag * math.cos(math.radians(ang))
    y = mag * math.sin(math.radians(ang))
    return(complex(x, y))


def plotting(xs, ys, x, y, c):
    plt.quiver(xs, ys, x, y, angles='xy', scale_units='xy',
               scale=1, width=0.005, color=c)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

def car_deg(x,y):
    cn = complex(x,y)
    a = abs(cn)
    b = np.angle(cn, deg = True)
    return (a,b)
    
#calling the function to convert the phase values from degrees to cartesian co-ordinates
phaseAcar = deg_car(phaseA[0], phaseA[1])
phaseBcar = deg_car(phaseB[0], phaseB[1])
phaseCcar = deg_car(phaseC[0], phaseC[1])


# a operator 1<120
a = complex(-0.5+0.866j)
a2= a*a
# Symmetrical Components A Matrix
A = np.array([[1, 1, 1],
              [1, a**2, a],
              [1, a, a**2]], dtype=complex)

# calculates the inverse of the A matrix
Ainv = np.linalg.inv(A)  

# creates a 3x1 matrix
sys = np.array([[deg_car(phaseA[0], phaseA[1])],
                [deg_car(phaseB[0], phaseB[1])],
                [deg_car(phaseC[0], phaseC[1])]])

# calculated symmetrical components
sym = Ainv.dot(sys)  

I0A = sym[0]
I1A = sym[1]
I2A = sym[2]
I0B = I0A
I1B = I1A * a2
I2B = I2A * a
I0C = I0A
I1C = I1A * a
I2C = I2A * a2



plotting(0, 0, phaseAcar.real, phaseAcar.imag, 'red')
plotting(0, 0, phaseBcar.real, phaseBcar.imag, 'yellow')
plotting(0, 0, phaseCcar.real, phaseCcar.imag, 'blue')

plotting(0, 0, I1A.real, I1A.imag, 'black')
plotting(I1A.real, I1A.imag, I2A.real, I2A.imag, 'black')
plotting(I2A.real + I1A.real, I2A.imag + I1A.imag,
         I0A.real, I0A.imag, 'black')

plotting(0, 0, I1B.real, I1B.imag, 'black')
plotting(I1B.real, I1B.imag, I2B.real, I2B.imag, 'black')
plotting(I2B.real + I1B.real, I2B.imag + I1B.imag,
         I0B.real, I0B.imag, 'black')

plotting(0, 0, I1C.real, I1C.imag, 'black')
plotting(I1C.real, I1C.imag, I2C.real, I2C.imag, 'black')
plotting(I2C.real + I1C.real, I2C.imag + I1C.imag,
         I0C.real, I0C.imag, 'black')


plt.show()




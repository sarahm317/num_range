import numpy as np
import math

def getPoints(A0, A1, n=100):
    theta = np.linspace(start=0, stop=2*math.pi, num=n)
    z1 = A0[0,0]; z2 = A0[1,1]
    z3 = A1[0,0]; z4 = A1[1,1]

    c1 = [complex(abs(z3)*math.cos(theta0), abs(z3)*math.sin(theta0)) + z1 for theta0 in theta]
    c2 = [complex(abs(z4)*math.cos(theta0), abs(z4)*math.sin(theta0)) + z2 for theta0 in theta]

    return np.append(c1,c2)
    
def getCoords(A0,A1, n=100):
    comp = getPoints(A0,A1,n=n)
    x = comp.real
    y = comp.imag
    return np.column_stack([x,y])


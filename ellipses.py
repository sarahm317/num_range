from numpy.linalg import norm,eig,det
from numpy import trace as tr
import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

def getOneEllipse(A):
    evals = eig(A)[0]
    f1 = evals[0]
    f2 = evals[1]
    center = 1/2*tr(A)
    x0 = center.real
    y0 = center.imag

    majAxVec_x = f2.real - f1.real
    majAxVec_y = f2.imag - f1.imag
    theta = cmath.phase(complex(majAxVec_x,majAxVec_y))/(2*np.pi)*360 # in DEGREES

    b = np.sqrt(tr(np.matmul(A,np.transpose(np.conjugate(A)))) - abs(f1)**2 - abs(f2)**2).real
    a = np.sqrt(b**2 + abs(f1-f2)**2).real
    elParam = [(x0,y0), a, b, theta]
    return elParam

def makePatch(A):
    [center, a, b, theta] = getOneEllipse(A)
    return Ellipse(xy=center, width=a, height=b, angle=theta)

def getEllipses(A0Mat, A1Mat, n):
    j = complex(0,1)
    theta = np.linspace(0, 2*np.pi, num = n)
    z = np.cos(theta) + j*np.sin(theta)

    els = [None] * n

    for x in range(n):
        A = A0Mat + z[x]*A1Mat
        els[x] = makePatch(A)

    return els
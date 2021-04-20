import numpy as np
import cmath
import LA
from scipy import optimize as opt


j = complex(0,1)
n = 500 # number of points around unit circle generated
theta = np.linspace(0, 2*np.pi, num = n)
z = np.cos(theta) + j*np.sin(theta) # z on unit circle


A0 = [[2j, 0], [0, j]]
A0Mat = np.matrix(A0)

A1 = [[0.01,0],[0,0]]
A1Mat = np.matrix(A1)

# (c,d) is predicted center of the circle
c = 0
d = 2

AArray = n*[1] # creates list of all possible A0 + zA1 matrices for z on unit circle
for i in range(n):
    AArray[i] = A0Mat + z[i]*A1Mat - complex(c,d)  * np.identity(2)

rad = n*[1] # vector that will store the numerical radius of all possible A0 + zA1

for i in range(n):
    mat = AArray[i] #extracts first matrix from array

    matStar = mat - 1/2*LA.tr(mat)*np.identity(2)

    etaNorm = LA.norm(matStar)**2 - 2*abs(LA.det(matStar))

    evals = LA.eig(mat)[0]
    lambda1 = evals[0]
    lambda2 = evals[1]
    lambda1Norm = abs(lambda1)
    lambda2Norm = abs(lambda2)

    if lambda1Norm == lambda2Norm: #case 1 in paper
        lambdaNorm = abs(lambda1)

        evecs = LA.eig(mat)[1]
        v1 = evecs[0]
        v2 = evecs[1]

        theta = abs(np.arccos(np.dot(v1,v2.T)/(LA.norm(v1)*LA.norm(v2))))/2

        x = etaNorm/(2*lambdaNorm*np.sin(theta))

        if x >= np.tan(theta):
            rad[i] = lambdaNorm*(x*np.sin(theta) + np.cos(theta))
        elif x < np.tan(theta):
            rad[i] = lambdaNorm * np.sqrt(1 + x**2)

    else: # case 2 in paper
        normDif = abs(lambda1 - lambda2)
        normSum = abs(lambda1 + lambda2)
        R = lambda1 * np.conj(lambda2)
        Rreal = (R + np.conj(R))/2
        a = 1/2 * np.sqrt(etaNorm**2 + normDif**2)
        c = normDif/2
        x0 = abs(lambda2Norm**2 - lambda1Norm**2)/(2*normDif)
        y0 = 1/normDif * np.sqrt((abs(lambda1*lambda2)**2 - abs(Rreal)**2)/2)

        def f(h):
            return (a**2 - h**2)*(a**2*x0 + c**2*h)**2 - (1/4 * a**2 * y0**2 * etaNorm**2 * h**2)
        
        #sol = opt.root_scalar(f, args = (), x0 = 0, x1 = a)
        sol = opt.fsolve(f,x0 = a)
        h = sol

        #h = sol.root

        rad[i] = a * (1 + x0/h) * np.sqrt(1 + (y0**2 * h**2 * c**2)/(a**2 * x0 + c**2 * h)**2)

print(np.std(rad)) # small number indicates that the numerical radius remains constant as z ranges around unit circle

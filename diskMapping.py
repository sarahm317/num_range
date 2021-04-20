import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import plottingFunctions

theta = np.linspace(start=0, stop=2*math.pi, num=200)
n = 2


# get disk points
x = np.cos(theta)
y = np.sin(theta)
z = x + complex(0,1) * y

a_0 = complex(2,2)
a_1 = 4

# toPlot = a_0 + a_1*z+ a_2*z**2 + a_3*z**3
toPlot = a_0 + a_1*z
real = toPlot.real
imaginary = toPlot.imag

plottingFunctions.plotMapping(real,imaginary)
import cmath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle

n= 10
nPolys = 10
A0 = np.diagflat([1]*(n-1),1)
A1 = np.zeros((n,n))
A1[n-1,0] = 1

j = complex(0,1)
theta = np.linspace(0, 2*np.pi, num = nPolys)
z = np.cos(theta) + j*np.sin(theta)

circle = Circle((0,0),1)
circle.set_fill(False)
circle.set_edgecolor('crimson')
circle.set_linewidth(3)
circle.set_facecolor(None)
patches = [circle]

for i in range(nPolys):
    p = [1] + [0]*(n-1) + [-z[i]]
    roots = np.roots(p)
    angles = np.sort([cmath.phase(root) for root in roots])
    roots = np.cos(angles) + j*np.sin(angles)
    x = roots.real
    y = roots.imag
    coords = np.stack((x,y),axis=1)


    poly = Polygon(xy=coords,closed=True)
    poly.set_edgecolor('royalblue')
    poly.set_facecolor('lightsteelblue')
    poly.set_linewidth(1)
    patches.append(poly)

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

# Draw major and minor grid lines
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

p = PatchCollection(patches,match_original=True)
ax.add_collection(p)
ax.fill(linewidth=2)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

path = "/Users/sarahmantell/Desktop/ToeplitzProject/MAA_Poster/"
filename = path + "poly_n10_rev001.png"
plt.savefig(filename,dpi=300)

plt.show()
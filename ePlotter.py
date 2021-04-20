import numpy as np
import cmath
import matplotlib.pyplot as plt
import LA
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle

def getEllipses(A0Mat, A1Mat, n):

    j = complex(0,1)
    theta = np.linspace(0, 2*np.pi, num = n)
    z = np.cos(theta) + j*np.sin(theta)

    els = [None] * n

    for x in range(n):
        A = A0Mat + z[x]*A1Mat

        evals = LA.eig(A)[0]
        f1 = evals[0]
        f2 = evals[1]
        center = 1/2*LA.tr(A)
        x0 = center.real
        y0 = center.imag

        majAxVec_x = f2.real - f1.real
        majAxVec_y = f2.imag - f1.imag
        theta = cmath.phase(complex(majAxVec_x,majAxVec_y))/(2*np.pi)*360 # in DEGREES

        b = np.sqrt(LA.tr(np.matmul(A,np.transpose(np.conjugate(A)))) - abs(f1)**2 - abs(f2)**2)
        a = np.sqrt(b**2 + abs(f1-f2)**2)

        els[x] = Ellipse(xy = (x0,y0),width = a, height = b, angle = theta)

    return els
    
def plotEllipses(els, **kwargs):
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

    for e in els:
        ax.add_artist(e)
        e.set_edgecolor('cornflowerblue')
        e.set_fill(False)

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

    plt.axis("equal")

    xlims = kwargs.get('xlims',None)
    ylims = kwargs.get('ylims',None)

    if xlims is not None and ylims is not None:
        plt.xlim(xlims[0],xlims[1])
        plt.ylim(ylims[0],ylims[1])

    filename = kwargs.get('filename', None)

    if filename is not None:
        plt.savefig(filename,dpi=300)

    circles = kwargs.get('circles', None)

    plt.show()

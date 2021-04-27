import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

def plotEllipses(els,font=18, graphed = False, xlims = None, ylims=None, filename=None):
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': font})
    collection = PatchCollection(els, alpha=0.3,
                                ec = 'darkblue', fc = 'cornflowerblue', lw = 2)
    ax.add_collection(collection)

    
    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    
    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=font, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=font, labelpad=-21, y=1.02, rotation=0)
    
    if graphed == True:    
        # Draw major and minor grid lines
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    plt.axis("equal")

    if xlims is not None and ylims is not None:
        plt.xlim(xlims[0],xlims[1])
        plt.ylim(ylims[0],ylims[1])

    if filename is not None:
        plt.savefig(filename,dpi=300, bbox_inches="tight", pad_inches=0, transparent=True)
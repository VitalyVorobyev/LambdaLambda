""" """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from pars import pars
from pdfs import csecPhi

def plotPhi(p=pars):
    """ """
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)

    plt.figure(num=1, figsize=(6, 4))

    x_tick = np.linspace(-np.pi, np.pi, 9)
    x_label = [
        r'$-\pi$',
        r'$-\frac{3\pi}{4}$',
        r'$-\frac{\pi}{2}$',
        r'$-\frac{\pi}{4}$',
        r'$0$',
        r'$+\frac{\pi}{4}$',
        r'$+\frac{\pi}{2}$',
        r'$+\frac{3\pi}{4}$',
        r'$+\pi$'
    ]

    xi = [-1., 0., 1.]
    lbl = ['-1', '0', '+1']
    phi = np.linspace(-np.pi, np.pi, 251)
    cosphi = np.cos(phi)
    pdf = [csecPhi(cosphi, a) for a in xi]

    for l,y in zip(lbl,pdf):
        plt.plot(phi, y, label=r'$\xi=${}'.format(l))

    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=14)

    plt.ylim([0., 1.05*max(y)])
    plt.xlabel(r'$\phi_1$ (rad)', fontsize=16)
    plt.legend(loc='best', fontsize=12)
    plt.grid()
    plt.tight_layout()

    plt.savefig('../plots/phi3Dist.pdf')
    plt.savefig('../plots/png/phi3Dist.png')

    plt.show()

if __name__ == '__main__':
    plotPhi()

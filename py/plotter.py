#! /usr/bin/python3

""" Visualization tools """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot1D(events, dim, label):
    """ 1D hist plot """
    x = events[:,dim]
    hist, edges = np.histogram(x, bins=40, density=True)
    edges = 0.5 * (edges[1:] + edges[:-1])
    plt.plot(edges, hist, linestyle='none', marker='.', label=label)
    return max(hist)

def plot2D(fnum, events, dim1, dim2, label1, label2, fname, xi):
    """ 2D plot """
    x = events[:,dim1]
    y = events[:,dim2]

    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.figure(num=fnum, figsize=(6, 5))
    plt.hist2d(x, y, bins=30, cmap=plt.cm.seismic, normed=True)
    plt.colorbar()

    props = dict(boxstyle='round', facecolor='w', alpha=0.9)
    plt.text(0.45, 1.1, r'$\xi = {}$'.format(xi), transform=plt.gca().transAxes, 
        fontsize=18, verticalalignment='top', bbox=props)

    plt.axis('equal')
    plt.xlabel(label1, fontsize=16)
    plt.ylabel(label2, fontsize=16)
    plt.grid()
    plt.tight_layout()

    plt.savefig('../plots/{}.pdf'.format(fname))
    plt.savefig('../plots/png/{}.png'.format(fname))

    plt.show()

def plotTheta(d0, d1, d1n):
    """  """
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)

    plt.figure(num=1, figsize=(6, 4))
    dim1 = 0

    mval = [
        plot1D(d0, dim1, r'$\xi=0$'),
        plot1D(d1, dim1, r'$\xi=+1$'),
        plot1D(d1n, dim1, r'$\xi=-1$')
    ]

    plt.ylim([0., 1.05*max(mval)])
    plt.xlabel(r'$\cos{\theta}$', fontsize=16)
    plt.legend(loc='best', fontsize=12)
    plt.grid()
    plt.tight_layout()

    plt.savefig('../plots/cosTheta.pdf')
    plt.savefig('../plots/png/cosTheta.png')

    plt.show()

def plotPhi(d0, d1, d1n):
    """  """
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)

    plt.figure(num=1, figsize=(6, 4))
    dim1 = 4

    mval = [
        plot1D(d0, dim1, r'$\xi=0$'),
        plot1D(d1, dim1, r'$\xi=+1$'),
        plot1D(d1n, dim1, r'$\xi=-1$')
    ]

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

    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=14)

    plt.ylim([0., 1.05*max(mval)])
    plt.xlabel(r'$\phi_2$ (rad)', fontsize=16)
    plt.legend(loc='best', fontsize=12)
    plt.grid()
    plt.tight_layout()

    plt.savefig('../plots/phi2Dist.pdf')
    plt.savefig('../plots/png/phi2Dist.png')

    plt.show()

def main():
    d0 = np.load('../data/ll_xi0.npz')
    d1 = np.load('../data/ll_xi1.npz')
    d1n = np.load('../data/ll_xi1n.npz')
    phsp0, data0 = d0['events'], d0['data']
    phsp1, data1 = d1['events'], d1['data']
    phsp1n, data1n = d1n['events'], d1n['data']

    # plotPhi(data0, data1, data1n)
    plotTheta(data0, data1, data1n)

    # dim1, dim2, dim3 = 0, 1, 3
    # plot2D(2, data0, dim1, dim2, r'$\cos{\theta}$', r'$\cos{\theta_1}$',
    #     'costh_costh1_xi0', 0)

    # plot2D(2, data1, dim1, dim2, r'$\cos{\theta}$', r'$\cos{\theta_1}$',
    #     'costh_costh1_xi1', 1)

    # plot2D(2, data1n, dim1, dim2, r'$\cos{\theta}$', r'$\cos{\theta_1}$',
    #     'costh_costh1_xi1n', -1)

    # plot2D(2, data0, dim1, dim3, r'$\cos{\theta}$', r'$\cos{\theta_2}$',
    #     'costh_costh2_xi0', 0)

    # plot2D(2, data1, dim1, dim3, r'$\cos{\theta}$', r'$\cos{\theta_2}$',
    #     'costh_costh2_xi1', 1)

    # plot2D(2, data1n, dim1, dim3, r'$\cos{\theta}$', r'$\cos{\theta_2}$',
    #     'costh_costh2_xi1n', -1)

if __name__ == '__main__':
    main()

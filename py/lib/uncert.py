""" """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def n(xieta, prec):
    return 0.5 * (1 + xieta**2) / xieta * prec**-2

def phiFit(xi):
    """ """
    return 1.8*10**6 / xi**2

if __name__ == '__main__':
    prec = 0.001

    xi = np.linspace(0.3, 1., 101)
    # y = n(eta * xi, prec)

    eta1, eta2 = 0.17, 0.24
    ym1 = n(eta1*xi, prec)
    ym2 = n(eta2*xi, prec)
    ym3 = phiFit(xi)

    plt.figure(num=1, figsize=(6, 4))
    plt.plot(xi, ym1, label='prec = {:.2f}%, eta = {:.2f}'.format(100*prec, eta1))
    plt.plot(xi, ym2, label='prec = {:.2f}%, eta = {:.2f}'.format(100*prec, eta2))
    plt.plot(xi, ym3, label='prec = {:.2f}%, phiFit'.format(100*prec, eta2))

    plt.xlabel(r'$\xi$', fontsize=16)
    plt.legend(loc='best', fontsize=12)
    plt.xlim(0.3, 1.)
    plt.ylim(0., 1.05 * max(ym1.max(), ym2.max(), ym3.max()))
    plt.grid()
    plt.tight_layout()
    for ext in ['.pdf', '.png']:
        plt.savefig('../' + 'plots/neta{:.2f}'.format(100*prec).replace('.','-') + ext)
    plt.show()

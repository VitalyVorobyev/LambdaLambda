""" Calculations for forward-backward asymmetry """

from pars import pars
from pdfs import aFB
from upolfit import corrMtx, hessErr

import numpy as np

def etaFB():
    """ aFB(1.) """
    return 0.75 * pars.alph1 * (pars.alpha + 1.)/(pars.alpha + 3.)

def dAlr(xi):
    """ """
    xietasq = (xi*etaFB())**2
    return np.sqrt(0.5 * (1. + xietasq)) / xietasq

def dxidAfb():
    """ """
    return 1. / etaFB()

def dxidAlpha(xi):
    """ """
    return -8./3. * aFB(xi, pars) / (1.+pars.alpha)**2 / pars.alph1

def dxidAlph1(xi):
    """ """
    return -4./3 * aFB(xi, pars) * (3. + pars.alpha) / (1. + pars.alpha) / pars.alph1**2

def dxidDphi(xi):
    """ """
    return 0.

def derivs(xi):
    """ Vector of partial derivatives """
    return np.array([dxidAfb(), dxidAlpha(xi), dxidDphi(xi), dxidAlph1(xi)])

def dxi(xi):
    """ sigma(xi) = sqrt(
        (dxi / dAfb   * sigma(Alr))   ** 2 + 
        (dxi / ddPhi  * sigma(dPhi))  ** 2 + ...
        2*(dxi / dAfb) * (dxi / ddPhi) * cov(Afb, dPhi) + ...
    )
    """
    der = derivs(xi)
    errs = np.array([dAlr(xi)] + list(hessErr()[:-1]))
    corr = corrMtx()
    return np.sqrt(
        ((der*errs)**2).sum() +\
        2. * (np.outer(errs, errs) * corr * np.outer(der, der)).sum()
    )

def main():
    """ Unit test """
    xi = 1.
    print('  Abf: {:.3f}'.format(dxidAfb()))
    print(' dphi: {:.3f}'.format(dxidDphi(xi)))
    print('alpha: {:.3f}'.format(dxidAlpha(xi)))
    print('alph1: {:.3f}'.format(dxidAlph1(xi)))
    print('  dxi: {:.3f}'.format(dxi(xi)))

    import matplotlib.pyplot as plt
    plt.rc('font', size=14)

    xi = [0.4, 0.6, 0.8, 0.9]
    n = np.logspace(5, 8)
    for x in xi:
        plt.plot(n, dxi(x) / np.sqrt(n) / x, label=r'$\xi=${:.1f}'.format(x))
    plt.grid()
    plt.semilogx()
    plt.semilogy()
    plt.ylabel(r'$d\xi/\xi$')
    plt.xlabel(r'$N$')
    plt.xlim((10**5, 10**8))
    plt.ylim((10**-4, 20.))
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('fbasym_xi_prec.pdf')
    plt.show()

if __name__ == '__main__':
    main()

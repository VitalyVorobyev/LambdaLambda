""" Calculations for left-right asymmetry """

from pars import pars
from pdfs import aLR
from upolfit import corrMtx, hessErr

import numpy as np

def eta():
    """ aLR(1.) """
    return 3.*np.pi/8.*np.sqrt(1. - pars.alpha**2) / (3.+pars.alpha)*\
        pars.alph1 * pars.cosdphi

def dAlr(xi):
    """ """
    xietasq = (xi*eta())**2
    return np.sqrt(0.5 * (1. + xietasq)) / xietasq

def dxidAlr():
    """ partial derivative of xi over Alr """
    # return 1./aLR(1., pars)
    return 1. / eta()

def dxidDphi(xi):
    """ partial derivative of xi over dPhi """
    return 8. / (3.*np.pi) * aLR(xi, pars) * (pars.alpha + 3) / np.sqrt(1.-pars.alpha**2) *\
        pars.sindphi / pars.cosdphi**2 / pars.alph1

def dxidAlpha(xi):
    """ partial derivative of xi over alpha """
    return 8. / (3.*np.pi) * aLR(xi, pars) / pars.cosdphi *\
        (3.*pars.alpha + 1)/(1.-pars.alpha**2)**(3/2) / pars.alph1

def dxidAlph1(xi):
    """ partial derivative of xi over alpha1 """
    return -8. / (3.*np.pi) * aLR(xi, pars) / pars.cosdphi *\
        (pars.alpha + 2)/np.sqrt(1.-pars.alpha**2) / pars.alph1**2

def derivs(xi):
    """ Vector of partial derivatives """
    return np.array([dxidAlr(), dxidAlpha(xi), dxidDphi(xi), dxidAlph1(xi)])

def dxi(xi):
    """ sigma(xi) = sqrt(
        (dxi / dAlr   * sigma(Alr))  ** 2 + 
        (dxi / ddPhi  * sigma(dPhi)) ** 2 + ...
        2*(dxi / dAlr) * (dxi / ddPhi) * cov(Alr, dPhi) + ...
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
    print('  Alr: {:.3f}'.format(dxidAlr()))
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
    plt.savefig('lrasym_xi_prec.pdf')
    plt.show()

if __name__ == '__main__':
    main()

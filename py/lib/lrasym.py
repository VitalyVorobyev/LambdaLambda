#! /usr/bin/env python3
""" Calculations for left-right asymmetry """

from lib.pars import pars, plotpath
from lib.pdfs import aLR
from lib.fitresreader import readFitRes

from draw.precision import asymPrecision

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
    return np.array([dxidAlpha(xi), dxidDphi(xi), dxidAlph1(xi)])

def errors(data):
    """ """
    return np.array([data['fitres'][key][1] for key in ['alpha', 'dphi', 'alph1']])

def correl(data):
    """ """
    return data['fitcor'][:-1,:-1]

def sigmaCoefs(data):
    """ """
    errs = errors(data)
    corr = correl(data)
    ders = derivs(1.)

    p1 = (np.outer(errs, errs) * corr * np.outer(ders, ders)).sum()
    return (1./eta()**2, p1)

def dxi(xi, n1, n2):
    """ sigma(xi) = sqrt(
        (dxi / dAlr   * sigma(Alr))  ** 2 + 
        (dxi / ddPhi  * sigma(dPhi)) ** 2 + ...
        2*(dxi / dAlr) * (dxi / ddPhi) * cov(Alr, dPhi) + ...
    )
    """
    data = readFitRes('upol', 0., False)
    p0, p1 = sigmaCoefs(data)
    return np.sqrt((p0 + xi**2)/n1 + p1*xi**2 / n2)

def main():
    """ Unit test """
    xi = 1.
    print('  Alr: {:.3f}'.format(dxidAlr()))
    print(' dphi: {:.3f}'.format(dxidDphi(xi)))
    print('alpha: {:.3f}'.format(dxidAlpha(xi)))
    print('alph1: {:.3f}'.format(dxidAlph1(xi)))
    print('  dxi: {:.3f}'.format(dxi(xi, 1, 1)))

    data = readFitRes('upol', 0., False)
    p0, p1 = sigmaCoefs(data)
    print('p0: {:.3f}, p1: {:.3f}'.format(p0, p1))

    import matplotlib.pyplot as plt
    plt.rc('font', size=14)

    xi = [0.4, 0.6, 0.8]
    asymPrecision('lr', xi)

if __name__ == '__main__':
    3.5, 7.5, 6.8
    0.87, 0.91, -0.95




    main()

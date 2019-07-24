#! /usr/bin/env python3
""" Calculations for forward-backward asymmetry """

from lib.pars import pars, plotpath
from lib.pdfs import aFB
from lib.fitresreader import readFitRes

from draw.precision import asymPrecision

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
    return (1./etaFB()**2, p1)

def dxi(xi, n1, n2):
    """ sigma(xi) = sqrt(
        (dxi / dAfb   * sigma(Alr))   ** 2 + 
        (dxi / ddPhi  * sigma(dPhi))  ** 2 + ...
        2*(dxi / dAfb) * (dxi / ddPhi) * cov(Afb, dPhi) + ...
    )
    """
    data = readFitRes('upol', 0., False)
    p0, p1 = sigmaCoefs(data)
    return np.sqrt((p0 + xi**2)/n1 + p1*xi**2 / n2)

def main():
    """ Unit test """
    xi = 1.
    print('  Abf: {:.3f}'.format(dxidAfb()))
    print(' dphi: {:.3f}'.format(dxidDphi(xi)))
    print('alpha: {:.3f}'.format(dxidAlpha(xi)))
    print('alph1: {:.3f}'.format(dxidAlph1(xi)))
    print('  dxi: {:.3f}'.format(dxi(xi, 1, 1)))

    data = readFitRes('upol', 0., False)
    p0, p1 = sigmaCoefs(data)
    print('p0: {:.3f}, p1: {:.3f}'.format(p0, p1))

    xi = [0.4, 0.6, 0.8]
    asymPrecision('fb', xi)

if __name__ == '__main__':
    main()

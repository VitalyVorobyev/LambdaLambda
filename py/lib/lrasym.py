""" Calculations for left-right asymmetry """

from pars import pars
from pdfs import aLR

import numpy as np

def dxidAlr():
    """ partial derivative of xi over Alr """
    return 1./aLR(1., pars)

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

def main():
    """ Unit test """
    print(dxidAlr())
    print(dxidDphi(1.))
    print(dxidAlpha(1.))
    print(dxidAlph1(1.))
    # import matplotlib.pyplot as plt

    # xi = np.linspace(0.3, 1.0, 71)
    # plt.plot(xi, dxidDphi(xi))
    # plt.grid()
    # plt.tight_layout()
    # plt.show()

if __name__ == '__main__':
    main()

""" """

import numpy as np

from lib.pars import pars

pisq = np.pi**2 
pisqOver16 = pisq / 16.

def a(data, p):
    return 1. + p.alpha*data.f5() +\
        p.alph1*p.alph2*(data.f1() + p.beta*p.cosdphi*data.f2() + p.alpha*data.f6()) +\
        p.beta*p.sindphi*(p.alph1*data.f3() + p.alph2*data.f4())

def b(data, p):
    return (1. + p.alpha)*(p.alph1*data.g1() + p.alph2*data.g2())+\
            p.beta*(p.cosdphi*(p.alph1*data.g3() + p.alph2*data.g4())+\
            p.alph1*p.alph2*p.sindphi*data.g5())

def csec6D(data, xi, p=pars):
    """ Complere differential cross section """
    result = a(data, p) if np.isclose(xi, 0) else a(data, p) + xi * b(data, p)
    if (any(result < 0)):
        print('Negative PDF detected')
    return result

def __sideSelector(data, p, side):
    """ """
    return (p.alph1, data.sinphi1, data.sinth1, data.cosphi1, data.costh1) if side == 1 else\
           (p.alph2, data.sinphi2, data.sinth2, data.cosphi2, data.costh2)

def csec3D(data, xi, side, p=pars):
    """ Single Lambda cross section """
    ali, sphi, sthi, cphi, cthi = __sideSelector(data, p, side)
    return 1. + p.alpha*data.costh**2 + ali*p.beta*p.sindphi*data.sinth*data.costh*sthi*sphi +\
        xi*((1. + p.alpha)*ali*data.costh*cthi + ali*p.beta*p.cosdphi*data.sinth*sthi*cphi)

def csecPhi(data, xi, side, p=pars):
    """ 1D cross section for azimuthal angle in Lambda frame """
    ali, _, _, cphi, _ = __sideSelector(data, p, side)
    return 1. + p.alpha/3. + xi*pisqOver16*ali*p.beta*p.cosdphi*cphi

def csecPhiRaw(phi1, xi, p=pars):
    """ 1D cross section for azimuthal angle in Lambda frame """
    return 1. + p.alpha / 3. +\
        xi*pisqOver16*p.alph1*p.beta*p.cosdphi*np.cos(phi1)

def csec2D(data, xi, side, p=pars):
    """ Single Lambda cross section """
    ali, _, _, _, cthi = __sideSelector(data, p, side)
    return 1. + data.costh * (p.alpha*data.costh + xi*(1.+p.alpha)*ali*cthi)

def csec2DRaw(costh, costh1, xi, p=pars):
    """ Single Lambda cross section """
    return 1. + costh*(p.alpha*costh + xi*(1.+p.alpha)*p.alph1*costh1)

def aLR(xi, p=pars):
    """ Left-right asymmetry """
    return xi * 3.*np.pi / 8. * np.sqrt(1-p.alpha**2) / (p.alpha+3) * p.alph1 * p.cosdphi

def aFB(xi, p=pars):
    """ Forward-backward asymetry """
    return xi * 3.*p.alph1 / 4. * (p.alpha + 1.) / (p.alpha + 3.)

if __name__ == '__main__':
    print('asymLR = {:.3f}xi'.format(aLR(1., pars)))
    print('asymFB = {:.3f}xi'.format(aFB(1., pars)))

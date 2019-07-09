""" """

import numpy as np

from pars import pars

pisq = np.pi**2 
pisqOver16 = pisq / 16.
eps = 1.e-6

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
    result = a(data, p) if xi < eps else a(data, p) + xi * b(data, p)
    if (any(result < 0)):
        print('Negative PDF detected')
    return result

def csec3D(data, xi, p=pars):
    """ Single Lambda cross section """
    return 1. + p.alpha * data.costh**2 + p.alph1 * np.sqrt(1. - p.alpha**2) * p.sindphi *\
        data.costh * data.sinth1 * data.sinphi1 + xi * (
            (1.+p.alpha)*p.alph1 + p.alph1 * np.sqrt(1. - p.alpha**2) * p.cosdphi *\
            data.sinth * data.sinth1 * data.cosphi1
        )

def csecPhi(data, xi, p=pars):
    """ 1D cross section for azimuthal angle in Lambda frame """
    return 1. + p.alpha / 3. + xi * pisqOver16 * p.alph1 * np.sqrt(1. - p.alpha**2)*\
        p.cosdphi * data.cosphi1

def csec2D(data, xi, p=pars):
    """ Single Lambda cross section """
    return 1. + data.costh*(p.alpha*data.costh + xi*(1.+p.alpha)*p.alph1*data.costh1)

def aLR(xi, p=pars):
    """ Left-right asymmetry """
    return xi * 3.*np.pi / 8. * np.sqrt(1-p.alpha**2) / (p.alpha+3) * p.alph1 * p.cosdphi

def aFB(xi, p=pars):
    """ Forward-backward asymetry """
    return xi * 3.*p.alph1 / 4. * (p.alpha + 1.) / (p.alpha + 3.)

if __name__ == '__main__':
    print('asymLR = {:.3f}xi'.format(aLR(1., pars)))
    print('asymFB = {:.3f}xi'.format(aFB(1., pars)))

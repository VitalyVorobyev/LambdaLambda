""" Form-factors from BESIII measurement """

import numpy as np

datapath = '../data'

class Pars(object):
    def __init__(self, dphi, alpha, alph1, alph2=None):
        self.dphi = dphi
        self.cosdphi = np.cos(dphi)
        self.sindphi = np.sin(dphi)
        self.alpha = alpha
        self.beta = np.sqrt(1. - alpha**2)
        self.alph1 = alph1
        self.alph2 = -alph1 if alph2 is None else alph2

    def __str__(self):
        return 'Pars:\n\
   alpha: {:.3f}\n\
    dphi: {:.3f}\n\
   alph1: {:.3f}\n\
   alph1: {:.3f}'.format(self.alpha, self.dphi, self.alph1, self.alph2)

pars = Pars (
    42.4 / 180. * np.pi,  # +- 0.6 +- 0.5 deg
    0.461,  # +- 0.006 +- 0.007
    0.750  # +- 0.009 +- 0.004
)

def sinToCos(sin):
    return np.sqrt(1. - sin**2)

class Data(object):
    def __init__(self, events):
        """ events is a np.array of shape (nevt, 5) """
        self.costh = events[:,0]
        self.sinth = sinToCos(self.costh)
        self.costh1 = events[:,1]
        self.sinth1 = sinToCos(self.costh1)
        self.cosphi1 = np.cos(events[:,2])
        self.sinphi1 = np.sin(events[:,2])
        self.costh2 = events[:,3]
        self.sinth2 = sinToCos(self.costh2)
        self.cosphi2 = np.cos(events[:,4])
        self.sinphi2 = np.sin(events[:,4])

        self.N = events.shape[0]

        assert(not np.isnan(self.f1()).any())
        self.f = [self.f1(), self.f2(), self.f3(), self.f4(), self.f5(), self.f6()]
        self.g = [self.g1(), self.g2(), self.g3(), self.g4(), self.g5()]

    def f1(self):
        if hasattr(self, 'f'):
            return self.f[0]
        return self.sinth**2 * self.sinth1 * self.sinth2 * self.cosphi1 * self.cosphi2 +\
               self.costh**2 * self.costh1 * self.costh2

    def f2(self):
        if hasattr(self, 'f'):
            return self.f[1]
        return self.sinth * self.costh * (self.sinth1 * self.costh2 * self.cosphi1 +\
                                          self.costh1 * self.sinth2 * self.cosphi2)

    def f3(self):
        if hasattr(self, 'f'):
            return self.f[2]
        return self.sinth * self.costh * self.sinth1 * self.sinphi1

    def f4(self):
        if hasattr(self, 'f'):
            return self.f[3]
        return self.sinth * self.costh * self.sinth2 * self.sinphi2

    def f5(self):
        if hasattr(self, 'f'):
            return self.f[4]
        return self.costh**2

    def f6(self):
        if hasattr(self, 'f'):
            return self.f[5]
        return self.costh1 * self.costh2 -\
               self.sinth**2 * self.sinth1 * self.sinth2 * self.sinphi1 * self.sinphi2

    def g1(self):
        if hasattr(self, 'g'):
            return self.g[0]
        return self.costh * self.costh1

    def g2(self):
        if hasattr(self, 'g'):
            return self.g[1]
        return self.costh * self.costh2

    def g3(self):
        if hasattr(self, 'g'):
            return self.g[2]
        return self.sinth * self.sinth1 * self.cosphi1

    def g4(self):
        if hasattr(self, 'g'):
            return self.g[3]
        return self.sinth * self.sinth2 * self.cosphi2

    def g5(self):
        if hasattr(self, 'g'):
            return self.g[4]
        return self.sinth * (self.sinth1 * self.costh2 * self.sinphi1 +\
                             self.sinth2 * self.costh1 * self.sinphi2)

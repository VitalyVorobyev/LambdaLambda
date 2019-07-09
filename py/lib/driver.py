import numpy as np

def sqomsq(x):
    return np.sqrt(1. - x**2)

class LL(object):
    def __init__(self, alpha, dphi, alph1, alph2, xi):
        self.set(alpha, dphi, alph1, alph2, xi)

    def set(self, alpha, dphi, alph1, alph2, xi):
        self.alpha = alpha
        self.squmasq = np.sqrt(1. - alpha**2)
        self.dphi = dphi
        self.sindphi = np.sin(dphi)
        self.cosdphi = np.cos(dphi)
        self.alph1 = alph1
        self.alph2 = alph2
        self.aa12 = alph1 * alph2
        self.xi = xi

    def __call__(self, event):
        if len(event.shape) == 1:
            costh, costh1, phi1, costh2, phi2 = event
        elif len(event.shape) == 2:
            costh, costh1, phi1, costh2, phi2 = [event[:,i] for i in range(5)]

        self.costh, self.sinth = costh, sqomsq(costh)
        self.costh1, self.sinth1 = costh1, sqomsq(costh1)
        self.costh2, self.sinth2 = costh2, sqomsq(costh2)
        self.cosphi1, self.sinphi1 = np.cos(phi1), np.sin(phi1)
        self.cosphi2, self.sinphi2 = np.cos(phi2), np.sin(phi2)
        self.sincosth = self.costh * self.sinth

        if abs(self.xi) < 10**-7:
            a = self._a()
            negaMask = a < 0
            if any(negaMask):
                print('Negative PDF')
                print(event[negaMask])
                print('a: ', a[negaMask])
            return a

        a, b = self._a(), self._b()
        r = a + self.xi * b
        
        negaMask = r < 0
        if any(negaMask):
            print('Negative PDF')
            print(event[negaMask])
            print('a: ', a[negaMask])
            print('b: ', b[negaMask])
        
        return r

    def _f1(self):
        return self.sinth**2 * self.sinth1 * self.sinth2 * self.cosphi1 * self.cosphi2 +\
               self.costh**2 * self.costh1 * self.costh2

    def _f2(self):
        return self.sincosth * (self.sinth1 * self.costh2 * self.cosphi1 +\
                                self.costh1 * self.sinth2 * self.cosphi2)

    def _f3(self):
        return self.sincosth * self.sinth1 * self.sinphi1

    def _f4(self):
        return self.sincosth * self.sinth2 * self.sinphi2

    def _f5(self):
        return self.costh**2

    def _f6(self):
        return self.costh1 * self.costh2 -\
            self.sinth**2 * self.sinth1 * self.sinth2 * self.sinphi1 * self.sinphi2

    def _a(self):
        return 1. + self.alpha * self._f5() +\
            self.aa12 * (self._f1() + self.squmasq * self.cosdphi * self._f2()+\
                                                       self.alpha * self._f6()) +\
            self.squmasq * self.sindphi * (self.alph1 * self._f3() + self.alph2 * self._f4())

    def _b(self):
        return self.alph1 * self._g1() + self.alph2 * self._g2() + self.aa12 * self._g12()

    def _g1(self):
        return (1. + self.alpha) * self.costh * self.costh1 +\
            self.squmasq * self.cosdphi * self.sinth * self.sinth1 * self.cosphi1

    def _g2(self):
        return (1. + self.alpha) * self.costh * self.costh2 +\
            self.squmasq * self.cosdphi * self.sinth * self.sinth2 * self.cosphi2

    def _g12(self):
        return self.sindphi * self.squmasq * self.sinth * (
            self.costh1 * self.sinth2 * self.sinphi2 +\
            self.costh2 * self.sinth1 * self.sinphi1)

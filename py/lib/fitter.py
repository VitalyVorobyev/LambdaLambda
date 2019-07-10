from iminuit import Minuit

from pars import Pars, Data
from pdfs import csec6D, csec2D, csecPhi

import numpy as np

""" Complete 5D fit with polarization """
class FitFull(object):
    def fcn(self, alpha, dphi, alph1, alph2, xi):
        loglh = self.loglh(xi, Pars(dphi, alpha, alph1, alph2))
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, a2 {:.3f}, xi {:.3f}'.format(
            loglh, alpha, dphi, alph1, alph2, xi))
        return loglh
    
    def loglh(self, xi, p):
        return -np.sum(np.log(csec6D(self.data, xi, p))) +\
            np.log(np.sum(csec6D(self.normdata, xi, p))) * self.data.N

    def fitTo(self, data, normdata, init):
        self.data = data
        self.normdata = normdata
        
        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=init.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=init.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=init.alph1, error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
            alph2=init.alph2, error_alph2=0.1, limit_alph2=(-1., 0.),       fix_alph2=False,
               xi= 0.0,       error_xi   =0.5, limit_xi   =(-1.05, 1.01),   fix_xi   =False
        )
        
        fmin, param = minimizer.migrad()
        minimizer.print_param()
        corrmtx = minimizer.matrix(correlation=True)
        return (fmin, param, corrmtx)

""" 5D fit for Lambda formfactors without polarized beam """
class FitFullUnpolarized(object):
    def fcn(self, alpha, dphi, alph1, alph2):
        loglh = self.loglh(Pars(dphi, alpha, alph1, alph2))
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, a2 {:.3f}'.format(
            loglh, alpha, dphi, alph1, alph2))
        return loglh
    
    def loglh(self, p):
        return -np.sum(np.log(csec6D(self.data, 0., p))) +\
            np.log(np.sum(csec6D(self.normdata, 0., p))) * self.data.N

    def fitTo(self, data, normdata, init):
        self.data = data
        self.normdata = normdata
        
        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=init.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=init.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=init.alph1, error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
            alph2=init.alph2, error_alph2=0.1, limit_alph2=(-1., 0.),       fix_alph2=False
        )

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        corrmtx = minimizer.matrix(correlation=True)
        return (fmin, param, corrmtx)

""" Azimuthal distribution 1D fit  """
class FitPhi(object):
    def fcn(self, xi):
        loglh = self.loglh(xi)
        print('loglh: {:.2f},  xi {:.3f}'.format(loglh, xi))
        return loglh

    def loglh(self, xi):
        return -np.sum(np.log(csecPhi(self.data, xi, self.p))) +\
            np.log(np.sum(csecPhi(self.normdata, xi, self.p))) * self.data.N

    def fitTo(self, data, normdata, pars):
        self.data = data
        self.normdata = normdata
        self.p = pars

        minimizer = Minuit(self.fcn, errordef=0.5,
               xi=0., error_xi=0.5, limit_xi=(-1.01, 1.01), fix_xi=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param)

""" Forward-backward distribution 2D fit  """
class FitFB2D(object):
    def fcn(self, xi):
        loglh = self.loglh(xi)
        print('loglh: {:.2f},  xi {:.3f}'.format(loglh, xi))
        return loglh

    def loglh(self, xi):
        return -np.sum(np.log(csec2D(self.data, xi, self.p))) +\
            np.log(np.sum(csec2D(self.normdata, xi, self.p))) * self.data.N

    def fitTo(self, data, normdata, pars):
        self.data = data
        self.normdata = normdata
        self.p = pars

        minimizer = Minuit(self.fcn, errordef=0.5,
               xi=0., error_xi=0.5, limit_xi=(-1.01, 1.01), fix_xi=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param)

""" Constrained fitters for Lambda -> p pi """

from iminuit import Minuit

from lib.pars import pars, Pars, Data, fitresfile
from lib.pdfs import csec2D, csecPhi, csec3D

import numpy as np

MULT = 2

def setMult(m):
    """ """
    global MULT
    MULT = m

def getMult():
    """ """
    global MULT
    return MULT

def getConc(N):
    """ Concentration matrix for Lambda form-factors """
    print('MULT = {}'.format(MULT))
    data = np.load(fitresfile('upol', 0., False) + '.npz')
    corr = data['corr']
    print(corr)
    errs = [x[1] for x in data['fitres'][:,1]] / np.sqrt(N*MULT)
    print(errs)
    covs = corr * np.outer(errs, errs)
    return np.linalg.inv(covs)

""" Azimuthal distribution 1D fit with constrained form-factors """
class FitPhiConstr(object):
    def fcn(self, alpha, dphi, alph1, xi):
        loglh = self.loglh(xi, Pars(dphi, alpha, alph1, -alph1))
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, xi {:.3f}'.format(
            loglh, alpha, dphi, alph1, xi))
        return loglh

    def constrLh(self, p):
        """ """
        diff = p.array[:-1] - pars.array[:-1]
        return (np.outer(diff, diff) * self.conc).sum()

    def loglh(self, xi, p):
        return -np.sum(np.log(csec2D(self.data, xi, p))) +\
            np.log(np.sum(csecPhi(self.normdata, xi, p))) * self.data.N+\
            0.5*self.constrLh(p)

    def fitTo(self, data, normdata, p=pars):
        self.data = data
        self.normdata = normdata
        self.conc = getConc(data.N)[:-1, :-1]
        print('Concentration matrix:')
        print(self.conc)

        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=p.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=p.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=p.alph1, error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
               xi=0., error_xi=0.5, limit_xi=(-1.01, 1.01), fix_xi=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param, minimizer.matrix(correlation=True))

""" Forward-backward distribution 2D fit  """
class FitFB2DConstr(object):
    def fcn(self, alpha, dphi, alph1, xi):
        loglh = self.loglh(xi, Pars(dphi, alpha, alph1, -alph1))
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, xi {:.3f}'.format(
            loglh, alpha, dphi, alph1, xi))
        return loglh

    def constrLh(self, p):
        """ """
        diff = p.array[:-1] - pars.array[:-1]
        return (np.outer(diff, diff) * self.conc).sum()

    def loglh(self, xi, p):
        return -np.sum(np.log(csecPhi(self.data, xi, p))) +\
            np.log(np.sum(csecPhi(self.normdata, xi, p))) * self.data.N+\
            0.5*self.constrLh(p)

    def fitTo(self, data, normdata, p=pars):
        self.data = data
        self.normdata = normdata
        self.conc = getConc(data.N)[:-1, :-1]
        print('Concentration matrix:')
        print(self.conc)

        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=p.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=p.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=p.alph1, error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
               xi=0., error_xi=0.5, limit_xi=(-1.01, 1.01), fix_xi=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param, minimizer.matrix(correlation=True))

""" Single-side full 3D fit """
class FitSSideConstr(object):
    def fcn(self, alpha, dphi, alph1, xi):
        loglh = self.loglh(xi, Pars(dphi, alpha, alph1, -alph1))
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, xi {:.3f}'.format(
            loglh, alpha, dphi, alph1, xi))
        return loglh

    def constrLh(self, p):
        """ """
        diff = p.array[:-1] - pars.array[:-1]
        return (np.outer(diff, diff) * self.conc).sum()

    def loglh(self, xi, p):
        return -np.sum(np.log(csec3D(self.data, xi, p))) +\
            np.log(np.sum(csec3D(self.normdata, xi, p))) * self.data.N+\
            0.5*self.constrLh(p)

    def fitTo(self, data, normdata, p=pars):
        self.data = data
        self.normdata = normdata
        self.conc = getConc(data.N)[:-1, :-1]
        print('Concentration matrix:')
        print(self.conc)

        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=p.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=p.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=p.alph1, error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
               xi=0., error_xi=0.5, limit_xi=(-1.01, 1.01), fix_xi=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param, minimizer.matrix(correlation=True))

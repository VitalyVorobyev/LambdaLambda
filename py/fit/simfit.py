""" """

from iminuit import Minuit

from lib.pars import pars, Pars, Data, fitresfile
from lib.pdfs import csec2D, csecPhi, csec3D, csec6D

from fit.constrainedfit import getConc

import numpy as np


class SimFitSS(object):
    ssec = {
        'ss3d' : csec3D,
        'ss3d_full' : csec3D,
        'ss2d' : csec2D,
        'ss1d' : csecPhi
    }
    def __init__(self, ftype):
        """ """
        assert(ftype in SimFitSS.ssec)
        self.ftype = ftype
        self.pdf = SimFitSS.ssec[ftype]

    def constrLh(self):
        """ """
        diff = self.p.array - pars.array
        return (np.outer(diff, diff) * self.conc).sum()

    def fcn(self, alpha, dphi, alph1, alph2, xip, xin):
        self.p = Pars(dphi, alpha, alph1, alph2)
        llhp = self.loglh(self.datap, xip)
        llhn = self.loglh(self.datan, xin)
        loglh = llhp + llhn
        if self.constr and self.ftype != 'ss3d_full':
            loglh = loglh + self.constrLh()
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, a2 {:.3f}, xip {:.3f}, xin {:.3f}'.format(
            loglh, alpha, dphi, alph1, alph2, xip, xin))
        return loglh

    def loglh(self, data, xi):
        """ """
        return self.loglhSS(data, xi, 1) + self.loglhSS(data, xi, -1)

    def loglhSS(self, data, xi, side):
        return -np.sum(np.log(self.pdf(data, xi, side, self.p))) +\
            np.log(np.sum(self.pdf(self.normdata, xi, side, self.p))) * data.N

    def fitTo(self, datap, datan, normdata, constr=True, p=pars):
        self.datap = datap
        self.datan = datan
        self.normdata = normdata
        self.constr = constr

        self.conc = getConc(datap.N)
        print('Concentration matrix:')
        print(self.conc)

        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=p.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=not constr,
             dphi=p.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =not constr,
            alph1=p.alph1, error_alph1=0.1, limit_alph1=( 0., 1.),       fix_alph1=not constr,
            alph2=p.alph2, error_alph2=0.1, limit_alph2=(-1., 0.),       fix_alph2=not constr,
              xip= 0.5, error_xip=0.5, limit_xip=( .0, 1.01), fix_xip=False,
              xin=-0.5, error_xin=0.5, limit_xin=(-1.01, .0), fix_xin=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param, minimizer.matrix(correlation=True))

class SimFitFull(object):
    def fcn(self, alpha, dphi, alph1, alph2, xip, xin):
        self.p = Pars(dphi, alpha, alph1, alph2)
        llhp = self.loglh(self.datap, xip)
        llhn = self.loglh(self.datan, xin)
        loglh = llhp + llhn
        print('loglh: {:.2f}, a {:.3f}, phi {:.3f}, a1 {:.3f}, a2 {:.3f}, xip {:.3f}, xin {:.3f}'.format(
            loglh, alpha, dphi, alph1, alph2, xip, xin))
        return loglh

    def loglh(self, data, xi):
        return -np.sum(np.log(csec6D(data, xi, self.p))) +\
            np.log(np.sum(csec6D(self.normdata, xi, self.p))) * data.N

    def fitTo(self, datap, datan, normdata, p=pars):
        self.datap = datap
        self.datan = datan
        self.normdata = normdata

        minimizer = Minuit(self.fcn, errordef=0.5,
            alpha=p.alpha, error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi=p.dphi,  error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1=p.alph1, error_alph1=0.1, limit_alph1=( 0., 1.),       fix_alph1=False,
            alph2=p.alph2, error_alph2=0.1, limit_alph2=(-1., 0.),       fix_alph2=False,
              xip= 0.5, error_xip=0.5, limit_xip=( .0, 1.01), fix_xip=False,
              xin=-0.5, error_xin=0.5, limit_xin=(-1.01, .0), fix_xin=False)

        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param, minimizer.matrix(correlation=True))

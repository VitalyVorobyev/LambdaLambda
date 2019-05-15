from iminuit import Minuit

from driver import LL

import numpy as np

class LLFit(object):
    ll = LL(1., 0., 0.6, -0.6, 0.)
    
    def __init__(self):
        pass
        
    @staticmethod
    def fcn(alpha, dphi, alph1, alph2, xi):
        LLFit.ll.set(alpha, dphi, alph1, alph2, xi)
        loglh = LLFit.loglh()
        print('loglh: {}, a {}, phi {}, a1 {}, a2 {}, xi {}'.format(
            loglh, alpha, dphi, alph1, alph2, xi))
        return loglh
    
    @staticmethod
    def loglh():
        return -np.sum(np.log(LLFit.ll(LLFit.data))) +\
            np.log(np.sum(LLFit.ll(LLFit.normdata))) * len(LLFit.data)

    @staticmethod
    def fitTo(data, normdata, init=None):
        LLFit.data = data
        LLFit.normdata = normdata
        
        minimizer = Minuit(
            LLFit.fcn,
            alpha= 0.6,       error_alpha=0.1, limit_alpha=(-1., 1.),       fix_alpha=False,
             dphi= 0.5*np.pi, error_dphi =1.0, limit_dphi =(-np.pi, np.pi), fix_dphi =False,
            alph1= 0.6,       error_alph1=0.1, limit_alph1=(0., 1.),        fix_alph1=False,
            alph2=-0.6,       error_alph2=0.1, limit_alph2=(-1., 0.),       fix_alph2=False,
               xi= 0.0,       error_xi   =0.5, limit_xi   =(-1.01, 1.01),   fix_xi   =False,
            errordef=0.5)
        
        fmin, param = minimizer.migrad()
        minimizer.print_param()
        return (fmin, param)

#! /usr/bin/python3

from collections import OrderedDict

from lib.pars import Data, Pars, pars, datafile, fitresfile
from lib.fitter import FitFull, FitFullUnpolarized, FitPhi, FitFB2D, FitSSide
from lib.efficiency import applyDetEff

import numpy as np
import matplotlib.pyplot as plt

fitmap = {
    'full' : FitFull,
    'upol' : FitFullUnpolarized,
    'phif' : FitPhi,
    'fb2d' : FitFB2D,
    'ss3d' : FitSSide
}

def saveFitRes(ftype, xi, eff, nsig, fres):
    """ """
    np.savez(fitresfile(ftype, xi, eff),
        status=np.array([[key, fres[0][key]] for key in  fres[0]]),
        fitres=np.array([[p.name, [p.value, p.error * np.sqrt(nsig)]] for p in fres[1]]),
        corr=np.array(fres[2]),
        nsig=nsig
    )

def getData(xi):
    return np.load(datafile(xi))

def runfit(data, ftype, N=10**5., xi=0., eff=False):
    """ """
    xi = '{:.1f}'.format(xi).replace('.', '_')
    print('N = {}'.format(N))
    signal = Data(applyDetEff(data['signal'][:N], data['signalmask'][:N], False))\
        if eff else Data(data['signal'][:N])
    norm = Data(data['phsp'])

    llfit = fitmap[ftype]()
    fmin, fitres, mtx = llfit.fitTo(signal, norm, pars)
    print(fmin)
    print(np.array(mtx))

    for p in fitres:
        print('{:5s}: {:.3f}'.format(p.name, p.error * np.sqrt(signal.N)))

    saveFitRes(ftype, xi, eff, signal.N, (fmin, fitres, mtx))

    print('Eff: {:.3f}'.format(float(signal.N) / data['signal'].shape[0]))

def runAll(nevt=10**5):
    """ Run all procedures """
    for xi in np.linspace(-1., 1., 21):
        data = getData(xi)
        for eff in [False, True]:
            print('Eff turned on' if eff else 'Eff turned off')
            for ftype in fitmap:
                if ftype != 'upol':
                    print('Starting {} for xi {}'.format(ftype, xi))
                    runfit(data, ftype, nevt, xi, eff)
    
    data = getData(0.)
    runfit(data, 'upol', nevt, 0., False)
    runfit(data, 'upol', nevt, 0., True)

def main():
    """ Unit test """
    # ftype = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in fitmap else 'full'
    # xi = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
    # runfit(getData(xi), ftype, xi, False)

if __name__ == '__main__':
    runAll()
    # main()

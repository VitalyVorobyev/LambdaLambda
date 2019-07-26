#! /usr/bin/env python3
from collections import OrderedDict

from lib.pars import Data, Pars, pars, datafile, fitresfile
from lib.efficiency import applyDetEff

from fit.fitter import FitFull, FitFullUnpolarized, FitPhi, FitFB2D, FitSSide
from fit.constrainedfit import FitPhiConstr, FitFB2DConstr, FitSSideConstr, setMult, getMult
from fit.simfit import SimFitSS, SimFitFull

import numpy as np
import matplotlib.pyplot as plt

fitmap = {
    'full'  : FitFull,
    'upol'  : FitFullUnpolarized,
    'phif'  : FitPhi,
    'phifc' : FitPhiConstr,
    'fb2d'  : FitFB2D,
    'fb2dc' : FitFB2DConstr,
    'ss3d'  : FitSSide,
    'ss3dc' : FitSSideConstr
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

def runsimfit(datap, datan, ftype, constr, N=10**5., xi=0., eff=False):
    """ """
    xi = '{:.1f}'.format(xi).replace('.', '_')
    print('N = {}'.format(N))
    signalp = Data(datap['signal'][:N])
    signaln = Data(datan['signal'][-N:])
    norm = Data(datap['phsp'])

    llfit = SimFitSS(ftype)
    fmin, fitres, mtx = llfit.fitTo(signalp, signaln, norm, constr, pars)
    print(fmin)
    print(np.array(mtx))

    for p in fitres:
        print('{:5s}: {:.3f}'.format(p.name, p.error * np.sqrt(signalp.N)))

    saveFitRes(ftype+'_sim_{}_{}'.format(constr, getMult()), xi, eff, signalp.N, (fmin, fitres, mtx))

def runfullsimfit(datap, datan, N=10**5., xi=0., eff=False):
    """ """
    xi = '{:.1f}'.format(xi).replace('.', '_')
    print('N = {}'.format(N))
    signalp = Data(datap['signal'][:N])
    signaln = Data(datan['signal'][-N:])
    norm = Data(datap['phsp'])

    llfit = SimFitFull()
    fmin, fitres, mtx = llfit.fitTo(signalp, signaln, norm, pars)
    print(fmin)
    print(np.array(mtx))

    for p in fitres:
        print('{:5s}: {:.3f}'.format(p.name, p.error * np.sqrt(signalp.N)))

    saveFitRes('full_sim', xi, eff, signalp.N, (fmin, fitres, mtx))

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

def runPhiConstr(nevt=int(1e5)):
    """ """
    for xi in np.linspace(-1., 1., 21):
        data = getData(xi)
        print('Starting {} for xi {:.1f}'.format('phifc', xi))
        runfit(data, 'phifc', nevt, xi, False)

def runFB2DConstr(nevt=int(1e5)):
    """ """
    for xi in np.linspace(-1., 1., 21):
        data = getData(xi)
        print('Starting {} for xi {:.1f}'.format('phifc', xi))
        runfit(data, 'fb2dc', nevt, xi, False)

def runSS3DConstr(nevt=int(1e5)):
    """ """
    for xi in np.linspace(-1., 1., 21):
        data = getData(xi)
        print('Starting {} for xi {:.1f}'.format('phifc', xi))
        runfit(data, 'ss3dc', nevt, xi, False)

def runSimFit(nevt=int(1e5)):
    """ """
    xi = 0.8
    datap = getData(xi)
    datan = getData(-xi)
    print('New fit: 3D Full')
    runsimfit(datap, datan, 'ss3d_full', False, nevt, xi)
    for constr in [False, True]:
        for key in ['ss1d', 'ss2d', 'ss3d']:
            print('New fit: {}, constr: {}'.format(key, constr))
            runsimfit(datap, datan, key, constr, nevt, xi)

def runSimFullFit(nevt=int(1e5)):
    """ """
    print('New fit: SimFull')
    xi = 0.8
    datap = getData(xi)
    datan = getData(-xi)
    runfullsimfit(datap, datan, nevt, xi)

def main():
    """ Unit test """
    data = getData(0.8)
    runfit(data, 'ss3d', int(1e5), 0.8, False)
    # ftype = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in fitmap else 'full'
    # xi = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
    # runfit(getData(xi), ftype, xi, False)

if __name__ == '__main__':
    setMult(1)
    # runSimFullFit()
    runSimFit()
    # runSS3DConstr()
    # runFB2DConstr()
    # runPhiConstr()
    # runAll()
    # main()

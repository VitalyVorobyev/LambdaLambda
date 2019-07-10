#! /usr/bin/python3

import sys
sys.path.append('./lib')

from pars import Data, Pars, pars, datapath
from fitter import FitFull, FitFullUnpolarized, FitPhi, FitFB2D

import numpy as np
import matplotlib.pyplot as plt

fitmap = {
    'full' : FitFull,
    'upol' : FitFullUnpolarized,
    'phif' : FitPhi,
    'fb2d' : FitFB2D
}

def main():
    if len(sys.argv) > 2:
        xi = '{:.1f}'.format(float(sys.argv[2])).replace('.', '_')
    else:
        xi = '1_0'
    datafile = '/'.join([datapath, 'll_xi{}.npz'.format(xi)])
    data = np.load(datafile)

    nevt = 100000
    normnevt = 1000000

    signal = Data(data['signal'][:nevt])
    norm = Data(data['phsp'][:normnevt])

    model = {
        'alpha' :  0.6,
        'dphi'  :  0.5 * np.pi,
        'alph1' :  0.6,
        'alph2' : -0.6
    }
    pars = Pars(**model)

    if len(sys.argv) > 1 and sys.argv[1] in fitmap:
        llfit = fitmap[sys.argv[1]]()
    else:
        llfit = FitFullUnpolarized()
    fmin, fitres, mtx = llfit.fitTo(signal, norm, pars)
    print(fmin)

    for line in mtx:
        for val in line:
            print('{:2.3f} '.format(val), end=' ')
        print('')

    for p in fitres:
        print('{:5s}: {:.3f} / sqrt(N)'.format(p.name, p.error * np.sqrt(signal.N)))


if __name__ == '__main__':
    main()

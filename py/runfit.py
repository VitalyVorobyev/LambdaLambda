#! /usr/bin/python

import sys
sys.path.append('./lib')

from reader import ReaderTxt
from pars import Data, Pars, pars
from fitter import FitFull, FitFullUnpolarized, FitPhi, FitFB2D

import numpy as np

def main():
    datafile = '../data/llraw.dat'
    normfile = '../data/ll_xi1.dat'
    
    nevt = 10000
    normnevt = 100000

    reader = ReaderTxt(datafile, brief=False)
    data = Data(reader.readEvents(nevt)[0])
    
    normreader = ReaderTxt(normfile, brief=True)
    norm = Data(normreader.readEvents(normnevt))

    model = {
        'alpha' :  0.6,
        'dphi'  :  0.5 * np.pi,
        'alph1' :  0.6,
        'alph2' : -0.6,
        # 'xi'    :  0.0
    }
    
    # pars = Pars(**model)
    llfit = FitFullUnpolarized()
    fmin, param = llfit.fitTo(data, norm, pars)
    # fmin, param = llfit.fitTo(data, norm, pars)

if __name__ == '__main__':
    main()

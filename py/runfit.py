#! /usr/bin/python

from reader import ReaderTxt
from fitter import LLFit

import numpy as np

def main():
    datafile = '../llraw.dat'
    normfile = '../build/ll_xi1.txt'
    
    nevt = 10000
    normnevt = 100000

    reader = ReaderTxt(datafile)
    data = reader.readEvents(nevt)

    normreader = ReaderTxt(normfile, brief=True)
    norm = normreader.readEvents(normnevt)

    model = {
        'alpha' :  0.6,
        'dphi'  :  0.5 * np.pi,
        'alph1' :  0.6,
        'alph2' : -0.6,
        'xi'    :  0.0
    }
    
    llfit = LLFit()
    fmin, param = llfit.fitTo(data, norm)

if __name__ == '__main__':
    main()

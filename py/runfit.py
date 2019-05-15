#! /usr/bin/python

from fitter import LLFit

import numpy as np

def main():
    d = np.load('ll_xi1.npz')
    events, data = d['events'], d['data']
    
    print(len(events), len(data))
    print(events[-5:])
    print(data[:5])
    
    model = {
        'alpha' :  0.6,
        'dphi'  :  0.5 * np.pi,
        'alph1' :  0.6,
        'alph2' : -0.6,
        'xi'    :  0.0
        }
    
    llfit = LLFit()
    fmin, param = llfit.fitTo(data[:200000], events)


if __name__ == '__main__':
    main()

#! /usr/bin/python

import sys
sys.path.append('./lib')

from driver import LL
from driver2 import LL2
from pars import Data, Pars
from pdfs import csec6D
from reader import ReaderTxt

import numpy as np

def main():
    d = np.load('../data/ll_xi1.npz')
    events, data = d['events'], d['data']

    model = {
        'alpha' :  0.6,
        'dphi'  :  0.5 * np.pi,
        'alph1' :  0.6,
        'alph2' : -0.6,
        'xi'    :  0.0
        }

    ll1 = LL(**model)
    ll2 = LL2(**model)

    d = Data(data)
    p = Pars(model['dphi'], model['alpha'], model['alph1'], model['alph2'])

    Y1 = ll1(data)
    Y2 = ll2(data)
    Y3 = csec6D(d, model['xi'], p)

    print('Y1 same as Y2: {}'.format(np.allclose(Y1, Y2)))
    print('Y1 same as Y3: {}'.format(np.allclose(Y1, Y3)))
    print('Y2 same as Y3: {}'.format(np.allclose(Y2, Y3)))

if __name__ == '__main__':
    main()

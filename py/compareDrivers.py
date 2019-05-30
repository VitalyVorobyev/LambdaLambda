#! /usr/bin/python

from driver import LL
from driver2 import LL2
from reader import ReaderTxt

import numpy as np

def main():
    d = np.load('ll.npz')
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

    Y1 = ll1(data)
    Y2 = ll2(data)

    print(np.allclose(Y1, Y2))

if __name__ == '__main__':
    main()

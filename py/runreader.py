#! /usr/bin/python

from driver import LL
from reader import ReaderTxt

import numpy as np

def main():
    datafile = '../ll.dat'
    reader = ReaderTxt(datafile)

    P2 = 3.096**2
    M2 = 1.115683**2
    R2 = 0.96**2  # +- 0.14 +- 0.02
    alpha = (P2 - 4.*M2 * R2) / (P2 + 4.*M2 * R2)

    print('alpha = {}'.format(alpha))
    
    model = {
        'alpha' :  alpha,
        'dphi'  :  40. / 180. * np.pi,
        'alph1' :  0.75,
        'alph2' : -0.75,
        'xi'    :  1.
        }

    for key, val in model.iteritems():
        print('{}: {}'.format(key, val))

    ll = LL(**model)
    
    # Calculate matrix element squared
    events = reader.readEvents()  # norm data
    msq = ll(events)
    msq = msq / max(msq)
    
    # Accept-reject
    xi = np.random.rand(len(events))
    data = events[msq>xi]

    name = 'll_xi1.npz'

    np.savez(name, events=events, data=data)
    np.savetxt('ll_xi1.dat', data, '%.6f')

if __name__ == '__main__':
    main()

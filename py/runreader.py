#! /usr/bin/python

from driver import LL
from reader import ReaderTxt

import numpy as np

def main():
    datafile = '../data/llraw.dat'
    reader = ReaderTxt(datafile, brief=False)
    events, moms = reader.readEvents()  # norm data

    P2 = 3.096**2
    M2 = 1.115683**2
    R2 = 0.96**2  # +- 0.14 +- 0.02
    alpha = (P2 - 4.*M2 * R2) / (P2 + 4.*M2 * R2)
    print('alpha = {}'.format(alpha))

    xiList = [(-1., '1n'), (0., '0'), (1., '1')]
    # xiList = [(.5, 'half')]
    
    for xi, label in xiList:
        model = {
            'alpha' :  alpha,
            'dphi'  :  40. / 180. * np.pi,
            'alph1' :  0.75,
            'alph2' : -0.75,
            'xi'    :  xi
        }

        for key, val in model.iteritems():
            print('{}: {}'.format(key, val))

        ll = LL(**model)
    
        # Calculate matrix element squared
        msq = ll(events)
        msq = msq / max(msq)
    
        # Accept-reject
        mask = msq > np.random.rand(len(events))
        data = events[mask]
        dataMoms = moms[mask]

        name = '../data/ll_xi{}.npz'.format(label)

        np.savez(name, events=events, data=data, moms=dataMoms)
        np.savetxt('../data/ll_xi{}.dat'.format(label), data, '%.6f')

if __name__ == '__main__':
    main()

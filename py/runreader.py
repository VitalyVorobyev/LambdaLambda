#! /usr/bin/python

import sys
sys.path.append('./lib')

from lib.reader import ReaderTxt
from lib.pars import pars, datapath, Data, strxi
from lib.pdfs import csec6D
from lib.efficiency import DetEff

import numpy as np

def main():
    datafile = '/'.join([datapath, 'llraw.dat'])
    reader = ReaderTxt(datafile, brief=False)
    phsp, moms = reader.readEvents()  # norm data
    print(moms.shape)
    deff = DetEff(10., 0.05)
    phspMask = deff(moms)

    xiList = np.linspace(-1., 1., 21)

    for xi in xiList:
        label = strxi(xi)
        print(label)
        # Calculate matrix element squared
        msq = csec6D(Data(phsp), xi, pars)
        msq = msq / max(msq)

        # Accept-reject
        mask = msq > np.random.rand(len(phsp))
        signal = phsp[mask]
        signalMask = deff(moms[mask])

        name = '/'.join([datapath, 'll_xi{}.npz'.format(label)])
        np.savez(name,
            phsp=phsp,
            signal=signal,
            phspmask=phspMask,
            signalmask=signalMask,
        )
        np.savetxt('/'.join([datapath, 'll_xi{}.dat'.format(label)]), signal, '%.6f')

if __name__ == '__main__':
    main()

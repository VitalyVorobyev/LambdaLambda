#! /usr/bin/python3
""" """

import numpy as np
import matplotlib.pyplot as plt
from plotter import protonPolarCMS

def main():
    """ """
    idata = [
        ['../data/ll_xi0.npz', 1, 'costhProton_xi0'],
        ['../data/ll_xi1.npz', 2, 'costhProton_xi1'],
        ['../data/ll_xi1n.npz', 3, 'costhProton_xi1n']
    ]
    nbins = 40
    for ifile, fnum, fname in idata:
        data = np.load(ifile)
        protonPolarCMS(data['moms'], nbins, fnum, fname)
    plt.show()

if __name__ == '__main__':
    main()

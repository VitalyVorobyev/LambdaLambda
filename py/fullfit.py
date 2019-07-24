#! /usr/bin/env python3
""" """

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from lib.fitresreader import readFitRes
from lib.pars import strxi

from draw.bias import drawFitBiasXi
from draw.precision import drawPrecision, drawPrecisionNevt
from draw.corrmtx import drawCorrAB, drawCorrMtx

def loadData(xi):
    """ """
    return readFitRes('full', xi, False)

def frexi(dataxi):
    return OrderedDict([[strxi(xi), d['fitres']] for xi, d in dataxi.items()])

def corxi(dataxi):
    return OrderedDict([[strxi(xi), d['fitcor']] for xi, d in dataxi.items()])

def main():
    """ Unit test """
    xil = np.linspace(-1, 0.901, 20)
    dataxi = OrderedDict([xi, loadData(xi)] for xi in xil)
    fresxi = frexi(dataxi)
    corrxi = corxi(dataxi)
    print(corrxi.keys())
    
    for key, [mean, err] in fresxi['0_8'].items():
        print('{:5s}: {:+.3f} +- {:.3f}'.format(key, mean, err))

    drawPrecisionNevt('full', 'xi', [0.4, 0.6, 0.8], fresxi)
    # drawFitBiasXi('full', fresxi, 10**5)
    # drawPrecision('full', fresxi, True)
    # drawCorrAB('full', corrxi)
    # drawCorrMtx('full', corrxi['0_8'], 0.8)

if __name__ == '__main__':
    main()

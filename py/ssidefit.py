#! /usr/bin/python3
""" Single side 3D fit """

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from lib.fitresreader import readFitRes
from lib.pars import strxi, datafile
from lib.fitter import FitSSide

from draw.bias import drawFitBiasXi
from draw.precision import drawPrecision
from draw.corrmtx import drawCorrAB, drawCorrMtx

from runfit import runfit #, fitmap, saveFitRes

# from pars import Data, Pars, pars, , fitresfile

def loadData(xi):
    """ """
    return readFitRes('ss3d', xi, False)

def frexi(dataxi):
    return OrderedDict([[strxi(xi), d['fitres']] for xi, d in dataxi.items()])

def corxi(dataxi):
    return OrderedDict([[strxi(xi), d['fitcor']] for xi, d in dataxi.items()])

def main():
    """ Unit test """
    xi = 0.8
    data = np.load(datafile(xi))
    # print(data['phsp'])
    runfit(data, 'ss3d', 10**5., xi)

    # xil = np.linspace(-1, 0.901, 20)
    # dataxi = OrderedDict([xi, loadData(xi)] for xi in xil)
    # fresxi = frexi(dataxi)
    # corrxi = corxi(dataxi)
    # print(corrxi.keys())

    # drawFitBiasXi('full', fresxi, 10**5)
    # drawPrecision('full', fresxi, True)
    # drawCorrAB('full', corrxi)
    # drawCorrMtx('ss3d', corrxi['0_8'], 0.8)

if __name__ == '__main__':
    main()
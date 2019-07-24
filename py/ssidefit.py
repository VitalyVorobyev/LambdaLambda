#! /usr/bin/python3
""" Single side 3D fit """

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from lib.fitresreader import readFitRes
from lib.pars import strxi

from draw.bias import drawFitBiasXi
from draw.precision import drawPrecision
from draw.corrmtx import drawCorrAB, drawCorrMtx

def loadData(xi):
    """ """
    return readFitRes('ss3d', xi, False)

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
    
    drawFitBiasXi('ss3d', fresxi, 10**5)
    drawPrecision('ss3d', fresxi, True)
    drawCorrAB('ss3d', corrxi)
    drawCorrMtx('ss3d', corrxi['0_8'], 0.8)

if __name__ == '__main__':
    main()

#! /usr/bin/env python3

import sys
import numpy as np

from lib.pars import fitresfile, simfitresfile

def compare(xi):
    """ """
    p = 0.64
    mult = 4
    coefFull = 2. * np.sqrt(0.5*p)
    coef = np.sqrt(mult + 2*p)
    print('    mult: {}'.format(mult))
    print('coefFull: {:.2f}'.format(coefFull))
    print('    coef: {:.2f}'.format(coef))
    data = np.load(fitresfile('upol', 0., False) + '.npz')['fitres']
    errs = [x[1][1] for x in data]
    print('Upol: {:.2f} {:.2f} {:.2f} {:.2f} ----'.format(*errs))
    data = np.load(fitresfile('full', xi, False) + '.npz')['fitres']
    errs = [x[1][1] for x in data]
    print('Full: {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(*errs))
    data = np.load(fitresfile('ss3d_full', xi, False) + '.npz')['fitres']
    print(' F3D: ---- ---- ---- ---- {:.2f}'.format(data[-1][1][1] * coefFull))
    data = np.load(simfitresfile('ss3d_sim_False', mult, xi) + '.npz')['fitres']
    print('  3D: ---- ---- ---- ---- {:.2f}'.format(data[-1][1][1]))
    data = np.load(simfitresfile('ss3d_sim_True', mult, xi) + '.npz')['fitres']
    print(' 3Dc: ---- ---- ---- ---- {:.1f}'.format(data[-1][1][1]*coef))
    data = np.load(simfitresfile('ss2d_sim_False', mult, xi) + '.npz')['fitres']
    print('  2D: ---- ---- ---- ---- {:.1f}'.format(data[-1][1][1]))
    data = np.load(simfitresfile('ss2d_sim_True', mult, xi) + '.npz')['fitres']
    print(' 2Dc: ---- ---- ---- ---- {:.1f}'.format(data[-1][1][1]*coef))
    data = np.load(simfitresfile('ss1d_sim_False', mult, xi) + '.npz')['fitres']
    print('  1D: ---- ---- ---- ---- {:.1f}'.format(data[-1][1][1]))
    data = np.load(simfitresfile('ss1d_sim_True', mult, xi) + '.npz')['fitres']
    print(' 1Dc: ---- ---- ---- ---- {:.1f}'.format(data[-1][1][1]*coef))

def main():
    compare(float(sys.argv[1]))
    # data = np.load(fitresfile('ss3d', 0.1, True) + '.npz')
    # print(data['status'])
    # print(data['fitres'])
    # print(data['corr'])

if __name__ == '__main__':
    main()

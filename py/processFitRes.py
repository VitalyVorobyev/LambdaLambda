#! /usr/bin/env python3

import sys
import numpy as np

from lib.pars import fitresfile, simfitresfile

def coefFull(p=0.64):
    """ """
    return 2. * np.sqrt(0.5*p)

def coefSim(mult, p=0.64):
    """ """
    return np.sqrt(mult + 2*p)

def allErrs(key, xi=0.):
    """ """
    return [x[1][1] for x in np.load(fitresfile(key, xi, False) + '.npz')['fitres']]

def xiErr(key, xi):
    return np.load(fitresfile(key, xi, False) + '.npz')['fitres'][-1][1][1]

def xiSimErr(key, mult, xi):
    return np.load(simfitresfile(key, mult, xi) + '.npz')['fitres'][-1][1][1]

def compare(xi, mult):
    """ """
    p = 0.64
    cful = coefFull(p)
    csim = coefSim(mult, p)
    print('       p: {:.2f}'.format(p))
    print('    mult: {}'.format(mult))
    print('coefFull: {:.2f}'.format(cful))
    print('    coef: {:.2f}'.format(csim))
    print('Upol: {:.2f} {:.2f} {:.2f} {:.2f} ----'.format(*allErrs('upol')))
    print('Full: {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(*allErrs('full', xi)))
    print(' F3D: ---- ---- ---- ---- {:.2f}'.format(xiErr('ss3d_full', xi)*cful))
    print('  3D: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss3d_sim_False', mult, xi)))
    print('  2D: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss2d_sim_False', mult, xi)))
    print('  1D: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss1d_sim_False', mult, xi)))
    print(' 3Dc: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss3d_sim_True', mult, xi)*csim))
    print(' 2Dc: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss2d_sim_True', mult, xi)*csim))
    print(' 1Dc: ---- ---- ---- ---- {:.2f}'.format(xiSimErr('ss1d_sim_True', mult, xi)*csim))

def main():
    compare(float(sys.argv[1]), int(sys.argv[2]))

if __name__ == '__main__':
    main()

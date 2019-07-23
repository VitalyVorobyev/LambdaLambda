#! /usr/bin/python3

import sys
sys.path.append('./lib')

import numpy as np

from pars import pars, fitresfile

def main():
    data = np.load(fitresfile('ss3d', 0.1, True) + '.npz')
    print(data['status'])
    print(data['fitres'])
    print(data['corr'])

if __name__ == '__main__':
    main()

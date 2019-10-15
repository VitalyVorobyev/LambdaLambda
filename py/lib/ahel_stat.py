#! /usr/bin/env python3
""" """

import numpy as np

jpsi_csec = 1. * 10**-30  # cm^2
xi = 0.8
ahel = 4.75 * xi * 10**-4
lumi = 10**35  # cm^-2 s^-1

N0 = jpsi_csec * 10**7 * lumi / 3.
epsilon = 0.5

xi_ahel = (ahel * np.sqrt(2.*N0*epsilon))**-1

print(xi_ahel)
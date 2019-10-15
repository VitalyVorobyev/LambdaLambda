#! /usr/bin/env python3
""" """

import numpy as np

mLambda = 1.1  # GeV
mTau = 2.6 * 10**-10 # s
mJpsi = 3.096  # GeV
speed_of_light = 3 * 10**10 # cm / s

gamma_Lambda = 0.5*mJpsi / mLambda
beta_Lambda = np.sqrt(1. - 1./gamma_Lambda**2) 
flight_len = gamma_Lambda * speed_of_light * mTau

print('Gamma(Lambda):  {}'.format(gamma_Lambda))
print('Beta(Lambda):   {}'.format(beta_Lambda))
print('Flight(Lambda): {}'.format(flight_len))

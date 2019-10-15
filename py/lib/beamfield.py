#! /usr/bin/env python3

import numpy as np

c = 3 * 10**10  # cm/s
mu_lambda = -0.613
mu_nucl = 5.050783699*10**-24 # Erg * G^-1
hbar = 1.0545716 * 10**-27   # Erg * s

def stripFieldX(sigmaX, h, I):
    """ """
    return 4. * I / sigmaX * np.arctan(0.5 * sigmaX / h)

def freq(B, mu):
    """ """
    return -2 * B * mu * mu_nucl / hbar

def angle(B, dt):
    """ """
    return freq(B, mu_lambda) * dt

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    I = 4.2 * 10**-3 # Amper
    sigmaX = 17.8 * 10**-4 # cm
    sigmaY = 0.178 * 10**-4 # cm
    B = stripFieldX(sigmaX, sigmaY, I)
    print('Filed: {} Gauss'.format(B))
    omega = freq(B, mu_lambda)
    print('Freq:  {} s^-1'.format(omega))
    print('Angle: {} mrad'.format(angle(B, 10**-10)*10**3))
    print('Angle: {} mrad'.format(angle(1.5*10**4, 1.4*2.6*10**-10)*10**3))

    h = np.linspace(sigmaY, 10*sigmaY, 1000)
    plt.figure(num=1)
    plt.plot(h * 10**4, stripFieldX(sigmaX, h, I))
    plt.plot(h * 10**4, stripFieldX(10*sigmaX, h, 10*I))
    plt.plot(h * 10**4, stripFieldX(100*sigmaX, h, 100*I))
    plt.plot(h * 10**4, stripFieldX(1000*sigmaX, h, 1000*I))
    plt.grid()
    # plt.semilogy()
    plt.tight_layout()
    plt.show()

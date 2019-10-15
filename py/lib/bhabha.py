""" Bha-bha differential cross section """

alpha = 1. / 137.
mjpsi = 3.0969  # GeV

int_lumi = 10 # ab
lumi = 10**35  # cm^-2 s^-1
gevsqinv_to_mb = 0.389379
mb_to_cmsq = 10**-27

def rate_norm():
    """ s^-1 """
    return lumi * mb_to_cmsq * alpha**2 / mjpsi**2 * gevsqinv_to_mb

def diffcsec(costh):
    """ """
    costhsq = costh**2
    return 0.5*(1-costhsq) +\
           (5+2*costh+costhsq) / (1-costh)**2 -\
           (1+costh)**2/(1-costh)

def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.integrate as integrate

    min_theta = 5.
    max_costh = np.cos(min_theta / 180. * np.pi)
    min_costh = np.cos(30. / 180. * np.pi)

    costh10 = np.cos(10. / 180. * np.pi)
    costh15 = np.cos(15. / 180. * np.pi)

    coef = rate_norm()
    print('rate norm: {}'.format(coef))

    costh = np.linspace(-0.95, 0.95, 1000)
    plt.figure(num=1)
    plt.plot(costh, diffcsec(costh))
    plt.grid()
    plt.semilogy()
    plt.tight_layout()

    plt.figure(num=2)
    costh = np.linspace(min_costh, max_costh, 1000)
    I = np.array([integrate.quad(diffcsec, -x, x)[0] for x in costh])
    plt.plot(costh, coef*I)
    I10 = coef*integrate.quad(diffcsec, -costh10, costh10)[0]
    I15 = coef*integrate.quad(diffcsec, -costh15, costh15)[0]
    print('I10: {:.2f}'.format(I10))
    print('I15: {:.2f}'.format(I15))
    plt.plot(costh10, I10, 'ko')
    plt.plot(costh15, I15, 'bo')
    plt.grid()
    plt.semilogy()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

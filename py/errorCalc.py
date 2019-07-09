#! /usr/bin/python3
""" """

import numpy as np

def main():
    mu = 1.
    x = 4.75 * 10**-4 * mu
    mpsi = 3.0969
    mZ = 91.1876
    mSqRat = (mpsi / mZ)**2
    xi = 0.23  # sin2(theta_W)
    cossqth = np.sqrt(1. - xi**2)
    tansqth =  xi / cossqth

    den = (4.*x*(1.-2*xi) + 2.*mSqRat*mu) * xi
    cX = -4*xi*(1-xi)*x / den
    cMu = (3./4 - 2.*xi) * mSqRat * mu / den

    print('Cx : {:.3f}'.format(cX))
    cX  = (3. - 5.*tansqth) / (3. + 5. * tansqth**2)
    # cX = 1./(3./(3.-8.*xi) - tansqth)
    print('Cx : {:.3f}'.format(cX))
    print('Cmu: {:.3f}'.format(cMu))
    cMu = (1-xi)*(3./8-xi)/ (3./8*(1.-xi) - xi*(3./8-xi))
    print('Cmu: {:.3f}'.format(cMu))


if __name__ == '__main__':
    main()

""" """

import numpy as np
import matplotlib.pyplot as plt

from hmap import heatmap, annotate_heatmap

varmap = {
    'alpha' : 0,
     'dphi' : 1,
    'alph1' : 2,
    'alph2' : 3,
       'xi' : 4
}

err = {
    '-1.0' : [2.538, 3.386, 1.872, 1.871, 2.144],
    '-0.9' : [2.618, 3.704, 2.007, 2.006, 2.236],
    '-0.8' : [2.752, 4.038, 2.156, 2.147, 2.345],
    '-0.6' : [2.953, 4.915, 2.592, 2.563, 2.299],
    '-0.4' : [3.170, 5.934, 3.335, 3.303, 2.197],
     '0.0' : [3.446, 7.756, 6.714, 6.663, 2.032],
     '0.4' : [3.114, 5.753, 3.271, 3.220, 2.177],
     '0.6' : [2.941, 4.853, 2.568, 2.587, 2.287],
     '0.8' : [2.751, 4.014, 2.155, 2.159, 2.375],
     '0.9' : [2.622, 3.659, 1.996, 2.010, 2.274],
     '1.0' : [2.536, 3.169, 1.522, 1.525, 1.317]
}

corr = {
    '-1.0' : [
        [ 1.000, -0.255,  0.003,  0.008, -0.018],
        [-0.255,  1.000, -0.141,  0.136, -0.354],
        [ 0.003, -0.141,  1.000, -0.267,  0.585],
        [ 0.008,  0.136, -0.267,  1.000, -0.585],
        [-0.018, -0.354,  0.585, -0.585,  1.000]
    ],
    '-0.8' : [
        [ 1.000, -0.135, -0.046,  0.042, -0.077],
        [-0.135,  1.000, -0.143,  0.137, -0.371],
        [-0.046, -0.143,  1.000, -0.081,  0.476],
        [ 0.042,  0.137, -0.081,  1.000, -0.464],
        [-0.077, -0.371,  0.476, -0.464,  1.000]
    ],
    '-0.6' : [
        [ 1.000, -0.005, -0.068,  0.076, -0.118],
        [-0.005,  1.000, -0.129,  0.131, -0.353],
        [-0.068, -0.129,  1.000,  0.176,  0.351],
        [ 0.076,  0.131,  0.176,  1.000, -0.324],
        [-0.118, -0.353,  0.351, -0.324,  1.000]
    ],
    '-0.4' : [
        [ 1.000,  0.125, -0.083,  0.084, -0.134],
        [ 0.125,  1.000, -0.111,  0.117, -0.302],
        [-0.083, -0.111,  1.000,  0.471,  0.220],
        [ 0.084,  0.117,  0.471,  1.000, -0.187],
        [-0.134, -0.302,  0.220, -0.187,  1.000]
    ],
     '0.0' : [
        [ 1.000,  0.288, -0.067,  0.047,  0.011],
        [ 0.288,  1.000, -0.055,  0.081,  0.015],
        [-0.067, -0.055,  1.000,  0.869, -0.020],
        [ 0.047,  0.081,  0.869,  1.000, -0.012],
        [ 0.011,  0.015, -0.020, -0.012,  1.000]
     ],
     '0.4' : [
        [ 1.000,  0.121, -0.078,  0.086,  0.133],
        [ 0.121,  1.000, -0.115,  0.105,  0.302],
        [-0.078, -0.115,  1.000,  0.462, -0.228],
        [ 0.086,  0.105,  0.462,  1.000,  0.194],
        [ 0.133,  0.302, -0.228,  0.194,  1.000]
     ],
     '0.6' : [
        [ 1.000,  0.004, -0.087,  0.085,  0.139],
        [ 0.004,  1.000, -0.130,  0.137,  0.352],
        [-0.087, -0.130,  1.000,  0.175, -0.341],
        [ 0.085,  0.137,  0.175,  1.000,  0.352],
        [ 0.139,  0.352, -0.341,  0.352,  1.000]
     ],
     '0.8' : [
        [ 1.000, -0.135, -0.042,  0.050,  0.076],
        [-0.135,  1.000, -0.150,  0.148,  0.380],
        [-0.042, -0.150,  1.000, -0.103, -0.485],
        [ 0.050,  0.148, -0.103,  1.000,  0.485],
        [ 0.076,  0.380, -0.485,  0.485,  1.000]
     ],
     '0.9' : [
        [ 1.000, -0.190, -0.032,  0.034,  0.057],
        [-0.190,  1.000, -0.136,  0.143,  0.364],
        [-0.032, -0.136,  1.000, -0.183, -0.525],
        [ 0.034,  0.143, -0.183,  1.000,  0.528],
        [ 0.057,  0.364, -0.525,  0.528,  1.000]
     ],
     '1.0' : [
        [ 1.000, -0.281,  0.003, -0.010, -0.001],
        [-0.281,  1.000,  0.088, -0.088, -0.024],
        [ 0.003,  0.088,  1.000,  0.111,  0.048],
        [-0.010, -0.088,  0.111,  1.000, -0.047],
        [-0.001, -0.024,  0.048, -0.047,  1.000]
     ]
}

def corrMtx(xi):
    """ """
    xi = '{:.1f}'.format(xi)
    return corr[xi] if xi in corr else None
    
def hessErr(xi):
    """ """
    xi = '{:.1f}'.format(xi)
    return err[xi] if xi in err else None

def drawCorr(xi):
    co = corrMtx(xi)
    if co is None:
        return None

    labels = [r'$\alpha$', r'$d\Phi$', r'$\alpha_1$', r'$\alpha_2$', r'$xi$']

    fig, ax = plt.subplots()

    im, cbar = heatmap(np.array(co), labels, labels, ax=ax,
                   cmap="coolwarm_r", cbarlabel=None)
    texts = annotate_heatmap(im, valfmt="{x:.2f}")

    fig.tight_layout()
    # plt.show()

def precisionPlot(var, xil):
    """ """
    plt.rc('font', size=14)
    n = np.logspace(5, 8)
    for xi in xil:
        err = hessErr(xi)[varmap[var]]
        print(xi, err)
        if err is not None:
            plt.plot(n, err / np.sqrt(n) / xi, label=r'$\xi=${:.1f}'.format(xi))
    plt.grid()
    plt.semilogx()
    plt.semilogy()
    plt.ylabel(r'$d\xi/\xi$')
    plt.xlabel(r'$N$')
    plt.xlim((10**5, 10**8))
    plt.ylim((10**-4, 20.))
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('fullfit_xi_prec.pdf')
    plt.show()

def main():
    """ Unit test """
    # drawCorr(0.6)
    # drawCorr(0.)
    # drawCorr(1.)
    # drawCorr(-1.)
    # plt.show()

    xi = [0.4, 0.6, 0.8, 0.9]
    precisionPlot('xi', xi)
   

if __name__ == '__main__':
    main()
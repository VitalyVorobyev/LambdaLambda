""" """

import numpy as np
import matplotlib.pyplot as plt

from lib.pars import plotpath, varttl, strxi

font = {'family' : 'monospace', 'size'   : 14}
plt.rc('font', **font)  # pass in the font dict as kwargs

def drawPrecisionNevt(lbl, var, xil, fresxi):
    """ """
    plt.rc('font', size=14)
    n = np.logspace(6, 9)
    for xi in xil:
        err = fresxi[strxi(xi)][var][1]
        print(xi, err)
        if err is not None:
            plt.plot(n, err / np.sqrt(n) / xi, label=r'$\xi=${:.1f}'.format(xi))
    plt.grid(which='both')
    plt.semilogx()
    plt.semilogy()
    plt.ylabel(r'$d\xi/\xi$')
    plt.xlabel(r'$N$')
    plt.xlim((10**6, 10**9))
    plt.ylim((1e-4, 2e-2))
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('/'.join([plotpath, '{}_{}_prec.pdf'.format(lbl, var)]))
    plt.savefig('/'.join([plotpath, '{}_{}_prec.png'.format(lbl, var)]))
    plt.show()

def drawPrecision(lbl, fresxi, relative=False):
    """ Precision as function of polarization """
    xil = list(fresxi.keys())
    keys = list(fresxi[xil[0]].keys())
    vals = {key : [] for key in keys}

    for xi, fres in fresxi.items():
        for key, [mean, err] in fres.items():
            if relative:
                err = err / abs(mean) if abs(mean) > 1.e-2 else 0
            vals[key].append(err)

    for fignum, [key, val] in enumerate(vals.items()):
        plt.figure(num=fignum, figsize=(6, 5))
        plt.plot(xil, val, marker='.', markersize=12, linestyle='none', label=varttl[key])

        ylabel =  r'd{0:}/{0:}/$\sqrt{1:}$'.format(varttl[key], '{N}') if relative else\
            r'd{0:}/$\sqrt{1:}$'.format(varttl[key], '{N}')
        plt.xlabel(r'$\xi$', fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.gca().set_xticks(np.linspace(-1,1, 21), minor=True)
        plt.gca().set_xticks(np.linspace(-1,1, 5), minor=False)
        # plt.legend(loc='best')
        plt.xlim([-1.05, 1.05])
        plt.ylim([0, 1.05 * max(val)])
        plt.grid(which='minor', linestyle='--')
        plt.grid()
        plt.tight_layout()

        fname = 'prec_{}_{}'.format(lbl, key)
        if relative:
            fname = fname + '_rel'
        print('Save in {}'.format(fname))

        plt.savefig('/'.join([plotpath, fname + '.png']))
        plt.savefig('/'.join([plotpath, fname + '.pdf']))

    plt.show()

def asymPrecision(lbl, xil):
    """ """
    if lbl == 'fb':
        import lib.fbasym
        dxi = lib.fbasym.dxi
    elif lbl == 'lr':
        import lib.lrasym
        dxi = lib.lrasym.dxi
    else:
        return

    n = np.logspace(6, 9)
    for xi in xil:
        plt.plot(n, dxi(xi, 1, 1) / np.sqrt(n) / xi, label=r'$\xi=${:.1f}'.format(xi))
    plt.grid(which='both')
    plt.semilogx()
    plt.semilogy()
    plt.ylabel(r'$d\xi/\xi$')
    plt.xlabel(r'$N$')
    plt.xlim((10**6, 10**9))
    plt.ylim((1e-4, 2e-2))
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('/'.join([plotpath, '{}asym_xi_prec.pdf'.format(lbl)]))
    plt.savefig('/'.join([plotpath, '{}asym_xi_prec.png'.format(lbl)]))
    plt.show()

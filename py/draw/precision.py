""" """

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('./lib')

from pars import plotpath, varttl, strxi

font = {'family' : 'monospace',
        'size'   : 14}

plt.rc('font', **font)  # pass in the font dict as kwargs


def drawPrecisionNevt(var, xil):
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

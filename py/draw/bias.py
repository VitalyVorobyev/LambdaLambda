""" """

import numpy as np
import matplotlib.pyplot as plt

from lib.pars import pars, plotpath, varttl, strxi, floxi

font = {'family' : 'monospace',
        'size'   : 14}
plt.rc('font', **font)  # pass in the font dict as kwargs

def drawFitBias(fres, nevt):
    """ """
    plt.figure(figsize=(4,4))

    for idx, (key, [mean, err]) in enumerate(fres.items()):
        err = err / np.sqrt(nevt)
        bias = (mean - pars[key]) / err
        plt.errorbar(idx, bias, yerr=1., marker='.', markersize=12)

    xlabels = [varttl[key] for key in list(fres.keys())]
    plt.xticks(np.arange(len(xlabels)), xlabels)
    plt.ylim([-3., 3.])
    plt.grid()
    plt.tight_layout()
    plt.show()

def drawFitBiasXi(lbl, fresxi, nevt):
    """ """
    xil = [floxi(xi) for xi in fresxi.keys()]
    keys = list(fresxi[strxi(xil[0])].keys())
    vals = {key : [] for key in keys}

    for xi, fres in fresxi.items():
        for key, [mean, err] in fres.items():
            tval = floxi(xi) if key == 'xi' else pars[key]
            err = err / np.sqrt(nevt)
            bias = (mean - tval) / err
            vals[key].append(bias)

    for key, val in vals.items():
        val = np.array(val)
        plt.figure(figsize=(6, 5))
        plt.errorbar(xil, val, yerr=1., marker='.', markersize=12, linestyle='none', label=varttl[key])
        print('chi2 = {:.3}'.format(np.sum(val**2)/val.shape[0]))

        ylabel =  r'pull({})'.format(varttl[key])
        plt.xlabel(r'$\xi$', fontsize=16)
        plt.ylabel(ylabel, fontsize=16)

        plt.ylim([-3., 3.])
        plt.grid()
        plt.tight_layout()

        fname = 'bias_{}_{}'.format(lbl, key)
        print('Save in {}'.format(fname))

        plt.savefig('/'.join([plotpath, fname + '.png']))
        plt.savefig('/'.join([plotpath, fname + '.pdf']))
    plt.show()

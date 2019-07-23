""" """

import numpy as np
import matplotlib.pyplot as plt
import itertools

from draw.hmap import heatmap, annotate_heatmap
from lib.pars import plotpath, varttl, strxi, varmap

def drawCorrMtx(lbl, mtx, xi=None, show=True):
    """ """
    labels = [varttl[key] for key in list(varttl.keys())[:mtx.shape[0]]]
    print(labels)

    fig, ax = plt.subplots()
    im, cbar = heatmap(mtx, labels, labels, ax=ax, cmap="coolwarm_r", cbarlabel=None)
    texts = annotate_heatmap(im, valfmt="{x:.2f}")
    fig.tight_layout()

    fname = 'corr_mtx_{}'.format(lbl)
    if xi is not None:
        fname = fname + '_xi_{}'.format(strxi(xi))
    print('Correlation matrix saved in file {}'.format(fname))
    plt.savefig('/'.join([plotpath, '{}.pdf'.format(fname)]))
    plt.savefig('/'.join([plotpath, '{}.png'.format(fname)]))

    if show:
        plt.show()

def drawCorrAB(lbl, corrxi):
    """ Correlation as function of polarization """
    xil = list(corrxi.keys())
    keys = list(varmap.keys())[:corrxi[xil[0]].shape[0]]
    # vals = {key : [] for key in keys}

    for idx, [v1, v2] in enumerate(itertools.combinations(keys, 2)):
        print('{:5s} vs {:5s}'.format(v1, v2))
        i, j = varmap[v1], varmap[v2]
        print(i,j)
        for _, mtx in corrxi.items():
            print(mtx)
        val = [mtx[i, j] for _, mtx in corrxi.items()]
        plt.figure(num=idx, figsize=(6, 5))
        plt.plot(xil, val, marker='.', markersize=12, linestyle='none')

        ylabel =  r'corr {} vs {}'.format(varttl[v1], varttl[v2])
        plt.xlabel(r'$\xi$', fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.gca().set_xticks(np.linspace(-1,1, 21), minor=True)
        plt.gca().set_xticks(np.linspace(-1,1, 5), minor=False)
    
        plt.xlim([-1.05, 1.05])
        plt.ylim([-1.05, 1.05])
        plt.grid(which='minor', linestyle='--')
        plt.grid()
        plt.tight_layout()

        fname = 'corr_{}_{}_vs_{}'.format(lbl, v1, v2)
        plt.savefig('/'.join([plotpath, fname + '.png']))
        plt.savefig('/'.join([plotpath, fname + '.pdf']))

    plt.show()
    # for v2 in var2:
    #     i, j = varmap[var1], varmap[v2]
    #     lbl = 'corr {} vs {}'.format(varttl[var1], varttl[v2])
    #     data = np.array(sorted([[float(key), corr[key][i][j]] for key in corr.keys()]))
    #     plt.plot(data[:,0], data[:,1], '.', markersize=12, label=lbl)
    # plt.legend(loc='best', fontsize=12)
    # plt.xlabel(r'$\xi$')
    # plt.xlim((-1.05, 1.05))
    # plt.ylim((-1., 1.))
    # plt.tight_layout()
    # plt.grid()
    # fname = 'corr_{}_{}_vs_{}'.format(lbl, var1, var2)
    # plt.savefig('/'.join([plotpath, fname + '.png']))
    # plt.savefig('/'.join([plotpath, fname + '.pdf']))
    # plt.show()

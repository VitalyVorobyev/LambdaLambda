import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from lib.pdfs import csecPhiRaw, csec2DRaw
from lib.pars import plotpath, strxi

matplotlib.rc('font', size=14)
# plt.rc('xtick', labelsize=12)
# plt.rc('ytick', labelsize=12)

def lrDiffDist():
    phi = np.linspace(-np.pi, np.pi, 101)
    x_tick = np.linspace(-np.pi, np.pi, 9)
    x_label = [
        r'$-\pi$',
        r'$-\frac{3\pi}{4}$',
        r'$-\frac{\pi}{2}$',
        r'$-\frac{\pi}{4}$',
        r'$0$',
        r'$+\frac{\pi}{4}$',
        r'$+\frac{\pi}{2}$',
        r'$+\frac{3\pi}{4}$',
        r'$+\pi$'
    ]

    plt.figure(num=1, figsize=(6, 4))
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=14)

    mval = 0.
    for xi in [0., -1., 1.]:
        y = csecPhiRaw(phi, xi)
        plt.plot(phi, y, label=r'$\xi={:.0f}$'.format(xi))
        mval = max(mval, max(y))

    plt.ylim([0., 1.05*mval])
    plt.xlim([phi[0], phi[-1]])
    plt.xlabel(r'$\phi$ (rad)', fontsize=16)
    plt.legend(loc='best', fontsize=14)
    plt.grid()
    plt.tight_layout()

    plt.savefig('/'.join([plotpath, 'phidist.pdf']))
    plt.savefig('/'.join([plotpath, 'phidist.png']))

    plt.show()

def fbDiffDist(xi):
    x, y = np.meshgrid(np.linspace(-1., 1., 101),
                       np.linspace(-1., 1., 101))

    z = csec2DRaw(x, y, xi)
    z = z / z.max()

    plt.figure(num=1, figsize=(5, 4))
    cnt = plt.contourf(x, y, z, levels=100, cmap=plt.cm.viridis, vmin=0, vmax=1)
    plt.colorbar(cnt)
    plt.axis('equal')
    plt.xlabel(r'$\cos{\theta}$', fontsize=16)
    plt.ylabel(r'$\cos{\theta_1}$', fontsize=16)

    plt.tight_layout()

    plt.savefig('/'.join([plotpath, 'fbdist_xi{}.pdf'.format(strxi(xi))]))
    plt.savefig('/'.join([plotpath, 'fbdist_xi{}.png'.format(strxi(xi))]))
    
    plt.show()

if __name__ == '__main__':
    # lrDiffDist()
    fbDiffDist(0)
    fbDiffDist(1)

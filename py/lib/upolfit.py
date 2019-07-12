""" """

import numpy as np
import matplotlib.pyplot as plt

def corrMtx():
    """ """
    return np.array([
        [ 1.000,  0.298, -0.075, 0.037],  # alpha
        [ 0.298,  1.000, -0.037, 0.098],  # dphi
        [-0.075, -0.037,  1.000, 0.868],  # alph1
        [ 0.037,  0.098,  0.868, 1.000],  # alph2
    ])

def hessErr():
    """ """
    return np.array([
        3.446,  # /sqrt(N) for alpha
        7.757,  # /sqrt(N) for dphi
        6.716,  # /sqrt(N) for alph1
        6.652   # /sqrt(N) for alph2
        ])

def main():
    from hmap import heatmap, annotate_heatmap
    co = corrMtx()
    if co is None:
        return None

    labels = [r'$\alpha$', r'$d\Phi$', r'$\alpha_1$', r'$\alpha_2$']

    fig, ax = plt.subplots()
    im, cbar = heatmap(np.array(co), labels, labels, ax=ax,
                   cmap="coolwarm_r", cbarlabel=None)
    texts = annotate_heatmap(im, valfmt="{x:.2f}")
    fig.tight_layout()
    plt.savefig('corr_mtx_upol.pdf')
    plt.show()

if __name__ == '__main__':
    main()
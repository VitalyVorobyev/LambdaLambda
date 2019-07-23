""" """

import numpy as np

from fitresreader import readFitRes
from pars import plotpath, pars

# import sys
# sys.path.append('./draw')

from draw.corrmtx import drawCorrMtx
from draw.bias import drawFitBias

def loadData():
    """ """
    return readFitRes('upol', 0., False)

def main():
    data = loadData()
    if data['status']:
        print('Fit is good')
    else:
        print('Fit is bad')
        return

    co = data['fitcor']
    drawCorrMtx(co, 'upol')

    print('Fit errors:')
    for key, [mean, err] in data['fitres'].items():
        print('{:5s}: {:+.3f} +- {:.3f} / sqrt(N)'.format(key, mean, err))

    print('Fit bias for 100k events:')
    for key, [mean, err] in data['fitres'].items():
        err = err / np.sqrt(10**5)
        bias = mean - pars[key]
        print('{:5s}: {:+.3f} +- {:.3f} ({:.1f} sigma)'.format(key, bias, err, np.abs(bias) / err))

    drawFitBias(data['fitres'], 10**5)

if __name__ == '__main__':
    main()

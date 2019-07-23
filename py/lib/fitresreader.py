""" Tools for deading fit results """

import numpy as np
from collections import OrderedDict

from lib.pars import fitresfile

FTYPES = set(['full', 'upol', 'phif', 'fb2d', 'ss3d'])

def readFitRes(ftype, xi, eff):
    """  """
    assert(ftype in FTYPES)
    data = np.load(fitresfile(ftype, xi, eff) + '.npz')
    status = OrderedDict([x,y] for x,y, in zip(data['status'][:,0], data['status'][:,1]))
    fitres = OrderedDict([x,y] for x,y, in zip(data['fitres'][:,0], data['fitres'][:,1]))
    return {'status' : status['is_valid'],
            'fitres' : fitres,
            'fitcor' : data['corr']}

def main():
    """ Unit test """
    status, fitres, corr = readFitRes('full', 0.4, False)
    # print(dict(status))
    print(fitres['alpha'])
    # for var, fr in fitres[0].items():
    #     print('{}: {}'.format(var, fr))
    # print(corr)

if __name__ == '__main__':
    main()

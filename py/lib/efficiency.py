""" Detector efficiency """

import numpy as np

class DetEff(object):
    mSqThr = 0.5

    def __init__(self, thmin, ptpion, ptproton=None):
        self.costh = np.cos(thmin / 180. * np.pi)
        self.ptpiSq = ptpion**2
        self.ptpSq = ptpion**2 if ptproton is None else ptproton**2
        print('costhr {:.3f}'.format(self.costh))

    def __call__(self, moms):
        """ moms.shape = (nevt, 4, 4) """
        pSq = np.sum(moms[:,:,1:]**2, axis=-1)
        ptSq = pSq - moms[:,:, -1]**2
        protonMask = moms[:,:, 0]**2 - pSq > DetEff.mSqThr
        thr = np.empty(moms.shape[:-1])
        thr[protonMask], thr[~protonMask] = self.ptpSq, self.ptpiSq
        costh = moms[:,:,-1] / np.sqrt(pSq)
        return (np.abs(costh) < self.costh) & (ptSq > thr)

def applyDetEff(data, mask, sside):
    """ """
    return data[np.all(mask, axis=-1)]

def main():
    """ Unit test """
    data = np.random.rand(1000000, 4, 4)
    data[:,:,0] = np.sqrt(0.13**2 + np.sum(data[:,:,1:]**2, axis=-1))
    print(data.shape)
    deff = DetEff(60., 0.05)
    effMask = deff(data)
    print(effMask.shape)

if __name__ == '__main__':
    main()

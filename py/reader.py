from driver import LL

import numpy as np

class ReaderTxt(object):
    def __init__(self, fname, brief=False):
        self.f = open(fname, 'r')
        self.brief = brief

    def readEvents(self, nevt=None):
        if self.brief:
            return self.readSimple(nevt)

        events = []
        if nevt is None:
            nevt = 10**9
        while len(events) < nevt:
            event = self.readEvent()
            # print(event)
            if event is not None:
                events.append(event)
            else:
                break
        return np.array(events)

    def readEvent(self):
        firstLine = self.f.readline().strip()
        if (firstLine is None) or (firstLine != 'Event'):
            return None
        # skip momenta
        for i in range(4):
            self.f.readline()

        return map(float, self.f.readline().split())

    def readSimple(self, nevt):
        """ Read brief event format """
        events = []
        for line in self.f:
            if len(events) == nevt:
                break
            events.append(map(float, line.split()))
        return np.array(events)

def main():
    import matplotlib.pyplot as plt

    reader = ReaderTxt('../ll.dat')

    alpha = 0.6
    dphi = 0.5 * np.pi
    ll1 = LL(alpha, dphi, 0.6, -0.6,  1.)
    ll2 = LL(alpha, dphi, 0.6, -0.6, -1.)
    ll3 = LL(alpha, dphi, 0.6, -0.6,  0.)

    events = reader.readEvents()
    msq1 = ll1(events)  # / 5.03  # 5.02372410309
    msq2 = ll2(events)  # / 5.07  # 5.06247648097
    msq3 = ll3(events)  # / 2.71  # 2.69813970806
    msq1 = msq1 / max(msq1)
    msq2 = msq2 / max(msq2)
    msq3 = msq3 / max(msq3)

    print('min1: {}, max1: {}'.format(min(msq1), max(msq1)))
    print('min2: {}, max2: {}'.format(min(msq2), max(msq2)))
    print('min3: {}, max3: {}'.format(min(msq3), max(msq3)))
    
    plt.figure()
    plt.hist(msq1, bins=100, alpha=0.3, range=[0, 1], label='1')
    plt.hist(msq2, bins=100, alpha=0.3, range=[0, 1], label='-1')
    plt.hist(msq3, bins=100, alpha=0.3, range=[0, 1], label='0')
    plt.tight_layout()
    plt.grid()
    plt.legend(loc='best')
    plt.show()
    
    plt.figure()
    x = events[:, 1]
    plt.hist(x, bins=100, weights=msq1, density=True, alpha=0.3, range=[-1, 1], label='1')
    plt.hist(x, bins=100, weights=msq2, density=True, alpha=0.3, range=[-1, 1], label='-1')
    plt.tight_layout()
    plt.grid()
    plt.legend(loc='best')
    plt.show()
    
    xi = np.random.rand(len(events))
    data1 = events[msq1>xi]
    data2 = events[msq2>xi]
    data3 = events[msq3>xi]
    print(len(data1), len(data2), len(data3))
    
    plt.figure()
    plt.hist(data1[:, 1]*data1[:, 3], bins=100, density=True, alpha=0.3, range=[-1, 1], label='1')
    plt.hist(data2[:, 1]*data2[:, 3], bins=100, density=True, alpha=0.3, range=[-1, 1], label='-1')
    plt.tight_layout()
    plt.grid()
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()

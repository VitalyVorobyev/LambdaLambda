import numpy as np

class ReaderTxt(object):
    def __init__(self, fname, brief):
        """ Constructor. Args:
             - fname: input file name
             - type: type of reader
                * None (default) - read full event format skipping particle momenta
                * 'brief' - read brief event format
                * 'full' - read full event format and save particle momenta
        """
        self.f = open(fname, 'r')
        self.brief = brief

    def readEvent(self):
        firstLine = self.f.readline().strip()
        if (firstLine is None) or (firstLine != 'Event'):
            return (None, None)
        moms = [[float(x.strip()) for x in self.f.readline()[1:-2].split(',')] for _ in range(4)]
        return (moms, map(float, self.f.readline().split()))

    def readEvents(self, nevt=None):
        return self.readSimple(nevt) if self.brief else self.readDefault(nevt)

    def readDefault(self, nevt):
        events = []
        moms = []
        if nevt is None:
            nevt = 10**9
        while len(events) < nevt:
            mom, event = self.readEvent()
            if event is not None:
                events.append(event)
                moms.append(mom)
            else:
                break
        return (np.array(events), np.array(moms))

    def readSimple(self, nevt):
        """ Read brief event format """
        events = []
        for line in self.f:
            if len(events) == nevt:
                break
            events.append(map(float, line.split()))
        return np.array(events)

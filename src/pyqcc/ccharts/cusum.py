from .ccharts import ccharts
import numpy as np
from .tables import d2


class cusum(ccharts):

    _title = "CUSUM Chart"

    def __init__(self, target=None, std=None, interval=4, k=None):
        super(cusum, self).__init__()

        self.target = target
        self.std = std
        self.interval = interval

        if k is None:
            self.k = 0.5
        elif not isinstance(k, (int, float,)):
            self.k = 0.5
        else:
            self.k = k

    def plot(self, data, size, newdata=None):

        if size > 1:
            data = np.mean(data, axis=1)

        target = self.target
        std = self.std
        interval = self.interval

        if target is None:
            target = np.mean(data)

        if std is None:
            rbar = []
            for i in range(len(data) - 1):
                rbar.append(abs(data[i] - data[i + 1]))
            std = np.mean(rbar) / d2[2]

        k = self.k

        cplus = []  # values
        cminus = []  # values
        i, j = 0, 0
        for xi in data:
            cplus.append(max([0, xi - (target + k) + i]))
            cminus.append(min([0, xi - (target - k) + j]))
            i, j = cplus[-1], cminus[-1]

        lcl = -interval * std
        ucl = interval * std
        center = 0

        return ([cplus, cminus], center, lcl, ucl, self._title)

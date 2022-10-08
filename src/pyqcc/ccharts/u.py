from .ccharts import ccharts
import numpy as np


class u(ccharts):

    _title = "U Chart"

    def __init__(self, size=1):
        super(u, self).__init__()

        self.size = size - 1

    def plot(self, data, size, newdata=None):

        sizes, data = data.T
        if self.size == 1:
            sizes, data = data, sizes

        data2 = data / sizes
        ubar = np.sum(data) / np.sum(sizes)

        lcl, ucl = [], []
        for i in sizes:
            lcl.append(ubar - 3 * np.sqrt(ubar / i))
            ucl.append(ubar + 3 * np.sqrt(ubar / i))

        return (data2, ubar, lcl, ucl, self._title)

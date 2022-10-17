from .ccharts import ccharts
import numpy as np


class p(ccharts):

    _title = "P Chart"

    def __init__(self, size=1):
        super(p, self).__init__()

        self.size = size - 1

    def plot(self, data, size, newdata=None):

        sizes, data = data.T
        if self.size == 1:
            sizes, data = data, sizes

        data2 = data / sizes
        pbar = np.mean(data2)

        if np.mean(sizes) == sizes[0]:
            size = sizes[0]
            lcl = pbar - 3 * np.sqrt((pbar * (1 - pbar)) / size)
            ucl = pbar + 3 * np.sqrt((pbar * (1 - pbar)) / size)

            if lcl < 0:
                lcl = 0
            if ucl > 1:
                ucl = 1

            if newdata is not None:
                return (newdata, pbar, lcl, ucl, self._title)

            return (data2, pbar, lcl, ucl, self._title)

        else:
            lcl, ucl = [], []
            for size in sizes:
                lcl.append(pbar - 3 * np.sqrt((pbar * (1 - pbar)) / size))
                ucl.append(pbar + 3 * np.sqrt((pbar * (1 - pbar)) / size))
            
            if newdata is not None:
                return (newdata, pbar, lcl, ucl, self._title)

            return (data2, pbar, lcl, ucl, self._title)

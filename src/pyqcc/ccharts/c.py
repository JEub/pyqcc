from .ccharts import ccharts
import numpy as np


class c(ccharts):

    _title = "C chart"

    def __init__(self, size=1):
        super(c, self).__init__()

        self.size = size - 1

    def plot(self, data, size, newdata=None):

        sizes, data = data.T
        if self.size == 1:
            sizes, data = data, sizes

        # the samples must have the same size for this charts
        assert np.mean(sizes) == sizes[0]

        cbar = np.mean(data)

        lcl = cbar - 3 * np.sqrt(cbar)
        ucl = cbar + 3 * np.sqrt(cbar)

        return (data, cbar, lcl, ucl, self._title)

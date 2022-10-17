from .ccharts import ccharts
from .tables import D4, D3, d2
import numpy as np


class mr(ccharts):

    _title = "MR - Moving Range Chart"

    def plot(self, data, size, newdata=None):
        assert size == 1
        newvalues = None

        R = np.array(
            [np.nan] + [abs(data[i] - data[i + 1]) for i in range(len(data) - 1)]
        )

        if newdata:
            newdata = data[-1:] + newdata
            n = len(newdata)
            newvalues = [abs(newdata[i] - newdata[i + 1]) for i in range(n - 1)]

        Rbar = np.nanmean(R)

        lclr = D3[2] * Rbar
        uclr = D4[2] * Rbar

        return (R, Rbar, lclr, uclr, self._title)


class xmr(ccharts):

    _title = "X chart"

    def plot(self, data, size, newdata=None):
        assert size == 1
        newvalues = None

        R = np.array(
            [np.nan] + [abs(data[i] - data[i + 1]) for i in range(len(data) - 1)]
        )

        if newdata:
            newvalues = newdata

        Rbar = np.nanmean(R)
        Xbar = np.mean(data)

        lclx = Xbar - 3 * (Rbar / d2[2])
        uclx = Xbar + 3 * (Rbar / d2[2])

        return (data, Xbar, lclx, uclx, self._title)

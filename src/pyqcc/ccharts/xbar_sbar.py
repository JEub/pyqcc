from .ccharts import ccharts
from .tables import A3, B3, B4
import numpy as np


class xbar_sbar(ccharts):

    _title = "Xbar-S Chart"

    def plot(self, data, size, newdata=None):

        assert size >= 2
        assert size <= 10
        newvalues = None

        X, S = [], []
        for xs in data:
            assert len(xs) == size
            S.append(np.std(xs, ddof=1))
            X.append(np.mean(xs))

        if newdata is not None:
            newvalues = [np.mean(xs) for xs in newdata]

        sbar = np.mean(S)
        xbar = np.mean(X)

        lclx = xbar - A3[size] * sbar
        uclx = xbar + A3[size] * sbar

        if newvalues is not None:
            return (newvalues, xbar, lclx, uclx, self._title)

        return (X, xbar, lclx, uclx, self._title)


class sbar(ccharts):

    _title = "Standard Deviation Chart"

    def plot(self, data, size, newdata=None):

        assert size >= 2
        assert size <= 10
        newvalues = None

        S = []
        for xs in data:
            assert len(xs) == size
            S.append(np.std(xs, ddof=1))

        if newdata is not None:
            newvalues = [np.std(xs, ddof=1) for xs in newdata]

        sbar = np.mean(S)

        lcls = B3[size] * sbar
        ucls = B4[size] * sbar

        if newvalues is not None:
            return (newvalues, sbar, lcls, ucls, self._title)

        return (S, sbar, lcls, ucls, self._title)

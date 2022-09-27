from .ccharts import ccharts
from .tables import A2, D3, D4
import numpy as np


class xbar_rbar(ccharts):

    _title = "Xbar-R Chart"

    def plot(self, data, size, newdata=None):
        assert size >= 2
        assert size <= 10
        newvalues = None

        R, X = [], []  # values
        for xs in data:
            assert len(xs) == size
            R.append(max(xs) - min(xs))
            X.append(np.mean(xs))

        if newdata is not None:
            newvalues = [np.mean(xs) for xs in newdata]

        Rbar = np.mean(R)  # center
        Xbar = np.mean(X)

        lcl = Xbar - A2[size] * Rbar
        ucl = Xbar + A2[size] * Rbar

        if newvalues is not None:
            return (newvalues, Xbar, lcl, ucl, self._title)
        return (X, Xbar, lcl, ucl, self._title)


class rbar(ccharts):

    _title = "R Chart"

    def plot(self, data, size, newdata=None):
        assert size >= 2
        assert size <= 10
        newvalues = None

        R = []  # values
        for xs in data:
            assert len(xs) == size
            R.append(max(xs) - min(xs))

        if newdata is not None:
            newvalues = [max(xs) - min(xs) for xs in newdata]

        Rbar = np.mean(R)  # center

        lcl = D3[size] * Rbar
        ucl = D4[size] * Rbar

        if newvalues is not None:
            return (newvalues, Rbar, lcl, ucl, self._title)
        
        return (R, Rbar, lcl, ucl, self._title)

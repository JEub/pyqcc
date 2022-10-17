from .ccharts import ccharts
from .tables import A3, B3, B4
import numpy as np
from scipy import stats
from scipy.special import gamma
from math import sqrt


class xbar_sbar(ccharts):

    _title = "Xbar-S Chart"

    def plot(self, data, size, newdata=None):

        assert size >= 2
        
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
        
        if size <= 10:
            a3 = A3[size]
        else:
            c4 = (gamma(size / 2) * sqrt(2/(size - 1))) / (gamma((n-1)/2))
            a3 = 3 / (c4 * sqrt(size))
        
        lclx = xbar - a3 * sbar
        uclx = xbar + a3 * sbar

        if newvalues is not None:
            return (newvalues, xbar, lclx, uclx, self._title)

        return (X, xbar, lclx, uclx, self._title)


class sbar(ccharts):

    _title = "Standard Deviation Chart"

    def plot(self, data, size, newdata=None):

        assert size >= 2

        newvalues = None

        S = []
        for xs in data:
            assert len(xs) == size
            S.append(np.std(xs, ddof=1))

        if newdata is not None:
            newvalues = [np.std(xs, ddof=1) for xs in newdata]

        sbar = np.mean(S)

        if size <= 10:
            b3 = B3[size]
            b4 = B4[size]
        else:
            c4 = (gamma(size / 2) * sqrt(2/(size - 1))) / (gamma((n-1)/2))
            b3 = 1 - (3 / (c4 * (sqrt(2*(size-1)))))
            b4 = 1 + (3 / (c4 * (sqrt(2*(size-1)))))

        lcls = b3 * sbar
        ucls = b4 * sbar

        if newvalues is not None:
            return (newvalues, sbar, lcls, ucls, self._title)

        return (S, sbar, lcls, ucls, self._title)

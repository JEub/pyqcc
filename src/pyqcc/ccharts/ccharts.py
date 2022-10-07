#!/usr/bin/env python3

from ..pyqcc import qcc


class ccharts(object):

    def __init__(self):
        self.layers = [self]

    def __radd__(self, model):
        if isinstance(model, qcc):
            model.layers += self.layers
            return model

        self.layers.append(model)
        return self

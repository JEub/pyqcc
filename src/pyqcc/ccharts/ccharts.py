#!/usr/bin/env python3

from ..pyqcc import spc


class ccharts(object):

    def __init__(self):
        self.layers = [self]

    def __radd__(self, model):
        if isinstance(model, spc):
            model.layers += self.layers
            return model

        self.layers.append(model)
        return self

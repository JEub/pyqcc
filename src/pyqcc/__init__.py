#!/usr/bin/env python3
#
#  Copyright (C) 2022 James Eubanks <jeubanks.github@gmail.com>
# 
# Orignal work - pyspc
#   Copyright (C) 2016  Carlos Henrique Silva <carlosqsilva@outlook.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
__version__ = '0.1.1'
__author__ = "James Eubanks"
__email__ = "jeubanks.github@gmail.com"

import warnings
warnings.simplefilter("ignore")

# For testing purposes we might need to set mpl backend before any
# other import of matplotlib.
# def _set_mpl_backend():
#     import os
#     import matplotlib as mpl

#     env_backend = os.environ.get('MATPLOTLIB_BACKEND')
#     if env_backend:
#         # we were instructed
#         mpl.use(env_backend)

#_set_mpl_backend()


from .ccharts import *
from .sampledata import *

from .pyqcc import qcc
from .rules import rules

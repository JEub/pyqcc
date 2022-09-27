#!/usr/bin/env python3
from pyqcc import *

a = qcc(pistonrings) + cusum() + ewma() + rules()
#print(a)
b = qcc(pistonrings) + xbar_sbar() + sbar() + rules()
#print(b)
c = qcc(viscosidade) + xmr() + mr() + cusum() + rules()
#print(c)
d = qcc(plastic) + Tsquare_single() + rules()
#print(d)
e = qcc(experiment) + Tsquare()
#print(e)
f = qcc(mewma_example) + mewma() + rules()
#print(f)

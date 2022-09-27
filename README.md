# PyQCC
Version: 0.1.2  

This package is a modification of the original Work by Carlos Henrique Silva's <carlosqsilva@outlook.com> `pyspc` package. The original work can be found [here](https://github.com/carlosqsilva/pyspc). 

Statistical Process Control Charts Library for Humans

PyQCC is a Python library aimed to make Statistical Process Control Charts as easy as possible but especially relevant to statsisticians for performing Quality Control.

## Features

Control Charts by Variables
* Mean and Amplitude
* Mean and Standard Deviation
* Individual Values and Moving Range
* Individual values with subgroups
* Exponentially Weighted Moving Average (EWMA)
* Cumulative Sum (CUSUM)

Control Charts by Attributes
* P Chart
* NP Chart
* C Chart
* U Chart

Multivariate Control Charts
* T Square Hotelling
* T Square Hotelling with SubGroup
* Multivariate Exponentially Weighted Moving Average (MEWMA)

## Installation
```bash
$ pip install pyqcc
```

## Usage
```python
from pyqcc import *

a = qcc(pistonrings) + ewma()
print(a)
```
<img src="https://github.com/jeub/pyqcc/blob/main/screenshots/1-screen.png" align="center" height="400" width="450">

adding rules highlighting...
```python
a + rules()
```

<img src="https://github.com/jeub/pyqcc/blob/main/screenshots/2-screen.png" align="center" height="400" width="450">

adding more control charts to the mix...
```python
a + cusum() + xbar_sbar() + sbar()
``` 

<img src="https://github.com/jeub/pyqcc/blob/main/screenshots/3-screen.png" align="center" height="500" width="450">

it comes with 18 sample datasets to play with, available in **./pyspc/sampledata**, you can use your own data (of course). Your data can be nested lists, numpy array or pandas DataFrame.
```python
import numpy
from pyqcc import *
fake_data = numpy.random.randn(30, 5) + 100
a = qcc(fake_data) + xbar_rbar() + rbar() + rules()
print(a)
```

<img src="https://github.com/jeub/pyqcc/blob/main/screenshots/5-screen.png" align="center" height="400" width="450">

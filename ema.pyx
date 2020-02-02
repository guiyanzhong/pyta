"""
EMA: Exponential Moving Average.
"""

import numpy as np
from pandas import Series


def ema(arg, int window):
    """EMA: Exponential Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Exponential moving average of arg.
    """
    arg = Series(arg.dropna().values, index = arg.index)
    cdef double[:] _arg = arg.values
    ema = np.empty(len(arg))
    cdef double w = 2.0 / (window + 1)
    cdef int i
    ema[0] = _arg[0]
    for i in range(1, len(arg)):
        ema[i] = _arg[i] * w + ema[i-1] * (1.0 - w)

    return Series(data = ema, name = "ema" + str(window), index = arg.index)

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

    cdef double[:] values = arg.values
    ema = np.empty(len(arg))
    cdef double w = 2.0 / (window + 1)
    cdef int i
    cdef int first_value_processed = 0

    for i in range(len(values)):
        if values[i] != values[i]:
            ema[i] = values[i]
        else:
            if first_value_processed == 0:
                e = values[i]
                first_value_processed = 1
            else:
                e = values[i] * w + e * (1.0 - w)
            ema[i] = e

    return Series(data = ema, name = "ema" + str(window), index = arg.index)

"""
KD: KD indicator.
"""


import numpy as np
import pandas as pd


def kd(ohlc, int n=9, int m1=3, int m2=3):
    """KD indicator.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (open, high, low, close).

        n, m1, m2 (int): KD params.

    Returns:
        DataFrame: K & D values.
    """

    cdef double[:] closes = ohlc["close"].values
    cdef double[:] highs = ohlc["high"].values
    cdef double[:] lows = ohlc["low"].values
    cdef int _len = closes.size
    cdef int i, j

    # RSV = (C - Ln) / (Hn - Ln) * 100
    rsv = np.empty(_len)
    rsv[:] = np.nan
    for i in range(n - 1, _len):
        lowest = lows[i]
        highest = highs[i]
        for j in range(1, n):
            if (lowest > lows[i - j]):
                lowest = lows[i - j]
            if (highest < highs[i - j]):
                highest = highs[i - j]
        rsv[i] = (closes[i] - lowest) / (highest - lowest) * 100
    # K = 2/3 * prevK + 1/3 * RSV
    # D = 2/3 * prevD + 1/3 * K
    # If no prevK or prevD, use 50 instead
    k = np.empty(_len)
    k[:] = np.nan
    d = np.empty(_len)
    d[:] = np.nan
    k[0] = 50
    d[0] = 50
    for i in range(1, _len):
        if (np.isnan(rsv[i])):
            k[i] = 50; k[i - 1] = np.nan
            d[i] = 50; d[i - 1] = np.nan
        else:
            k[i] = k[i - 1] * (m1 - 1) / m1 + rsv[i] / m1
            d[i] = d[i - 1] * (m2 - 1) / m2 + k[i] / m2
    # Mark: J = 3K - 2D
    return pd.DataFrame({"K": k, "D": d})

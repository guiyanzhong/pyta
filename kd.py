"""
KD: KD indicator.
"""


from datautils import gen_ohlc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def kd(ohlc, n=9, m1=3, m2=3):
    """KD indicator.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (open, high, low, close).

        n, m1, m2 (int): KD params.

    Returns:
        DataFrame: K & D values.
    """

    closes = ohlc["close"].values
    highs = ohlc["high"].values
    lows = ohlc["low"].values
    _len = closes.size

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
    k[0] = 50;
    d[0] = 50;
    for i in range(1, _len):
        if (np.isnan(rsv[i])):
            k[i] = 50; k[i - 1] = np.nan
            d[i] = 50; d[i - 1] = np.nan
        else:
            k[i] = k[i - 1] * (m1 - 1) / m1 + rsv[i] / m1
            d[i] = d[i - 1] * (m2 - 1) / m2 + k[i] / m2
    # Mark: J = 3K - 2D
    return pd.DataFrame({"K": k, "D": d})


def test_kd(ohlc):
    """KD test function."""
    kd_indicator = kd(ohlc, 9, 3, 3)

    # Plot the price series.
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
    ax1.grid(True)
    ax1.plot(ohlc["close"])
    plt.ylabel("CLOSE")
    plt.title("KD Chart")

    # Plot KD.
    ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=2, colspan=4)
    ax2.grid(True)
    ax2.plot(kd_indicator)
    plt.ylabel("KD")
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.show()


if __name__ == "__main__":
    test_kd(gen_ohlc())

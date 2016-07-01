"""
ATR: Average True Range.
"""


from datautils import gen_ohlc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sma import sma


def atr(ohlc, window=14):
    """ATR: Average True Range.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (opens, highs, lows, closes).

        window (int): ATR window size.

    Returns:
        Series: Average True Range of ohlc.
    """

    tr1 = ohlc["highs"] - ohlc["lows"]
    pre_closes = ohlc["closes"].shift(1)
    tr2 = (ohlc["highs"] - pre_closes).abs()
    tr3 = (ohlc["highs"] - pre_closes).abs()
    tr = np.maximum(np.maximum(tr1, tr2), tr3)

    atr = sma(tr, window)

    return Series(data = atr, name = "ATR_%d" % window)


def test_atr(ohlc):
    """ATR test function."""
    atr_indicator = atr(ohlc)

    # Plot the price series.
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
    ax1.grid(True)
    ax1.plot(ohlc["closes"])
    plt.ylabel("CLOSE")
    plt.title("ATR Chart")

    # Plot ATR.
    ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=2, colspan=4)
    ax2.grid(True)
    ax2.plot(atr_indicator)
    plt.ylabel("ATR")
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.show()


if __name__ == "__main__":
    test_atr(gen_ohlc())

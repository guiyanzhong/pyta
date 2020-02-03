"""
ATR: Average True Range.
"""


import pyximport; pyximport.install()
from datautils import gen_ohlc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
from sma import sma


def atr(ohlc, window=14):
    """ATR: Average True Range.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (open, high, low, close).

        window (int): ATR window size.

    Returns:
        DataFrame: True Range & Average True Range of ohlc.
    """

    tr1 = ohlc["high"].values - ohlc["low"].values
    pre_closes = ohlc["close"].shift(1).values
    tr2 = np.absolute(ohlc["high"].values - pre_closes)
    tr3 = np.absolute(ohlc["low"].values - pre_closes)
    tr = pd.Series(np.maximum(np.maximum(tr1, tr2), tr3))
    tr.name = "tr"
    tr.index = ohlc.index

    atr = sma(tr, window)
    atr.name = "atr%d" % window

    return pd.concat([tr, atr], axis=1)


def test_atr(ohlc):
    """ATR test function."""
    atr_indicator = atr(ohlc)

    # Plot the price series.
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
    ax1.grid(True)
    ax1.plot(ohlc["close"])
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

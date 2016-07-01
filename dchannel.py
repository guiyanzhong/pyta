"""
DCHANNEL: Donchain Channel.
"""

from datautils import gen_ohlc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.finance import candlestick2
from pandas import Series, DataFrame


def dchannel(ohlc, window):
    """DCHANNEL: Donchain Channel.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (opens, highs, lows, closes).

        window (int): Donchain Channel window size.

    Returns:
        DataFrame: Donchain Channel of ohlc."
    """

    dchannel_up = pd.rolling_max(ohlc["highs"], window)
    dchannel_low = pd.rolling_min(ohlc["lows"], window)

    return DataFrame({"dchannel_up":dchannel_up, "dchannel_low":dchannel_low})


def test_dchannel(ohlc):
    """DCHANNEL test function."""
    dchannel10 = dchannel(ohlc, 10)
    data = pd.concat([ohlc, dchannel10], axis=1)
    # print(data)
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=6)
    ax1.grid(True)
    candlestick2(ax1, ohlc["opens"], ohlc["closes"], ohlc["highs"], ohlc["lows"], width=0.7, colorup="r", colordown="g")
    ax1.plot(dchannel10)
    plt.title("DCHANNEL Chart")
    plt.show()


if __name__ == "__main__":
    test_dchannel(gen_ohlc())

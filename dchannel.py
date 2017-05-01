"""
DCHANNEL: Donchain Channel.
"""

from datautils import gen_ohlc
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.finance import candlestick2_ochl
from pandas import DataFrame


def dchannel(ohlc, window):
    """DCHANNEL: Donchain Channel.

    Params:
        ohlc (DataFrame): Time series data of OHLC prices (open, high, low, close).

        window (int): Donchain Channel window size.

    Returns:
        DataFrame: Donchain Channel of ohlc."
    """

    dchannel_high = ohlc["high"].rolling(window=window).max()
    dchannel_low = ohlc["low"].rolling(window=window).min()

    return DataFrame({"dchannel_high":dchannel_high, "dchannel_low":dchannel_low})


def test_dchannel(ohlc):
    """DCHANNEL test function."""
    dchannel10 = dchannel(ohlc, 10)
    data = pd.concat([ohlc, dchannel10], axis=1)
    # print(data)
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=6)
    ax1.grid(True)
    candlestick2_ochl(ax1, ohlc["open"], ohlc["close"], ohlc["high"], ohlc["low"], width=0.7, colorup="r", colordown="g")
    ax1.plot(dchannel10)
    plt.title("DCHANNEL Chart")
    plt.show()


if __name__ == "__main__":
    test_dchannel(gen_ohlc())

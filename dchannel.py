"""
DCHANNEL: Donchain Channel.
"""

import pyximport; pyximport.install()
from datautils import gen_ohlc
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf
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
    # Add a date index for mplfinance
    ohlc.index = pd.date_range("2024-08-01", periods=len(ohlc))
    # Calculate DCHANNEL
    dchannel10 = dchannel(ohlc, 10)
    # Plot
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=6)
    ax1.grid(True)
    dc = mpf.make_addplot(dchannel10, ax=ax1)
    mpf.plot(ohlc, type='candle', style='charles', addplot=dc, ax=ax1)
    plt.title("DCHANNEL Chart")
    plt.show()


if __name__ == "__main__":
    test_dchannel(gen_ohlc())

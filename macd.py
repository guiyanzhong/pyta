"""
MACD: Moving Average Convergence/Divergence.
"""

from datautils import gen_closes
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from ema import ema


def macd(closes, p1=12, p2=26, p3=9, ma=ema):
    """MACD: Moving Average Convergence/Divergence.

    Params:
        closes (Series): Time series data of close prices.

        p1, p2, p3 (int): Moving average window size in MACD, default to (12, 26, 9).

        ma (function): Moving average function used in MACD calculation, can be ema or dema.

    Returns:
        Series: MACD of closes.
    """

    ma1 = ma(closes, p1)
    ma2 = ma(closes, p2)
    macd = ma1 - ma2
    signal = ma(macd, p3)
    divergence = macd - signal

    return DataFrame({"macd":macd, "signal":signal, "divergence":divergence})


def test_macd(closes):
    """MACD test function."""
    macd_indicator = macd(closes)
    data = macd_indicator
    # print(data)

    # Plot the price series.
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
    ax1.grid(True)
    ax1.plot(closes)
    plt.ylabel("CLOSE")
    plt.title("MACD Chart")

    # Plot MACD.
    ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=2, colspan=4)
    ax2.grid(True)
    ax2.plot(data["macd"])
    ax2.plot(data["signal"])
    ax2.fill_between(data.index, data["divergence"], 0, alpha=0.5)
    plt.ylabel("MACD")
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.show()


if __name__ == "__main__":
    test_macd(gen_closes())

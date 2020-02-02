"""
DEMA: Double Exponential Moving Average.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series
from ema import ema


def dema(arg, window):
    """DEMA: Double Exponential Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Double exponential moving average of arg.
    """

    ema1 = ema(arg, window)
    ema2 = ema(ema1, window)
    dema = ema1 * 2 - ema2

    return Series(data = dema, name = "dema" + str(window))


def test_dema(closes):
    """DEMA test function."""
    dema5 = dema(closes, 5)
    dema10 = dema(closes, 10)
    data = pd.concat([closes, dema5, dema10], axis=1)
    # print(data)
    data.plot(title = "DEMA Chart")
    plt.show()


if __name__ == "__main__":
    test_dema(gen_closes())

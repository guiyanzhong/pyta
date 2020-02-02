"""
SMA: Simple Moving Average.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series


def sma(arg, window):
    """SMA: Simple Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Simple moving average of arg.
    """

    ma = arg.rolling(window=window,center=False).mean()
    return Series(data = ma, name = "sma" + str(window))


def test_sma(closes):
    """SMA test function."""
    sma5 = sma(closes, 5)
    sma10 = sma(closes, 10)
    data = pd.concat([closes, sma5, sma10], axis=1)
    # print(data)
    data.plot(title = "SMA Chart")
    plt.show()


if __name__ == "__main__":
    test_sma(gen_closes())

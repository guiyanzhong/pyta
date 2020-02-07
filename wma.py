"""
WMA: Weighted Moving Average.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series


def wma(arg, window):
    """WMA: Weighted Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Weighted moving average of arg.
    """

    values = arg.values
    wma = []
    bar_count = len(arg)
    nan_count = window - 1
    if bar_count < nan_count:
        nan_count = bar_count
    for i in range(nan_count):
        wma.append(np.nan)
    div = (window + 1) * window / 2.0
    for i in range(window-1, bar_count):
        sum = 0
        for j in range(window):
            sum += values[i - j] * (window - j)
        wma.append(sum / div);

    return Series(data = wma, name="wma" + str(window), index = arg.index)


def test_wma(closes):
    """WMA test function."""
    wma5 = wma(closes, 5)
    wma10 = wma(closes, 10)
    data = pd.concat([closes, wma5, wma10], axis=1)
    # print(data)
    data.plot(title = "WMA Chart")
    plt.show()


if __name__ == "__main__":
    test_wma(gen_closes())

"""
EMA: Exponential Moving Average.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series


def ema(arg, window):
    """EMA: Exponential Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Exponential moving average of arg.
    """
    arg = Series(arg.dropna().values, index = arg.index)
    ema = []
    w = 2.0 / (window + 1)
    ema.append(arg[0])
    for i in range(1, len(arg)):
        ema.append(arg[i] * w + ema[-1] * (1.0 - w))

    return Series(data = ema, name = "ema" + str(window), index = arg.index)


def test_ema(closes):
    """EMA test function."""
    ema5 = ema(closes, 5)
    ema10 = ema(closes, 10)
    data = pd.concat([closes, ema5, ema10], axis=1)
    # print(data)
    data.plot(title = "EMA Chart")
    plt.show()


if __name__ == "__main__":
    test_ema(gen_closes())

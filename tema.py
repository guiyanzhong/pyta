"""
TEMA: Triple Exponential Moving Average.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series
from ema import ema


def tema(arg, window):
    """TEMA: Triple Exponential Moving Average.

    Params:
        arg (Series): Time series data such as close prices.

        window (int): Moving average window size.

    Returns:
        Series: Triple exponential moving average of arg.
    """

    ema1 = ema(arg, window)
    ema2 = ema(ema1, window)
    ema3 = ema(ema2, window)
    tema = ema1 * 3 - ema2 * 3 + ema3

    return Series(data = tema, name = "tema" + str(window))


def test_tema(closes):
    """TEMA test function."""
    tema5 = tema(closes, 5)
    tema10 = tema(closes, 10)
    data = pd.concat([closes, tema5, tema10], axis=1)
    # print(data)
    data.plot(title = "TEMA Chart")
    plt.show()


if __name__ == "__main__":
    test_tema(gen_closes())

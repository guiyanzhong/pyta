"""
BBANDS: Bollinger Bands.
"""

import pyximport; pyximport.install()
from datautils import gen_closes
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sma import sma


def bbands(closes, window=20, d=2):
    """
    BBANDS: Bollinger Bands.

    Params:
        closes (Series): Time series of closing prices.

        window (int): Moving average window size.

        d (int): Standard deviation multiple.

    Returns:
        DataFrame: Bollinger Bands of the closing price series.
    """

    def calc_sd():
        """
        Calculate (moving) standard deviation of the closing price series,
        which will be used in calculating Bollinger Bands.
        """
        sd = [np.nan] * min(closes.size, window - 1)
        for i in range(window - 1, closes.size):
            sum = 0.0
            m = boll_mid[i]
            for j in range(window):
                sum += (closes[i - j] - m) ** 2;
            sd.append(math.sqrt(sum / window))
        return Series(data = sd, name = "sd")

    boll_mid = sma(closes, window)
    sd = calc_sd()
    boll_up = boll_mid + sd * d
    boll_low = boll_mid - sd * d

    return DataFrame({"boll_up":boll_up, "boll_mid":boll_mid, "boll_low":boll_low})


def test_bbands(closes):
    """BBANDS test function."""
    bb = bbands(closes, 20, 2)
    data = pd.concat([DataFrame(closes), bb], axis=1)
    # print(data)
    data.plot(title = "BBANDS Chart")
    plt.show()


if __name__ == "__main__":
    test_bbands(gen_closes(200))

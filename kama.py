"""
KAMA: Kaufmans Adaptive Moving Average.
"""

from datautils import gen_closes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series


def kama(x, n=10, pow1=2, pow2=30):
    """KAMA: Kaufmans Adaptive Moving Average.

    Params:
        x (Series): Time series data such as close prices.

        n (int): number of periods for the Efficiency Ratio (ER).

        pow1 (int): number of periods for the fastest EMA constant.

        pow2 (int): number of periods for the slowest EMA constant.

    Returns:
        Series: Kaufmans adaptive moving average of x.
    """

    nan_count = x[pd.isnull(x)].size
    x = Series(x.dropna().values, name = x.name)

    change = (x - x.shift(n)).abs()
    volatility = (x - x.shift(1)).abs().rolling(window=n).sum()
    er = change / volatility
    sc = (er * (2.0 /(pow1 + 1.0) - 2.0 / (pow2 + 1.0)) + 2.0 / (pow2 + 1.0)) ** 2.0

    kama = [np.nan] * sc.size
    first_value = True
    for i in range(len(kama)):
        if not pd.isnull(sc[i]):
            if first_value:
                kama[i] = x[i]
                first_value = False
            else:
                kama[i] = kama[i-1] + sc[i] * (x[i] - kama[i-1])

    return Series(data = [np.nan] * nan_count + kama, name = "kama(%d,%d,%d)" % (n, pow1, pow2))


def test_kama(closes):
    """KAMA test function."""
    kama10 = kama(closes, 10, 2, 30)
    data = pd.concat([closes, kama10], axis=1)
#    print(data)
    data.plot(title = "KAMA Chart")
    plt.show()


if __name__ == "__main__":
    test_kama(gen_closes())

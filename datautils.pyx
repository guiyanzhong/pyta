"""
Module for test data preparations.
"""


from pandas import Series, DataFrame
import pandas as pd
import numpy as np


def gen_ohlc(int count=100):
    """
    Generate random walk OHLC price data.

    Params:
        count (int): How many bars in the generated OHLC data.

    Returns:
        DataFrame: Containing columns of "open", "high", "low" and "close".
    """

    # Generate ticks.
    cdef int bar_tick_count = 100
    cdef int i, j
    ticks = np.cumsum(np.random.standard_normal(count * bar_tick_count)) + 500.0
    # Generate OHLC from ticks.
    j = -1; o = ticks[0]; h = o; l = o; c = o
    opens = []; highs = []; lows = []; closes = []
    for i in range(ticks.size):
        if i // bar_tick_count != j:
            j = i // bar_tick_count
            opens.append(o); highs.append(h); lows.append(l); closes.append(c)
            o = ticks[i]; h = o; l = o; c = o
        else:
            if ticks[i] > h:
                h = ticks[i]
            if ticks[i] < l:
                l = ticks[i]
            c = ticks[i]
    opens.append(o); highs.append(h); lows.append(l); closes.append(c)
    opens.pop(0); highs.pop(0); lows.pop(0); closes.pop(0)
    return DataFrame({"open":opens, "high":highs, "low":lows, "close":closes})


def gen_closes(count=100):
    """
    Generate random walk close price data.

    Params:
        count (int): How many close prices in the generated data.

    Returns:
        Series: Series of close prices.
    """

    return Series(data = np.cumsum(np.random.standard_normal(count)) + 500.0, name = "close")



if __name__ == "__main__":
    # Test gen_closes().
    pd.options.display.max_rows = 10
    closes = gen_closes()
    print("\ngen_closes():\n", closes)
    # Test gen_ohlc().
    pd.options.display.max_rows = 5
    ohlc = gen_ohlc()
    print("\ngen_ohlc():\n", ohlc)

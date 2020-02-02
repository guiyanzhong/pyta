import pyximport; pyximport.install()
from datautils import gen_closes
from ema import ema
import matplotlib.pyplot as plt
import pandas as pd


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

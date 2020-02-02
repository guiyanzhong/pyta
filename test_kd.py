import pyximport; pyximport.install()
from datautils import gen_ohlc
from kd import kd
import matplotlib.pyplot as plt


def test_kd(ohlc):
    """KD test function."""
    kd_indicator = kd(ohlc, 9, 3, 3)

    # Plot the price series.
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=4, colspan=4)
    ax1.grid(True)
    ax1.plot(ohlc["close"])
    plt.ylabel("CLOSE")
    plt.title("KD Chart")

    # Plot KD.
    ax2 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=2, colspan=4)
    ax2.grid(True)
    ax2.plot(kd_indicator)
    plt.ylabel("KD")
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.show()


if __name__ == "__main__":
    test_kd(gen_ohlc())

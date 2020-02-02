import pyximport; pyximport.install()
from datautils import gen_ohlc
from kd import kd
import matplotlib.pyplot as plt
import time


def test_kd(ohlc):
    t1 = time.time()
    for i in range(10):
        kd_indicator = kd(ohlc, 9, 3, 3)
    t2 = time.time()
    print("Calculate KD: \t\t %gs" % ((t2 - t1) / 10.0))
    # print(kd_indicator)


if __name__ == "__main__":
    cnt = 100000
    t1 = time.time()
    ohlc = gen_ohlc(cnt)
    t2 = time.time()
    print("Generate %d bars: \t %gs" % (cnt, (t2 - t1)))
    test_kd(ohlc)

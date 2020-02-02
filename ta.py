"""
Meta module that import all technical indicators functions,
such as EMA, MACD, Bollinger Bands etc.
"""

import pyximport; pyximport.install()

from pandas import Series, DataFrame
import numpy as np

import datautils
import atr
import sma
import ema
import dema
import tema
import wma
import kama
import macd
import test_kd
import bbands
import dchannel

if __name__ == "__main__":
    # Generate test data.
    ohlc = datautils.gen_ohlc()
    closes = ohlc["close"]
    # Test indicators.
    atr.test_atr(ohlc)
    sma.test_sma(closes)
    ema.test_ema(closes)
    dema.test_dema(closes)
    tema.test_tema(closes)
    wma.test_wma(closes)
    kama.test_kama(closes)
    macd.test_macd(closes)
    test_kd.test_kd(ohlc)
    bbands.test_bbands(closes)
    dchannel.test_dchannel(ohlc)

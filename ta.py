"""
Meta module that import all technical indicators functions,
such as EMA, MACD, Bollinger Bands etc.
"""

from pandas import Series, DataFrame
import numpy as np

from datautils import gen_ohlc
from datautils import gen_closes
from atr import atr, test_atr
from sma import sma, test_sma
from ema import ema, test_ema
from dema import dema, test_dema
from tema import tema, test_tema
from wma import wma, test_wma
from kama import kama, test_kama
from macd import macd, test_macd
from kd import kd, test_kd
from bbands import  bbands, test_bbands
from dchannel import  dchannel, test_dchannel


if __name__ == "__main__":
    # Generate test data.
    ohlc = gen_ohlc()
    closes = ohlc["close"]
    # Test indicators.
    test_atr(ohlc)
    test_sma(closes)
    test_ema(closes)
    test_dema(closes)
    test_tema(closes)
    test_wma(closes)
    test_kama(closes)
    test_macd(closes)
    test_kd(ohlc)
    test_bbands(closes)
    test_dchannel(ohlc)

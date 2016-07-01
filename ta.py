"""
Meta module that import all technical indicators functions,
such as MA, EMA, AMA, MACD, Bollinger Bands etc.
"""

from pandas import Series, DataFrame
import numpy as np

from datautils import gen_ohlc
from atr import atr, test_atr
from sma import sma, test_sma
from ema import ema, test_ema
from dema import dema, test_dema
from tema import tema, test_tema
from kama import kama, test_kama
from macd import macd, test_macd
from bbands import  bbands, test_bbands
from dchannel import  dchannel, test_dchannel


if __name__ == "__main__":
    # Generate test data.
    ohlc = gen_ohlc()
    closes = ohlc["closes"]
    # Test indicators.
    test_atr(ohlc)
    test_sma(closes)
    test_ema(closes)
    test_dema(closes)
    test_tema(closes)
    test_kama(closes)
    test_macd(closes)
    test_bbands(closes)
    test_dchannel(ohlc)

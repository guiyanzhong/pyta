import pyximport; pyximport.install()
from datautils import gen_ohlc
import atr
import bbands
import dchannel
import sma
import ema
import dema
import tema
import wma
import kama
import kd
import macd
import matplotlib.pyplot as plt
import time

cnt = 10000

t1 = time.time()
ohlc = gen_ohlc(cnt)
closes = ohlc["close"]
t2 = time.time()
print("Generate %d bars: \t %gs" % (cnt, (t2 - t1)))

t1 = time.time()
for i in range(1):
    indicator = atr.atr(ohlc)
print("Calculate ATR: \t\t %gs" % ((time.time() - t1) / 1.0))

t1 = time.time()
for i in range(1):
    indicator = bbands.bbands(closes, 20, 2.0)
print("Calculate BOLL: \t %gs" % ((time.time() - t1) / 1.0))

t1 = time.time()
for i in range(10):
    indicator = dchannel.dchannel(ohlc, 10)
print("Calculate DCHANNEL: \t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = sma.sma(closes, 10)
print("Calculate SMA: \t\t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = ema.ema(closes, 10)
print("Calculate EMA: \t\t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = dema.dema(closes, 10)
print("Calculate DEMA: \t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = tema.tema(closes, 10)
print("Calculate TEMA: \t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(1):
    indicator = wma.wma(closes, 10)
print("Calculate WMA: \t\t %gs" % ((time.time() - t1) / 1.0))

t1 = time.time()
for i in range(10):
    indicator = kama.kama(closes)
print("Calculate KAMA: \t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = kd.kd(ohlc)
print("Calculate KD: \t\t %gs" % ((time.time() - t1) / 10.0))

t1 = time.time()
for i in range(10):
    indicator = macd.macd(closes)
print("Calculate MACD: \t %gs" % ((time.time() - t1) / 10.0))

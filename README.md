# pyta

Financial market technical analysis indicators implemented in Python.

> Implemented indicators include:

- SMA
- EMA
- DEMA
- TEMA
- WMA
- KAMA
- KD
- MACD
- Bollinger Bands
- Donchian Channel
- ATR

> Dependencies:

- cython
- numpy
- pandas
- matplotlib

> Try it:

- python3 ta.py

> Performance:

Action              | Time
--------------------|---------------
Generate 10000 bars | 0.351827s
Calculate ATR       | 0.00291061s
Calculate BOLL      | 1.78936s
Calculate DCHANNEL  | 0.00190716s
Calculate SMA       | 0.000572467s
Calculate EMA       | 0.00386355s
Calculate DEMA      | 0.00800772s
Calculate TEMA      | 0.0122036s
Calculate WMA       | 0.829549s
Calculate KAMA      | 0.242825s
Calculate KD        | 0.0434763s
Calculate MACD      | 0.0120981s

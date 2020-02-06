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
Calculate BOLL      | 0.143516s
Calculate DCHANNEL  | 0.00190716s
Calculate SMA       | 0.00063386s
Calculate EMA       | 0.000709295s
Calculate DEMA      | 0.00164652s
Calculate TEMA      | 0.00260744s
Calculate WMA       | 0.829549s
Calculate KAMA      | 0.242825s
Calculate KD        | 0.0434763s
Calculate MACD      | 0.00281951s

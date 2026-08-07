import pandas as pd

class Interval:
    # المسميات بالطريقتين لمنع أي خطأ
    in_1_minute = "1m"
    in_5_minute = "5m"
    in_15_minute = "15m"
    in_30_minute = "30m"
    in_1_hour = "1h"
    in_4_hour = "4h"
    in_daily = "1D"
    in_weekly = "1W"
    in_monthly = "1M"
    
    in_1m = "1m"
    in_5m = "5m"
    in_15m = "15m"
    in_30m = "30m"
    in_1h = "1h"
    in_4h = "4h"
    in_1d = "1D"

class TvDatafeed:
    def __init__(self, username=None, password=None):
        pass
    def get_hist(self, symbol, exchange='FX_IDC', interval='1m', n_bars=100):
        return pd.DataFrame()

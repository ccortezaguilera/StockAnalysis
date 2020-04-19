"""
############
stock_day.py
############
"""


class StockDay(object):
    def __init__(self, date, open, high, low, close, volume):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        # self.adj_close = adj_close

    def get_abs_diff(self):
        return abs(self.close - self.open)

    def increase(self):
        return self.close - self.open

    def decrease(self):
        return self.open - self.close

    def percent_increase(self):
        return ((self.close - self.open) / self.open) * 100

    def percent_decrease(self):
        return ((self.open - self.close) / self.open) * 100

    def __str__(self):
        return "%s %f %f %f %f %d" % (
            str(self.date),
            self.open,
            self.high,
            self.low,
            self.close,
            self.volume,
        )

# stock_day.py - class definition


class StockDay(object):

    def __init__(self, date, open, high, low, close, volume, adj_close):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close

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

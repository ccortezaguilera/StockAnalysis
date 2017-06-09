#stock_history.py
import sys
import stock_day

class StockHistory:

    def __init__(self, symbol, filename):
        self.symbol = symbol
        self.history = []
        self.month_history = {}
        self.date_history = {}
        self.__read_file(filename)

    def __read_file(self, filename):
        with open(filename, 'r') as f:
            stock_lines = f.readlines()
            stock_lines = stock_lines[1:]

            for line in stock_lines:
                line = line.strip()
                values = line.split(',')
                print(values[0], values[1], values[2], values[3])
                #day = stock_day.StockDay()
                #self.history.append(day)
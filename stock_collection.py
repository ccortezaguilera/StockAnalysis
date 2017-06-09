# uses epoch time for the date
import time

class StockCollection(object):

    def __init__(self):
        self.stocks = {}

    def download_stock(self, symbol):
        todays_date = int(time.mktime(time.strptime(time.time(), '%Y-%m-%d %H:%M:%S'))) - time.timezone
        #todo check if todays date works
        url = 'http://www.google.com/finance/historical?q=NASDAQ%3A' + symbol + '&output=csv'
        #url = 'https://query1.finance.yahoo.com/v7/finance/download/' \
        #      + symbol + '?period1=-5364633600000&period2=' + todays_date +'&interval=1&events=history&crumb=4XcUYPDyyJE'
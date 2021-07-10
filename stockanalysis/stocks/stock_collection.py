"""
###################
stock_collection.py
###################

Holds a collection of stocks can be considered similar to a portfolio
"""
# uses epoch time for the date
import datetime
import logging
import os

# import time
from datetime import timedelta

from .stock_day import StockDay

logger = logging.getLogger(__name__)

CSV = ".csv"
TIMEZONE = "TIMEZONE"
STOCKS_DIR = "stocks"


class StockCollection(object):
    def __init__(self):
        self.stocks = {}

    def __datetime_to_str(self, date):
        return str(date.strftime("%m/%d/%Y"))

    def __safe_open_w(self, path, file):
        """

        :param file:
        :return:
        """
        import os.path

        if os.path.exists(path):
            logger.info(path + " directory exists")
            pass
        else:
            logger.info("making " + path + " directory")
            try:
                os.makedirs(path)
            except OSError as e:
                logger.error(e.errno, e.winerror)
                raise
        return open(
            os.path.join(path, file), "wb+"
        )  # todo check that it's the right condition for opening

    def __extract_day_data(self, day_data, start=0, data={}):
        """
        :param day_data: the data wanted to be extracted
        :param start: the day currently extracting from 0 to N
        :param data: the unix time (epoch time) the function
            has already extracted and has kept for memory
        :return:
        """
        if day_data[0][0] == "a":
            # getting the month day and year -> mm/dd/year
            day = datetime.datetime.fromtimestamp(int(day_data[0][1:]))
            day_str = self.__datetime_to_str(day)
            data[day_str] = StockDay(
                day,
                float(day_data[1]),
                float(day_data[2]),
                float(day_data[3]),
                float(day_data[4]),
                int(day_data[5]),
            )
            return day
        else:
            new_day = start + timedelta(days=int(day_data[0]))
            new_day_str = self.__datetime_to_str(new_day)
            data[new_day_str] = StockDay(
                new_day,
                float(day_data[1]),
                float(day_data[2]),
                float(day_data[3]),
                float(day_data[4]),
                int(day_data[5]),
            )
            return start

    def process_data(self, data, symbol):
        row_count = len(data)
        logger.info(row_count)
        start = 0
        collection = (
            {}
        )  # stock_history.StockHistory(symbol, os.join(STOCKS_DIR,symbol+CSV))
        for line in data:
            stock_day_data = line.split(",")
            if stock_day_data[0][0:8] != TIMEZONE:
                start = self.__extract_day_data(stock_day_data, start, collection)
        return collection

    def __download_stock(self, symbol):

        """
        :param symbol:

        q - symbol
        x - stock exchange symbol https://www.google.com/googlefinance/disclaimer/
        i - Interval size in seconds
        p - Period (number d | number Y) d: days ; Y: years
        f - data you want (
            d: timestamp/interval,
            c: close,
            v: volume,
            o: opening,
            h: high,
            l: low
        )
        """
        # todays_date = (
        #     int(time.mktime(time.strptime(time.time(), "%Y-%m-%d %H:%M:%S")))
        #     - time.timezone
        # )
        # from urllib.request import urlopen

        # todo remove this symbol
        # symbol = "AAPL"
        #################
        pass

    def download(self, **kwargs):
        """
        :param symbol:type string
        """
        symbol = kwargs.get("symbol")
        self.__download_stock(symbol)

    def __download_all(self):
        for stock in self.stocks:
            self.__download_stock(stock)

    def __load_stock(self, filename):
        # todo make sure the filename is only $STOCK_NAME.csv
        """
        :type filename: File
        """
        # symbol = filename.split(".")[0]
        # stock_path = os.path.join(STOCKS_DIR, filename)
        # todo create stock_history object
        # todo add the stock_history object to the dictionary
        # with the symbol name as key
        pass

    def load(self, **kwargs):
        """ """
        if os.path.exists(STOCKS_DIR):
            stock_files = os.listdir(STOCKS_DIR)
            for stock in stock_files:
                self.__load_stock(stock)

    def list(self):
        """

        :rtype: list
        """
        return self.stocks.keys()

    def refresh(self, **kwargs):
        self.__download_all()

    def max_day_increase(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_day_increase()

    def max_day_percent_increase(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_day_percent_increase()

    def max_day_decrease(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_day_decrease()

    def max_day_percent_decrease(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_day_percent_decrease()

    def max_month_increase(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_month_increase()

    def max_year_increase(self, **kwargs):
        symbol = kwargs.get("symbol")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.max_year_increase()

    def what_if(self, **kwargs):
        symbol = kwargs.get("symbol")
        date_invested = kwargs.get("date_invested")
        amount_invested = kwargs.get("amount_invested")
        symbol = symbol.upper()
        history = self.stocks[symbol]
        history.what_if(date_invested, amount_invested)

    def symb(self, sym):
        list_stocks = []
        for sys in sym:
            history = self.stocks[sys]
            dict_stocks = history.last_day()
            list_stocks.append(dict_stocks)
        return list_stocks

    def top3(self, **kwargs):
        self.stocks.keys()
        sym = self.stocks.keys()
        list1 = self.symb(sym)
        dict2 = list1[-1]
        list2 = sorted(dict2.keys())
        biggest = list2[-1]
        biggest2 = list2[-2]
        biggest3 = list2[-3]
        logger.info(
            "Top1 %s: %f Top2 %s: %f Top3 %s: %f"
            % (
                dict2[biggest],
                biggest,
                dict2[biggest2],
                biggest2,
                dict2[biggest3],
                biggest3,
            )
        )

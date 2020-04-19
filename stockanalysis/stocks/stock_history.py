"""
################
stock_history.py
################
"""
from .stock_day import StockDay

latest_day = {}


class StockHistory:
    def __init__(self, symbol, filename):
        self.symbol = symbol
        self.history = []
        self.month_history = {}
        self.date_history = {}
        self.__read_file(filename)

    def __str__(self):
        return "%s stock" % self.symbol

    def __read_file(self, filename):
        with open(filename, "r") as f:
            stock_lines = f.readlines()
            stock_lines = stock_lines[1:]

            for line in stock_lines:
                line = line.strip()
                values = line.split(",")
                print(values[0], values[1], values[2], values[3])
                day = StockDay(
                    values[0],
                    float(values[1]),
                    float(values[2]),
                    float(values[3]),
                    float(values[4]),
                    int(values[5]),
                )
                self.history.append(day)

    def max_day_increase(self):
        max_diff = 0.0
        max_day = None

        for day in self.history:
            diff = day.increase()
            if diff > max_diff:
                max_diff = diff
                max_day = day
        print(
            "%s: %s | open = %f | close= %f | diff = %f"
            % (self.symbol, max_day.date, max_day.open, max_day.close, max_diff)
        )

    def max_day_decrease(self):
        max_diff = 0.0
        max_day = None

        for day in self.history:
            diff = day.decrease()
            if diff > max_diff:
                max_diff = diff
                max_day = day
        print(
            "%s: %s open = %f close = %f diff = %f"
            % (self.symbol, max_day.date, max_day.open, max_day.close, max_diff)
        )

    def max_day_percent_increase(self):
        max_diff = 0.0
        max_day = None

        for day in self.history:
            diff = day.percent_increase()
            if diff > max_diff:
                max_diff = diff
                max_day = day
        print(
            "%s: %s open = %f close = %f percent diff = %f"
            % (self.symbol, max_day.date, max_day.open, max_day.close, max_diff)
        )

    def max_day_percent_decrease(self):
        max_diff = 0.0
        max_day = None

        for day in self.history:
            diff = day.percent_decrease()
            if diff > max_diff:
                max_diff = diff
                max_day = day
        print(
            "%s: %s open = %f close = %f percent diff = %f"
            % (self.symbol, max_day.date, max_day.open, max_day.close, max_diff)
        )

    def get_months(self):
        month_dict = {}
        for day in self.history:
            month_dict[day.date[0:7]] = 1
        return month_dict.keys()

    def get_days_in_month(self, month):
        days = []
        for day in self.history:
            if month == day.date[0:7]:
                days.append(day)
        return days

    def max_month_increase(self):
        max_diff = 0.0
        max_month = None
        months = self.get_months()

        for month in months:
            days = self.get_days_in_month(month)
            last_day = days[0].close
            first_day = days[-1].close
            diff = last_day - first_day
            if diff > max_diff:
                max_diff = diff
                max_month = month
        print("%s: %s diff = %f" % (self.symbol, max_month, max_diff))

    def get_years(self):
        year_dict = {}
        for day in self.history:
            year_dict[day.date[0:4]] = 1
        return year_dict.keys()

    def get_days_in_year(self, year):
        days = []
        for day in self.history:
            if year == day.date[0:4]:
                days.append(day)
        return days

    def max_year_increase(self):
        max_diff = 0.0
        max_year = None
        years = self.get_years()

        for year in years:
            days = self.get_days_in_year(year)
            last_day = days[0].close
            first_day = days[-1].close
            diff = last_day - first_day
            if diff > max_diff:
                max_diff = diff
                max_year = year
        print("%s: %s diff = %f" % (self.symbol, max_year, max_diff))

    def what_if(self, date_invested, amount_invested):
        current_date = date_invested
        current_num = amount_invested
        last = self.history[0]
        value = last.adj_close
        earned = None
        for day in self.history:
            if current_date == day.date[0:10]:
                earned = (value - day.adj_close) * float(current_num)
        # todo fix the prints
        print("<b>%s: earned = %f</b>" % (self.symbol, earned))

    def last_day(self):
        last = self.history[0]
        price = ((last.close - last.open) / last.open) * 100
        latest_day[price] = self.symbol
        return latest_day

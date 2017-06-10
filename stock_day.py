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

import os, os.path


def __safe_open_w(path, file):
    if os.path.exists(path):
        print(path + ' directory exists')
        pass
    else:
        print('making ' + path + ' directory')
        try:
            os.makedirs(path)
        except OSError as e:
            print(e.errno, e.winerror)
            raise
    return open(os.path.join(path,file), 'w+')

'''
extract_day_data
@:parameter day_data - the data wanted to be extracted
@:parameter day - the day currently extracting from 0 to N
@:days - the unix time (epoch time) the function has already extracted and has kept for memory
'''
def extract_day_data(day_data, day=0, days={}):
    #todo decide on the data structure to hold the days we might want our stock_history
    import datetime
    if (day_data[day][0] == 'a'):
        # getting the month day and year -> mm/dd/year
        indicator_day = datetime.datetime.fromtimestamp(int(day_data[0][1:])).strftime('%m/%d/%Y')

        if len(days) > 0:
            days.pop()
        days.append(indicator_day)
    else:
        days[-1]

def process_data(data):
    row_count = len(data)
    print(row_count)
    #print(data)
    for line in data:
        stock_day_data = line.split(',')
        extract_day_data(stock_day_data)



def main():
    from urllib.request import urlopen
    '''
    q - symbol
    x - stock exchange symbol https://www.google.com/googlefinance/disclaimer/
    i - Interval size in seconds
    p - Period (number d | number Y) d: days ; Y: years
    f - data you want (d: timestamp/interval, c: close, v: volume, o: opening, h: high, l: low)
    '''
    symbol = 'AAPL'
    url = 'https://www.google.com/finance/getprices?q=' + symbol + '&x=' + 'NASDAQ' + '&i=86400&p=40Y&f=d,c,h,l,o,v'
    with urlopen(url) as response:
        body = response.read()
        body_str = body.decode('utf-8').split('\n')
        #TODO process data
        process_data(body_str[7:len(body_str)-1])
        #filename = symbol + '.csv'
        #with __safe_open_w('stock', filename) as f:
        #    print('writing ' + f.name)
        #    f.write(data)
        #    f.close()

if __name__ == '__main__':
    main()

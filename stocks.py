import stock_collection

DOWNLOAD = "download"
LIST = "list"
MAX_DAY_INCREASE = "max_day_increase"
REFRESH = "refresh"
# todo add constants


def print_table(symbol, convtype):
    collection = stock_collection.StockCollection()
    collection.load()

    if convtype == 'list':
        collection.list()

    elif convtype == DOWNLOAD:
        collection.download()

    elif convtype == REFRESH:
        collection.refresh()

    elif convtype == MAX_DAY_INCREASE:
        collection.max_day_increase(symbol)

    elif convtype == 'max_day_decrease':
        collection.max_day_decrease(symbol)

    elif convtype == 'max_day_percent_increase':
        collection.max_day_percent_increase(symbol)

    elif convtype == 'max_day_percent_decrease':
        collection.max_day_percent_decrease(symbol)

    elif convtype == 'max_month_increase':
        collection.max_month_increase(symbol)

    elif convtype == 'max_year_increase':
        collection.max_year_increase(symbol)

    elif convtype == 'top3':
        collection.top3()

    else:
        print('Command not recognized: %s for stock: %s' % (convtype, symbol))


def print_a(symbol, date_invested, amount_invested, convtype):
    collection = stock_collection.StockCollection()
    collection.load()
    if convtype == 'what_if':
        collection.what_if(symbol, date_invested, amount_invested, convtype)
    else:
        print('Command not recognized: %s %s %s %s'
              % (symbol, date_invested, amount_invested, convtype))

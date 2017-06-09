from flask import Flask, render_template, json, request, url_for, redirect
from Conversions import Conversions
import stocks

__author__ = 'Carlos Aguilera'
__version__ = "1.0.0"

app = Flask('StockAnalysis')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    #process the post request
    print(request.form)
    '''
    __convtype = request.form['convtype']
    # date is year-month-day
    __day_invested = request.form['date_invested']
    if __day_invested == None:
        redirect('/', code=400)
    # trim the last decimals
    __amount_invested = request.form['amount_invested']
    if __amount_invested == None:
        redirect(url_for('main'), code=400)
    __stock = request.form['symbol']
    if __stock == None:
        redirect(url_for('main'), code=400)
    
    if __convtype == Conversions.WHAT_IF._value_:
        #call what if
        return 'Got What if' + __day_invested + __amount_invested + __stock
    elif __convtype == Conversions.DOWNLOAD._value_:
        print(url_for('result'))
        return 'hello!'
        #return redirect(url_for('result'), code=307)
    elif __convtype == Conversions.MAX_DAY_INCREASE._value_:
        return 'Got Max Day Increase'
    elif __convtype == Conversions.MAX_DAY_DECREASE._value_:
        return 'Got Max Day Decrease'
    elif __convtype == Conversions.MAX_MONTH_INCREASE._value_:
        return 'Got Max Month Increase'
    elif __convtype == Conversions.MAX_DAY_PERCENT_INCREASE:
        return 'Got Max Day Percent Increase'
    elif __convtype == Conversions.MAX_DAY_PERCENT_DECREASE:
        return 'Got max Day Percent Decrease'
    elif __convtype == Conversions.TOP3._value_:
        return 'Got Top 3'
    elif __convtype == Conversions.REFRESH._value_:
        return 'Got Refresh'
    else:
        return 'Got nothing'
    '''
    return 'HELLO WORLD!'

@app.route('/what_if', methods=['POST'])
def what_if(symbol, data_invested, amount_invested, convtype):
    return 'Calculating'


@app.route('/result', methods=['POST'])
def result(convtype):
    return 'result'

if __name__ == "__main__":
    print("starting server...")
    app.run()

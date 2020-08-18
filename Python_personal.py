import alpaca_trade_api as tradeapi
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
import pandas as pd

#authentication and connection details
APCA_API_KEY_ID = 'PKJR18ZFP621QZF53T7E'
APCA_API_SECRET_KEY = 'xc4EkoG8Xk2Us6v4et0btchMA2Ga9m6bkBNgSa/k'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

#instantiate REST API
api = tradeapi.REST(
    key_id=APCA_API_KEY_ID,
    secret_key=APCA_API_SECRET_KEY,
    base_url=APCA_API_BASE_URL
)

#obtain account information
account = api.get_account()

#get the candlestick chart
def candlestick(chart_ticker):
    df = api.get_barset(chart_ticker, 'day', limit=253).df[chart_ticker]
    quotes = zip(mdates.date2num(df.index.to_pydatetime()),
    df.open, df.high, df.low, df.close)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.xaxis_date()
    ax.autoscale_view()
    all_days = DayLocator()
    ax.xaxis.set_minor_locator(all_days)
    candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r')
    plt.show()
    return plt.show()


# Check our current balance vs. our balance at the last market close
    balance_change = float(account.equity) - float(account.last_equity)
    print("Today's portfolio balance change:{}").format(balance_change)

def submit(ticker, quantity, profit_limit, stop_limit):
    api.submit_order(
       symbol=ticker,
       side='buy',
       type='market',
       qty=str(quantity),
       time_in_force='day',
       order_class='bracket',
       take_profit=dict(
           limit_price=str(profit_limit),
       ),
       stop_loss=dict(
           stop_price=str(stop_limit),
           limit_price=str(stop_limit),
       )
    )

stock=input("Which stock ticker would you like to know the weekly change for?")

barset=api.get_barset(stock,"day",limit=5)
stock_bars=barset[stock]

week_open=stock_bars[0].o
week_close=stock_bars[-1].c
percent_change=((week_close-week_open)/week_open)*100
print(stock+" has moved {}% over the last 5 days".format(percent_change))

candlestick("TSLA")
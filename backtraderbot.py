import backtrader as bt
import backtrader.indicators as btind
import pandas as pd


class MovingAverageCrossStrategy(bt.Strategy):
    params = (
        ('fast_ma_period', 10),
        ('slow_ma_period', 30),
    )

    def __init__(self):
        self.fast_ma = btind.SimpleMovingAverage(self.data, period=self.params.fast_ma_period)
        self.slow_ma = btind.SimpleMovingAverage(self.data, period=self.params.slow_ma_period)
        self.crossover = btind.CrossOver(self.fast_ma, self.slow_ma)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()



def load_data():
    # Replace 'your_data.csv' with the path to your historical price data file.
    data = pd.read_csv('bitcoin_historical_data.csv', index_col='time', parse_dates=True)
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    return bt.feeds.PandasData(dataname=data)

data = load_data()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.adddata(data)
    cerebro.addstrategy(MovingAverageCrossStrategy)

    cerebro.broker.set_cash(10000)  # Set initial cash amount

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

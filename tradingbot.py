import ccxt
import time

# Replace 'YOUR_BINANCE_API_KEY' and 'YOUR_BINANCE_SECRET_KEY' with your actual Binance API credentials.
exchange = ccxt.binance({
    'apiKey': 'YOUR_BINANCE_API_KEY',
    'secret': 'YOUR_BINANCE_SECRET_KEY',
})


def straddle_trade(pair, amount, stop_loss, take_profit):
    # Place a buy order
    buy_order = exchange.create_market_buy_order(pair, amount)
    print("Buy order placed:", buy_order)

    # Place a sell order
    sell_order = exchange.create_market_sell_order(pair, amount)
    print("Sell order placed:", sell_order)

    # Wait for the orders to be filled
    time.sleep(5)

    # Check if the buy order was filled
    buy_order = exchange.fetch_order(buy_order['id'])
    if buy_order['status'] == 'closed':
        print("Buy order filled.")
    else:
        print("Buy order not filled. Cancelling sell order.")
        exchange.cancel_order(sell_order['id'])
        return

    # Check if the sell order was filled
    sell_order = exchange.fetch_order(sell_order['id'])
    if sell_order['status'] == 'closed':
        print("Sell order filled.")
    else:
        print("Sell order not filled. Cancelling buy order.")
        exchange.cancel_order(buy_order['id'])
        return

    # Calculate profit/loss
    pnl = (take_profit - stop_loss) * amount
    print(f"Profit/Loss: {pnl:.2f} {pair.split('/')[1]}")

if __name__ == "__main__":
    pair = 'EUR/USDT'
    amount = 100  # The amount of EUR to trade
    stop_loss = 0.005  # 50 pips (assuming EUR/USD price is in decimals, not pips)
    take_profit = 0.01  # 100 pips (assuming EUR/USD price is in decimals, not pips)

    straddle_trade(pair, amount, stop_loss, take_profit)

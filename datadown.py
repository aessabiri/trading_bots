import requests
import pandas as pd

def get_historical_data(symbol, currency, limit, aggregate):
    base_url = "https://min-api.cryptocompare.com/data/v2/histohour"
    params = {
        "fsym": symbol,       # Cryptocurrency symbol (e.g., BTC for Bitcoin)
        "tsym": currency,     # Currency symbol (e.g., USD)
        "limit": limit,       # Number of data points to retrieve
        "aggregate": aggregate,  # Data aggregation interval (in days)
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()["Data"]["Data"]
    
    df = pd.DataFrame(data)
    df["time"] = pd.to_datetime(df["time"], unit="s")  # Convert Unix timestamp to datetime
    
    return df

if __name__ == "__main__":
    symbol = "BTC"         # Bitcoin symbol
    currency = "USD"       # Currency symbol (e.g., USD)
    limit = 2000           # Number of data points to retrieve
    aggregate = 1          # Data aggregation interval in days
    
    historical_data = get_historical_data(symbol, currency, limit, aggregate)
    print(historical_data)

      # Save the historical data to a CSV file
    csv_filename = "BTC_historical_datah.csv"  # Name of the CSV file
    historical_data.to_csv(csv_filename, index=False)
    
    print(f"Bitcoin historical data saved to {csv_filename}")

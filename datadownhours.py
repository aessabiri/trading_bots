import requests
import pandas as pd

def get_historical_data(symbol, currency, batch_size, aggregate, start_time):
    base_url = "https://min-api.cryptocompare.com/data/v2/histohour"
    params = {
        "fsym": symbol,
        "tsym": currency,
        "limit": batch_size,
        "aggregate": aggregate,
    }
    
    if start_time:
        params["toTs"] = start_time
    
    response = requests.get(base_url, params=params)
    data = response.json()["Data"]["Data"]
    
    df = pd.DataFrame(data)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    
    return df

if __name__ == "__main__":
    symbol = "BTC"
    currency = "USD"
    total_data_points = 10000  # Total number of data points to download
    batch_size = 2000  # Batch size for each request
    aggregate = 1
    
    all_data = []  # List to store all retrieved data
    
    for batch_num in range(total_data_points // batch_size):
        start_time = None if batch_num == 0 else all_data[-1]["time"].iloc[-1].timestamp()
        batch_data = get_historical_data(symbol, currency, batch_size, aggregate, start_time)
        all_data.extend(batch_data)
        print(f"Batch {batch_num + 1} downloaded")
    
    # Trim excess data points if the total_data_points limit is exceeded
    all_data = all_data[:total_data_points]
    
    historical_data = pd.DataFrame(all_data)
    
    csv_filename = "BTC_historical_data_hourly_10000_unique2.csv"
    historical_data.to_csv(csv_filename, index=False)
    
    print

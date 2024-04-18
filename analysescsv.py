import pandas as pd

def analyze_data(csv_filename):
    # Load the historical data from the CSV file
    data = pd.read_csv(csv_filename, parse_dates=['time'])
    
    # Calculate daily price change
    data['price_change'] = data['close'].diff()
    
    # Calculate average daily price change
    average_price_change = data['price_change'].mean()
    
    return data, average_price_change

if __name__ == "__main__":
    csv_filename = "BTC_historical_data.csv"  # Name of the CSV file
    
    # Analyze the data
    analyzed_data, avg_price_change = analyze_data(csv_filename)
    
    # Display the first few rows of the analyzed data
    print(analyzed_data.head())
    
    # Display the average daily price change
    print(f"Average daily price change: {avg_price_change:.2f}")

import requests
import pandas as pd

# Replace with your Alpha Vantage API key
API_KEY = "1VSD2L3BCXRBY2UO"
BASE_URL = "https://www.alphavantage.co/query"

# Set API parameters
params = {
    "function": "TIME_SERIES_MONTHLY",
    "symbol": "AAPL",
    "apikey": API_KEY
}

# Make GET request
response = requests.get(BASE_URL, params=params)
data = response.json()

# Extract time series data
time_series = data.get("Monthly Time Series", {})

# Convert to Pandas DataFrame
df = pd.DataFrame.from_dict(time_series, orient="index", dtype=float)

# Rename columns for clarity
df.columns = ["Open", "High", "Low", "Close", "Volume"]

# Convert index to datetime and sort
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Print the latest 12 months
print(df.tail(12))
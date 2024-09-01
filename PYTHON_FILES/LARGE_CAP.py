import yfinance as yf
import pandas as pd

# List of large-cap companies (problematic tickers removed)
large_cap_tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS',
                     'ICICIBANK.NS', 'HINDUNILVR.NS', 'HDFC.NS', 'BHARTIARTL.NS',
                     'KOTAKBANK.NS', 'LT.NS', 'ITC.NS', 'SBIN.NS', 'ASIANPAINT.NS',
                     'BAJFINANCE.NS', 'DMART.NS']

# Initialize an empty list to store the data
large_cap_data = []

for ticker in large_cap_tickers:
    # Fetch data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d", interval="5m")

    # Get additional information
    info = stock.info
    market_cap = info.get('marketCap', None)
    pe_ratio = info.get('trailingPE', None)
    industry_pe = info.get('industryPE', None)
    debt_to_equity = info.get('debtToEquity', None)
    dividend_yield = info.get('dividendYield', None)
    roe = info.get('returnOnEquity', None) if 'returnOnEquity' in info else None

    # Append data for each time interval
    for time, row in hist.iterrows():
        large_cap_data.append({
            'Timestamp': time,
            'Stock Name': ticker,
            'Open': row['Open'],
            'High': row['High'],
            'Low': row['Low'],
            'Close': row['Close'],
            'Volume': row['Volume'],
            'Market Cap': market_cap,
            'PE Ratio': pe_ratio,
            'Industry PE': industry_pe,
            'Debt to Equity': debt_to_equity,
            'Dividend Yield': dividend_yield,
            'ROE': roe
        })

# Convert the list to a DataFrame
large_cap_df = pd.DataFrame(large_cap_data)

# Save to CSV
large_cap_df.to_csv("/home/sushantswarup00/ETL_PROJECT/SOURCE_FILES/large_cap_companies_Minutes_data.csv", index=False)

print("Large-cap companies CSV file created successfully.")

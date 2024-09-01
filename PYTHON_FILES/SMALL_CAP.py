import yfinance as yf
import pandas as pd

# List of small-cap companies (problematic tickers removed)
small_cap_tickers = ['RADICO.NS', 'BIRLACORPN.NS', 'VSTIND.NS', 'TATAELXSI.NS',
                     'SIS.NS', 'EIHOTEL.NS', 'GRANULES.NS', 'TATAMETALI.NS',
                     'INDIAMART.NS', 'CERA.NS', 'FINPIPE.NS', 'JUBLPHARMA.NS',
                     'TATAINVEST.NS', 'BLUEDART.NS', 'GNFC.NS']

# Initialize an empty list to store the data
small_cap_data = []

for ticker in small_cap_tickers:
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
        small_cap_data.append({
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
small_cap_df = pd.DataFrame(small_cap_data)

# Save to CSV
small_cap_df.to_csv("/home/sushantswarup00/ETL_PROJECT/SOURCE_FILES/small_cap_companies_Minutes_data.csv", index=False)

print("Small-cap companies CSV file created successfully.")

"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        #read CSV files for each symbol
        file = symbol_to_path(symbol)
        dfsymbol = pd.read_csv(symbol_to_path(symbol),index_col="Date",
                                parse_dates = True,
                                usecols=['Date','Adj Close'], 
                                na_values=['nan'])
        #rename column name'Adj Close' to symbol name to prevent clash 
        dfsymbol = dfsymbol.rename(columns = {'Adj Close':symbol})
        #join the two dataframes 
        df = df.join(dfsymbol)
		
		#drop dates SPY did not trade
		if symbol == 'SPY':
			df = df.dropna(subset=['SPY'])

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-01-26')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    print df


if __name__ == "__main__":
    test_run()

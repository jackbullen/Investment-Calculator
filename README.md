# Investment-Calculator
An investment calculator.

Download the app and run: python3 ./main.py

Modify the investor variable in main.py, save, and re-run.

The strategy gives the percentage of investment amount going towards each stock.
Examples:
- 'strategy': {"NASDAQ:AAPL":0, "NASDAQ:GOOG":0, "NASDAQ:MSFT":0, "NASDAQ:TSLA":0, "NYSE:GM":1, -"NYSE:F":0, "TSE:TD":0, "TSE:BNS":0, "TSE:RY":0}
- 'strategy': {"NASDAQ:AAPL":0.3, "NASDAQ:GOOG":0.3, "NASDAQ:MSFT":0.4, "NASDAQ:TSLA":0, "NYSE:GM":1, "NYSE:F":0, "TSE:TD":0, "TSE:BNS":0, "TSE:RY":0}
- 'strategy': {"NASDAQ:AAPL":0, "NASDAQ:GOOG":0, "NASDAQ:MSFT":0, "NASDAQ:TSLA":0.3, "NYSE:GM":0.3, "NYSE:F":0.4, "TSE:TD":0, "TSE:BNS":0, "TSE:RY":0}
- 'strategy': {"NASDAQ:AAPL":0, "NASDAQ:GOOG":0, "NASDAQ:MSFT":0, "NASDAQ:TSLA":0, "NYSE:GM":0, "NYSE:F":0, "TSE:TD":0.3, "TSE:BNS":0.3, "TSE:RY":0.4}

## How it works
Securities data is fetched from Google Finance and saved into speadsheet using the apps script file dataGeneration. The data is downloaded in csv format and used to create investment projections.

## Data used
Closing price of NASDAQ:AAPL, NASDAQ:GOOG, NASDAQ:MSFT, NASDAQ:TSLA, NYSE:GM, NYSE:F, TSE:TD, TSE:BNS, TSE:RY from 2014 to 2023.

## To do
- Short-term: Verify it's making the correct calculations.
- Long-term: Link with a database and create a command-line interface to track investments in real-time.

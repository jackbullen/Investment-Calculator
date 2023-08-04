import warnings
warnings.filterwarnings("ignore")


import pandas as pd
import numpy as np
import math
import datetime as dt
from Account import Account

TICKERS = ["DATE", "NASDAQ:AAPL", "NASDAQ:GOOG", "NASDAQ:MSFT", "NASDAQ:TSLA", "NYSE:GM", "NYSE:F", "TSE:TD", "TSE:BNS", "TSE:RY"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

df = pd.read_csv("./stock_data.csv")
df = df[TICKERS]

stock_prices = df.dropna()

stock_prices['DATE'] = pd.to_datetime(stock_prices["DATE"])

def simulate_investment(acc, date, index):
    # Calculate the investment amounts for each stock based on the strategy
    for ticker, allocation in acc.strategy.items():
        stock_price = stock_prices[ticker][index]
        investment_amount = acc.monthly_investment * allocation
        acc.investments[ticker] += investment_amount/stock_price
        acc.balance -= investment_amount  # Deduct the investment amount from the balance
        
    acc.total_invested += acc.monthly_investment

def simulate_history(profile):
    initial_balance = profile["initial_balance"]
    monthly_income = profile["monthly_income"]
    monthly_expenses = profile["monthly_expenses"]
    monthly_investment = profile["monthly_investment"]
    strategy = profile["strategy"]
    investments = profile["investments"]
    dates = stock_prices['DATE']

    acc = Account(monthly_income, monthly_expenses, monthly_investment, strategy, initial_balance, investments)

    for i, date in enumerate(dates):
        if date.day == 1:
            #First day of month
            acc.balance += monthly_income - monthly_expenses
            simulate_investment(acc,date, i)

    total_investment_gains = 0
    for ticker, data in acc.investments.items():
        current_price = stock_prices[ticker][stock_prices.shape[0]-1]  # You should get the current price from an external source (e.g., API)
        total_investment_gains += current_price * acc.investments[ticker]

    return acc.total_invested, total_investment_gains, acc.balance

investor = {
    'initial_balance': 1000,
    'monthly_income': 4500,
    'monthly_expenses': 3800,
    'monthly_investment': 600,
    'investments': {"NASDAQ:AAPL":0, "NASDAQ:GOOG":0, "NASDAQ:MSFT":0, "NASDAQ:TSLA":0, "NYSE:GM":0, "NYSE:F":0, "TSE:TD":0, "TSE:BNS":0, "TSE:RY":0},
    'strategy': {"NASDAQ:AAPL":0.1, "NASDAQ:GOOG":0.1, "NASDAQ:MSFT":0.1, "NASDAQ:TSLA":0.3, "NYSE:GM":0, "NYSE:F":0, "TSE:TD":0, "TSE:BNS":0.2, "TSE:RY":0.2}
}   

total_invested, total_investment_gains, final_balance = simulate_history(investor)

print("Total Invested Amount: %0d$"%(total_invested))
print("Total Investment Gains: %0d$"%(total_investment_gains))
print("Final Balance: %0d$"%(final_balance))
print("Final Portfolio Value: %0d$"%(total_investment_gains+final_balance))

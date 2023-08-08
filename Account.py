import csv

class Account:
    def __init__(self, monthly_income, monthly_expenses, monthly_investment, strategy, initial_balance, investments):
        self.balance = initial_balance
        self.investments = investments
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.monthly_investment = monthly_investment
        self.strategy = strategy
        self.total_invested = 0
        self.total_saved = 0

# Move some of the code from main.py to here as class methods


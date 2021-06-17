# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """Reads portfolio into list of dictionaries"""
    portfolio_shares = []  # Initial portfolio state

    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        next(portfolio)  # Skip headings
        for line in portfolio:
            try:
                portfolio_shares.append({
                    'name': line[0],
                    'shares': int(line[1]),
                    'price': float(line[2])
                })
            except ValueError:
                print('Bad file format, this line will be skipped')
    return portfolio_shares


def read_prices(filename):
    """Reads stock prices from file"""
    stocks = {}  # Initial stocks state

    with open(filename, 'rt') as file:
        prices = csv.reader(file)
        next(prices)  # Skip headings
        for line in prices:
            try:
                stocks[str(line[0])] = float(line[1])
            except (ValueError, IndexError):
                print('Bad file format, this line will be skipped')
    return stocks


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculate current cost of portfolio
current_price = 0.0
for share in portfolio:
    current_price += share['shares'] * share['price']

# Calculate portfolio value
current_value = 0.0
for share in portfolio:
    current_value += share['shares'] * prices.get(share['name'], 0)

print('Current value', current_value)
print('Gain', current_value - current_price)
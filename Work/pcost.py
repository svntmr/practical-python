# pcost.py
#
# Exercise 1.27
from report import read_portfolio
import sys


def portfolio_cost(filename: str) -> float:
    """Calculates the total cost of portfolio"""
    total_cost = 0.0  # Total portfolio cost in dollars

    portfolio = read_portfolio(filename)
    for line, row in enumerate(portfolio):
        try:
            nshares = row.get('shares', 0)
            price = row.get('price', 0)
            total_cost += nshares * price
        except ValueError:
            print(f'Row {line}: Bad line: {row}')
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)


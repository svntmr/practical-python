# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    """Calculates the total cost of portfolio"""
    total_cost = 0.0  # Total portfolio cost in dollars

    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        next(portfolio)  # Skip headings
        for row, line in enumerate(portfolio):
            try:
                share_amount, share_price = line[1:]
                total_cost += float(share_amount) * float(share_price)
            except ValueError:
                print(f'Row {row}: Bad line: {line}')
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)


#! /usr/bin/env python3
# pcost.py
#
# Exercise 1.27
from report import read_portfolio


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


def main(argv: list):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)


if __name__ == '__main__':
    import sys
    main(sys.argv)


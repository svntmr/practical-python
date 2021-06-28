#! /usr/bin/env python3
# pcost.py
#
# Exercise 1.27
from report import read_portfolio


def portfolio_cost(filename: str) -> float:
    """Calculates the total cost of portfolio"""
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


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

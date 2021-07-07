#! /usr/bin/env python3
# report.py
#
# Exercise 2.4
from .fileparse import parse_csv
from .portfolio import Portfolio
from .tableformat import create_formatter, TableFormatter


def read_portfolio(filename: str, **opts) -> Portfolio:
    """Reads portfolio into Portfolio class instance"""
    with open(filename, 'r') as portfolio_lines:
        return Portfolio.from_csv(portfolio_lines)


def read_prices(filename: str) -> dict:
    """Reads stock prices from file"""
    with open(filename, 'r') as price_lines:
        return dict(parse_csv(price_lines, types=[str, float], has_headers=False))


def make_report(shares: list, share_prices: dict):
    """Saves info about shares into list of tuples"""
    report = []
    for share in shares:
        report.append((share.name, share.shares, current := share_prices.get(share.name, 0),
                       current - share.price))
    return report


def print_report(report, formatter: TableFormatter):
    """Prints the report with nice formatting"""
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        price = '${:.2f}'.format(price)  # Pre-format to add dollar sign
        data = [name, str(shares), f'{price}', f'{change:0.2f}']
        formatter.row(data)


def portfolio_report(portfolio_file: str = 'Data/portfolio.csv', prices_file: str = 'Data/prices.csv',
                     formatter: str = 'txt'):
    """Collects data about given portfolio and prices, makes small report"""
    portfolio = read_portfolio(portfolio_file)
    with open(prices_file, 'r') as report_lines:
        prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    tableformatter = create_formatter(formatter)
    print_report(report, tableformatter)


def main(argv: list):
    portfolio_file = argv[1]
    prices_file = argv[2]
    formatter = argv[3]
    portfolio_report(portfolio_file=portfolio_file, prices_file=prices_file, formatter=formatter)


if __name__ == '__main__':
    import sys

    main(sys.argv)

#! /usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename: str) -> list:
    """Reads portfolio into list of dictionaries"""
    with open(filename, 'r') as portfolio_lines:
        return parse_csv(portfolio_lines, types=[str, int, float])


def read_prices(filename: str) -> dict:
    """Reads stock prices from file"""
    with open(filename, 'r') as price_lines:
        return dict(parse_csv(price_lines, types=[str, float], has_headers=False))


def make_report(shares: list, share_prices: dict):
    """Saves info about shares into list of tuples"""
    report = []
    for share in shares:
        report.append((share['name'], share['shares'], current := share_prices.get(share['name'], 0),
                       current - share['price']))
    return report


def print_report(report):
    """Prints the report with nice formatting"""
    headers = ('Name', 'Shares', 'Price', 'Change')
    base_separation = '-' * 10
    separator = (base_separation,) * len(headers)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*separator))
    for name, shares, price, change in report:
        price = '${:.2f}'.format(price)  # Pre-format to add dollar sign
        print(f'{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}')


def portfolio_report(portfolio_file: str = 'Data/portfolio.csv', prices_file: str = 'Data/prices.csv'):
    """Collects data about given portfolio and prices, makes small report"""
    portfolio = read_portfolio(portfolio_file)
    with open(prices_file, 'r') as report_lines:
        prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv: list):
    portfolio_file = argv[1]
    prices_file = argv[2]
    portfolio_report(portfolio_file=portfolio_file, prices_file=prices_file)


if __name__ == '__main__':
    import sys
    main(sys.argv)

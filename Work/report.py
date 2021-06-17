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


def make_report(shares: list, share_prices: dict):
    """Saves info about shares into list of tuples"""
    report = []
    for share in shares:
        report.append((share['name'], share['shares'], current := share_prices.get(share['name'], 0),
                       current - share['price']))
    return report


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    base_separation = '-' * 10
    separator = (base_separation,) * len(headers)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*separator))
    for name, shares, price, change in report:
        price = '${:.2f}'.format(price)  # Pre-format to add dollar sign
        print(f'{name:>10s} {shares:>10d} {price:>10} {change:>10.2f}')

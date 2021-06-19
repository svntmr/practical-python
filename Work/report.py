# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    """Reads portfolio into list of dictionaries"""
    portfolio_shares = []  # Initial portfolio state

    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        headers = next(portfolio)
        for row, line in enumerate(portfolio):
            record = dict(zip(headers, line))
            try:
                portfolio_shares.append({
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                })
            except ValueError:
                print(f'Row {row}: Bad line: {line}')
    return portfolio_shares


def read_prices(filename):
    """Reads stock prices from file"""
    stocks = {}  # Initial stocks state

    with open(filename, 'rt') as file:
        prices = csv.reader(file)
        next(prices)  # Skip headings
        for row, line in enumerate(prices):
            try:
                stocks[str(line[0])] = float(line[1])
            except IndexError:
                pass
    return stocks


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
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    portfolio_report()

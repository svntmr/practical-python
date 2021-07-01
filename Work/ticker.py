from csv import reader

from follow import follow
from report import read_portfolio
from tableformat import create_formatter


def convert_types(lines, types):
    for line in lines:
        yield [func(val) for func, val in zip(types, line)]


def make_dicts(lines, headers):
    for line in lines:
        yield dict(zip(headers, line))


def select_columns(lines, indices):
    for line in lines:
        yield [line[index] for index in indices]


def filter_symbols(lines, names):
    for line in lines:
        if line['name'] in names:
            yield line


def ticker(portfolio_file, follow_file, formatter):
    formatter = create_formatter(formatter)
    portfolio = read_portfolio(portfolio_file)
    lines = follow(follow_file)
    lines = parse_stock_data(lines)
    lines = filter_symbols(lines, portfolio)
    formatter.headings(['Name', 'Price', 'Change'])
    for line in lines:
        formatter.row([line['name'], f"{line['price']:0.2f}", f"{line['change']:0.2f}"])


def parse_stock_data(lines):
    lines = reader(lines)
    lines = select_columns(lines, [0, 1, 4])
    lines = convert_types(lines, [str, float, float])
    lines = make_dicts(lines, ['name', 'price', 'change'])
    return lines


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    lines = parse_stock_data(lines)
    for line in lines:
        print(line)

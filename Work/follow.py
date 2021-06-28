import os
import time


def follow(filename: str = 'Data/stocklog.csv'):
    """Generator that reads the latest entries from the file"""
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)  # Sleep briefly and retry
            continue
        yield line


if __name__ == '__main__':
    from report import read_portfolio

    portfolio = read_portfolio('Data/portfolio.csv')

    for line in follow():
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

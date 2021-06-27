class TableFormatter:
    def headings(self, headers: list):
        """Emit the table headings."""
        raise NotImplementedError()

    def row(self, data: list):
        """Emit a single row of table data."""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers: list):
        """Emit a table in plain-text format"""
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, data: list):
        """Emit a single row of table data."""
        for d in data:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format."""

    def headings(self, headers: list):
        print(','.join(headers))

    def row(self, data: list):
        """Emit a single row of table data."""
        print(','.join(data))


class HTMLTableFormatter(TableFormatter):
    """Output portfolio data in HTML table format."""

    def headings(self, headers: list):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def row(self, data: list):
        """Emit a single row of table data."""
        print('<tr>', end='')
        for value in data:
            print(f'<td>{value}</td>', end='')
        print('</tr>')


def create_formatter(name: str) -> TableFormatter:
    """Creates specified table formatter"""
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
    return formatter

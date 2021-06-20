# fileparse.py
#
# Exercise 3.3
import csv
from typing import Optional


def parse_csv(filename: str, select: Optional[list] = None, types: Optional[list] = None, has_headers: bool = True,
              delimiter: str = ',', silence_errors=False) -> list:
    """Parse a CSV file into a list of records"""
    with open(filename) as f:
        if select and not has_headers:
            raise RuntimeError("select argument requires column headers")

        rows = csv.reader(f, delimiter=delimiter)

        records = []  # Container for file records

        if has_headers:
            # Read the file headers
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        for line, row in enumerate(rows):
            try:
                if not row:  # Skip rows with no data
                    continue
                # Type change if specified
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if has_headers:
                    # Filter the row if specific columns were selected
                    if indices:
                        row = [row[index] for index in indices]
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {line}:', e)

    return records

from fileparse import parse_csv
from stock import Stock


class Portfolio:
    def __init__(self):
        self._holdings = []

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self) -> float:
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares

    def append(self, holding: Stock):
        if not isinstance(holding, Stock):
            raise TypeError('Expected a stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = parse_csv(lines,
                              select=['name', 'shares', 'price'],
                              types=[str, int, float],
                              **opts)

        for d in portdicts:
            self.append(Stock(**d))

        return self

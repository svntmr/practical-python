class Stock:
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price:.2f})"

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        self._shares = value

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

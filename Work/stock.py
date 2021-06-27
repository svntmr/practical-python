class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price:.2f})"

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, shares: int):
        self.shares -= shares

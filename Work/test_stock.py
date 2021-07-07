import unittest

from stock import Stock

PRICE = 490.1
SHARES = 100
NAME = 'GOOG'


class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock(NAME, SHARES, PRICE)
        self.assertEqual(s.name, NAME)
        self.assertEqual(s.shares, SHARES)
        self.assertEqual(s.price, PRICE)

    def test_cost(self):
        s = Stock(NAME, SHARES, PRICE)
        self.assertEqual(s.cost, SHARES * PRICE)

    def test_sell(self):
        s = Stock(NAME, SHARES, PRICE)
        shares_to_sell = 25
        s.sell(shares_to_sell)
        self.assertEqual(s.shares, SHARES - shares_to_sell)

    def test_shares_attribute_allows_only_integers(self):
        s = Stock(NAME, SHARES, PRICE)
        with self.assertRaises(TypeError):
            s.shares = '100'


if __name__ == '__main__':
    unittest.main()

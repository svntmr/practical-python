# pcost.py
#
# Exercise 1.27
total_cost = 0.0  # Total portfolio cost in dollars

with open('Data/portfolio.csv', 'rt') as portfolio:
    next(portfolio)  # Skip headings
    for line in portfolio:
        share_amount, share_price = line.split(',')[1:]
        total_cost += float(share_amount) * float(share_price)
print(f'Total cost {total_cost}')

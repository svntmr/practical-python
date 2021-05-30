# mortgage.py
#
# Exercise 1.7
principal = 500000.0  # Mortgage size (dollars)
rate = 0.05  # Interest rate (percents)
payment = 2684.11  # Fixed monthly payment (dollars)
extra_payment = 1000.0  # Extra monthly payment (dollars)
extra_payment_start_month = 61  # When extra payments starts (month)
extra_payment_end_month = 108  # When extra payments ends (month)
total_paid = 0.0
months = 0

while principal > 0:
    months = months + 1
    monthly_payment = payment
    if extra_payment_start_month <= months <= extra_payment_end_month:
        monthly_payment = monthly_payment + extra_payment
    principal = principal * (1 + rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment

    if principal < 0:  # fix to not show negative principal
        principal = 0.0
    print(f'{months} month, {monthly_payment} monthly_payment, {round(principal, 2)} principal')

print(f'Total paid {round(total_paid, 2)}')
print(f'Months {months}')


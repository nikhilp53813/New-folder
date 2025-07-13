on_road_price = 1750000
down_payment = 50000
bank_interest = 10
P = total_loan = on_road_price-down_payment
r = interest_per_month = (bank_interest/12)/100
n = total_loan_months = 18
emi = (P*r*(1+r)**n) / ((1+r)**n-1)
print(emi) 
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_cnt = 0

while principal > 0:
    if month_cnt < 12:
        principal = principal * (1+rate/12) - (payment+1000)
        total_paid = total_paid + (payment+1000)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    month_cnt += 1


print('Total paid', round(total_paid, 1))
print('Month_cnt', month_cnt)
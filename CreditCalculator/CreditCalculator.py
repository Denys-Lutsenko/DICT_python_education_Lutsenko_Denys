'''ST1'''
loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

print(loan_principal, first_month, second_month,
      third_month, final_output, sep='\n')

'''ST2'''
from math import ceil

print('Enter the loan principal:')
principal = abs(int(input()))

print('''
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
''')
symbols = input()

if symbols == 'm':
    print('Enter the monthly payment:')
    monthly_pay = abs(int(input()))
    payment = ceil(principal / monthly_pay)
    if monthly_pay == principal:
        print(f'It will take {payment} month to repay the loan')
    else:
        print(f'It will take {payment} months to repay the loan')
elif symbols == 'p':
    print('Enter the number of months:')
    periods = abs(int(input()))
    payment = ceil(principal / periods)
    last_payment = principal - (periods - 1) * payment
    if principal % periods == 0:
        print(f'Your monthly payment = {payment}')
    else:
        print(f'Your monthly payment = {payment} and the last payment = {last_payment}.')


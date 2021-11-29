'''ST1'''
# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# print(loan_principal, first_month, second_month,
#       third_month, final_output, sep='\n')

'''ST2'''
# from math import ceil
#
# print('Enter the loan principal:')
# principal = abs(int(input()))
#
# print('''
# What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:
# ''')
# symbols = input()
#
# if symbols == 'm':
#     print('Enter the monthly payment:')
#     monthly_pay = abs(int(input()))
#     payment = ceil(principal / monthly_pay)
#     if monthly_pay == principal:
#         print(f'It will take {payment} month to repay the loan')
#     else:
#         print(f'It will take {payment} months to repay the loan')
# elif symbols == 'p':
#     print('Enter the number of months:')
#     periods = abs(int(input()))
#     payment = ceil(principal / periods)
#     last_payment = principal - (periods - 1) * payment
#     if principal % periods == 0:
#         print(f'Your monthly payment = {payment}')
#     else:
#         print(f'Your monthly payment = {payment} and the last payment = {last_payment}.')

'''ST3'''
import math

print('''
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')
symbols = input()

if symbols == 'n':
    print('Enter the loan principal:')
    principal = abs(int(input()))
    print('Enter the monthly payment:')
    monthly_pay = abs(int(input()))
    print('Enter the loan interest:')
    loan_interest = abs(float(input()))

    year_months = 12
    i = loan_interest / (year_months * 100)  # номинальная процентная ставка
    x = monthly_pay / (monthly_pay - i * principal)
    n = math.log(x, 1 + i)  # количество месяцев
    years = math.ceil(n) // year_months
    months = math.ceil(n) - years * year_months
    if years == 0 and months > 1:
        print(f'It will take {months} months to repay this loan!')
    elif years == 0 and months == 1:
        print(f'It will take {months} month to repay this loan!')
    else:
        if years > 1:
            print(f'It will take {years} years and {months} months to repay this loan!')
        else:
            print(f'It will take {years} year and {months} months to repay this loan!')
elif symbols == 'a':
    print('Enter the loan principal:')
    principal = abs(int(input()))
    print('Enter the number of periods:')
    periods = abs(int(input()))
    print('Enter the loan interest:')
    loan_interest = abs(float(input()))

    year_months = 12
    i = loan_interest / (year_months * 100)  # номинальная процентная ставка
    annuity = principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)

    print(f'Your monthly payment = {math.ceil(annuity)}!')
elif symbols == 'p':
    print('Enter the annuity payment:')
    annuity = abs(float(input()))
    print('Enter the number of periods:')
    periods = abs(int(input()))
    print('Enter the loan interest:')
    loan_interest = abs(float(input()))

    year_months = 12
    i = loan_interest / (year_months * 100)  # номинальная процентная ставка
    loan_principal = annuity / (i * math.pow(i + 1, periods) / (math.pow(i + 1, periods) - 1))

    print(f'Your loan principal = {math.floor(loan_principal)}!')
else:
    print('Oops! Please pay attention to correct input')



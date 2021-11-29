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
# import math
#
# print('''
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# ''')
# symbols = input()
#
# if symbols == 'n':
#     print('Enter the loan principal:')
#     principal = abs(int(input()))
#     print('Enter the monthly payment:')
#     monthly_pay = abs(int(input()))
#     print('Enter the loan interest:')
#     loan_interest = abs(float(input()))
#
#     year_months = 12
#     i = loan_interest / (year_months * 100)  # номинальная процентная ставка
#     x = monthly_pay / (monthly_pay - i * principal)
#     n = math.log(x, 1 + i)  # количество месяцев
#     years = math.ceil(n) // year_months
#     months = math.ceil(n) - years * year_months
#     if years == 0 and months > 1:
#         print(f'It will take {months} months to repay this loan!')
#     elif years == 0 and months == 1:
#         print(f'It will take {months} month to repay this loan!')
#     else:
#         if years > 1:
#             print(f'It will take {years} years and {months} months to repay this loan!')
#         else:
#             print(f'It will take {years} year and {months} months to repay this loan!')
# elif symbols == 'a':
#     print('Enter the loan principal:')
#     principal = abs(int(input()))
#     print('Enter the number of periods:')
#     periods = abs(int(input()))
#     print('Enter the loan interest:')
#     loan_interest = abs(float(input()))
#
#     year_months = 12
#     i = loan_interest / (year_months * 100)  # номинальная процентная ставка
#     annuity = principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)
#
#     print(f'Your monthly payment = {math.ceil(annuity)}!')
# elif symbols == 'p':
#     print('Enter the annuity payment:')
#     annuity = abs(float(input()))
#     print('Enter the number of periods:')
#     periods = abs(int(input()))
#     print('Enter the loan interest:')
#     loan_interest = abs(float(input()))
#
#     year_months = 12
#     i = loan_interest / (year_months * 100)  # номинальная процентная ставка
#     loan_principal = annuity / (i * math.pow(i + 1, periods) / (math.pow(i + 1, periods) - 1))
#
#     print(f'Your loan principal = {math.floor(loan_principal)}!')
# else:
#     print('Oops! Please pay attention to correct input')

'''ST4'''
import argparse
import math

parser = argparse.ArgumentParser(description="Calculation of differentiated and annuity payments")
parser.add_argument("--type", choices=["diff", "annuity"], help="You need to choose type of payments")
parser.add_argument("--payment", type=int, help="Input the monthly payment amount")
parser.add_argument("--principal", type=int, help="Input the loan principal")
parser.add_argument("--periods", type=int, help="Input the number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Input interest rate")

args = parser.parse_args()

# аннуитетный платеж
if args.type is not None and args.type not in "diff" and args.payment is not None \
        and args.principal is not None and args.interest is not None:
    # annuity payment's input: --payment, --principal, --interest
    if args.principal > 0 and args.payment > 0 and args.interest > 0:
        year_months = 12
        i = args.interest / (year_months * 100)  # номинальная процентная ставка
        x = args.payment / (args.payment - i * args.principal)
        n = math.log(x, 1 + i)  # количество месяцев
        years = math.ceil(n) // year_months
        months = math.ceil(n) - years * year_months
        overpayment = (args.payment * math.ceil(n)) - args.principal
        if years == 0 and months > 1:
            print(f'It will take {months} months to repay this loan!')
        elif years == 0 and months == 1:
            print(f'It will take {months} month to repay this loan!')
        else:
            if years > 1 and months == 0:
                print(f'It will take {years} years to repay this loan!')
            elif years == 1 and months == 0:
                print(f'It will take {years} year to repay this loan!')
            else:
                print(f'It will take {years} year and {months} months to repay this loan!')
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
elif args.type is not None and args.type not in "diff" and args.periods is not None \
        and args.principal is not None and args.interest is not None:
    # annuity payment's input: --principal, --periods, --interest
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        year_months = 12
        i = args.interest / (year_months * 100)  # номинальная процентная ставка
        annuity = args.principal * (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
        overpayment = math.ceil(annuity) * args.periods - args.principal
        print(f'Your annuity payment = {math.ceil(annuity)}!')
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
elif args.type is not None and args.type not in "diff" and args.periods is not None \
        and args.payment is not None and args.interest is not None:
    # annuity payment's input: --payment, --periods, --interest
    if args.payment > 0 and args.periods > 0 and args.interest > 0:
        year_months = 12
        i = float(args.interest) / (year_months * 100)  # номинальная процентная ставка
        loan_principal = args.payment / (i * math.pow(i + 1, args.periods) / (math.pow(i + 1, args.periods) - 1))
        overpayment = (args.payment * args.periods) - loan_principal
        print(f'Your loan principal = {math.floor(loan_principal)}!')
        print(f"Overpayment = {math.ceil(overpayment)}")
    else:
        print("Incorrect parameters")
# дифференцированная оплата
elif args.type is not None and args.type not in "annuity" and args.principal is not None \
        and args.periods is not None and args.interest is not None:
    # differentiated payment's input: --principal, --periods, --interest
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        payment = 0
        for m in range(1, args.periods + 1, 1):
            year_months = 12
            i = args.interest / (year_months * 100)  # номинальная процентная ставка
            diff = args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods)
            payment += math.ceil(diff)
            print(f"Month {m}: payment is {math.ceil(diff)}")
        overpayment = payment - args.principal
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")


# Пример 1: расчет дифференцированных выплат
# python CreditCalculator.py --type=diff --principal=1000000 --periods=10 --interest=10
# Пример 2: расчет аннуитета для 60-месячной (5-летней) ссуды с основной суммой 1000000 под 10% годовых.
# python CreditCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Пример 3: указано менее четырех аргументов
# python CreditCalculator.py --type=diff --principal=1000000 --payment=104000
# Пример 4: рассчитать дифференцированные выплаты при основной сумме
# 500 000 в течение 8 месяцев и процентной ставке 7,8%
# python CreditCalculator.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Пример 5: рассчитать основную сумму для пользователя, платящего 8722 в месяц в течение 120 месяцев под 5,6% годовых.
# python CreditCalculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Пример 6: подсчитайте, сколько времени потребуется, чтобы погасить ссуду с основной суммой 500 000,
# ежемесячным платежом в размере 23 000 и процентной ставкой 7,8%
# python CreditCalculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8


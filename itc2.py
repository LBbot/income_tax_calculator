#!bin/env python3
# itc2.py - Input annual salary to calculate income tax across the 4 current tax bands. Displays tax and net pay,
# monthly and annual, in CSV format. This version can be run with an argument/parameter for fast raw output, or run on
# its own for a more user-friendly experience with guided prompts.

import sys
import csv

def value_check(user_input):
    try:
        user_input = float(user_input)
        user_input = int(user_input)  # Float-Int conversion included to allow float inputs.
    except (ValueError, OverflowError):
        print("Unable to recognise input: '{}' Please try again.".format(user_input))
        return False

    if 0 < user_input < 1000000:
        return user_input
    else:
        print("The amount must be between 0-999999. Please try again.")
        return False

if len(sys.argv) < 2:
    while True:
        annual_salary = input("Input annual salary between £0 and £999999 and press Enter:\n"
                              "(Note: pennies on input will be rounded to the nearest £. Calculations do not include "
                              "National Insurance payments OR Personal Allowance reduction - incurred for every £2 over"
                              " £100,000 adjusted net income.) \n£")
        annual_salary = value_check(annual_salary)
        if annual_salary:
            break
else:
    annual_salary = value_check(sys.argv[1])
    if not annual_salary:
        sys.exit()


annual_salary_pennies = annual_salary * 100
tax_paid = 0

additional_rate = 15000000  # 45%
additional_rate_percentage = 45
higher_rate = 4500000  # 40%
higher_rate_percentage = 40
basic_rate = 1150000  # 20%
basic_rate_percentage = 20

# TODO write a function to calculate this without repeating lines.
if annual_salary_pennies > additional_rate:
    over_cap = annual_salary_pennies - additional_rate
    tax_paid += (over_cap * additional_rate_percentage) // 100
    tax_paid += ((additional_rate - higher_rate) * higher_rate_percentage // 100)
    tax_paid += ((higher_rate - basic_rate) * basic_rate_percentage // 100)

elif annual_salary_pennies > higher_rate:
    over_cap = annual_salary_pennies - higher_rate
    tax_paid += (over_cap * higher_rate_percentage) // 100
    tax_paid += ((higher_rate - basic_rate) * basic_rate_percentage // 100)

elif annual_salary_pennies > basic_rate:
    over_cap = annual_salary_pennies - basic_rate
    tax_paid += (over_cap * basic_rate_percentage) // 100

net_pay = annual_salary_pennies - tax_paid

itc_writer = csv.writer(sys.stdout)
itc_writer.writerow(["Monthly tax (£)", "Monthly take home pay (£)", "Annual tax (£)", "Annual take home pay (£)"])
itc_writer.writerow(["{:.2f}".format(tax_paid // 12 / 100),
                     "{:.2f}".format(net_pay // 12 / 100),
                     "{:.2f}".format(tax_paid / 100),
                     "{:.2f}".format(net_pay / 100)])

# More readable output option:
# print("Gross annual pay: £{:.2f}".format(annual_salary_pennies / 100))
# print("Tax paid monthly: £{:.2f}".format(tax_paid // 12 / 100))
# print("Tax paid annually: £{:.2f}".format(tax_paid / 100))
# print("Net monthly pay: £{:.2f}".format(net_pay // 12 / 100))
# print("Net annual pay: £{:.2f}".format(net_pay / 100))

#!bin/env python3
# income_tax_calculator.py - Input annual salary to calculate income tax across the 4 current tax bands. Displays tax
# and net pay - monthly and annual - in CSV format. Original user-friendly version with detailed prompt.

import sys
import csv

while True:
    annual_salary = input("Input annual salary between £0 and £999999 and press Enter:\n"
                          "(Note: pennies on input will be rounded to the nearest £. Calculations do not include "
                          "National Insurance payments OR Personal Allowance reduction - incurred for every £2 over "
                          "£100,000 adjusted net income.) \n£")
    try:
        annual_salary = float(annual_salary)
    except ValueError:
        print("Unable to recognise input: '{}' Please try again.".format(annual_salary))
        continue

    annual_salary = int(round(annual_salary))  # Float-Int conversion included to allow float inputs.
    if 0 < annual_salary < 1000000:
        break
    else:
        print("Amount outside of £0-999999 range. Please try again.")

annual_salary_pennies = annual_salary * 100
additional_rate = 15000000  # 45%
higher_rate = 4500000  # 40%
basic_rate = 1150000  # 20%
tax_paid = 0

if annual_salary_pennies > additional_rate:
    over_cap = annual_salary_pennies - additional_rate
    tax_paid += (over_cap * 45) // 100
    tax_paid += ((additional_rate - higher_rate) * 40 // 100)
    tax_paid += ((higher_rate - basic_rate) * 20 // 100)

elif annual_salary_pennies > higher_rate:
    over_cap = annual_salary_pennies - higher_rate
    tax_paid += (over_cap * 40) // 100
    tax_paid += ((higher_rate - basic_rate) * 20 // 100)

elif annual_salary_pennies > basic_rate:
    over_cap = annual_salary_pennies - basic_rate
    tax_paid += (over_cap * 20) // 100

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

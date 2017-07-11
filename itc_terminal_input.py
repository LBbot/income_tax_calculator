#!bin/env python3
# itc_terminal_input.py - Input annual salary via terminal to calculate income tax across the 4
# current tax bands. Displays tax and net pay - monthly and annual - in CSV format. 
# For clean presentation in Linux terminal enter the following (example input for £20,000): 
# python3 itc_terminal_input.py 20000 | column -t -s ,

import sys
import csv

try:
    if len(sys.argv) < 2:
        raise ValueError("No input supplied by command line.")
    annual_salary = float(sys.argv[1])
    annual_salary = int(round(annual_salary))
    if not 0 < annual_salary < 1000000:
        raise ValueError("Input outside of range.")
except ValueError as err:
    print(err, "Invalid. Did you try a number between 0-999999?")
    sys.exit()

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

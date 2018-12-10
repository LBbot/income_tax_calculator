#!bin/env python3
# itc2.py - Input annual salary to calculate income tax across the 4 current tax bands. Displays tax and net pay,
# monthly and annual, in CSV format. This version can be run with an argument/parameter for fast raw output, or run on
# its own for a more user-friendly experience with guided prompts.

import sys
import csv

# Function definitions
def value_check(user_input):
    try:
        user_input = float(user_input)
        user_input = int(user_input)  # Float-Int conversion included to allow float inputs.
    except (ValueError, OverflowError, NameError):
        print("Unable to recognise input: '{}' Please try again.".format(user_input))
        return False

    if 0 < user_input < 1000000:
        return user_input
    else:
        print("The amount must be between 0-999999. Please try again.")
        return False

def tax_maths(pennies, highest_rate_and_percentage):
    over_cap = pennies - highest_rate_and_percentage[0]
    bracket_tax = (over_cap * highest_rate_and_percentage[1]) // 100
    return bracket_tax


# Actual start of script
if len(sys.argv) < 2:
    while True:
        annual_salary = input(
            "Input annual salary between £0 and £999999 and press Enter:\n"
            "(Note: pennies on input will be rounded to the nearest £. Calculations do not include "
            "National Insurance payments OR Personal Allowance reduction - incurred for every £2 over"
            " £100,000 adjusted net income.) \n£"
        )
        annual_salary = value_check(annual_salary)
        if annual_salary:
            break
else:
    annual_salary = value_check(sys.argv[1])
    if not annual_salary:
        sys.exit()


# Set up variables for calculation
annual_salary_pennies = annual_salary * 100
tax_paid = 0
cap_and_percentage = False

# Rates
basic_rate = [1150000, 20]  # £11500 20%
higher_rate = [4500000, 40]  # £45000 40%
additional_rate = [15000000, 45] # £150000 45%

# Check rates from lowest to highest - if annual salary is higher, we update the cap_and_percentage variable
# (and add in any lower cap taxes - as they will be a fixed amount)
if annual_salary_pennies > basic_rate[0]:
    cap_and_percentage = basic_rate

if annual_salary_pennies > higher_rate[0]:
    tax_paid += ((higher_rate[0] - basic_rate[0]) * basic_rate[1] // 100)
    cap_and_percentage = higher_rate

if annual_salary_pennies > additional_rate[0]:
    tax_paid += ((additional_rate[0] - higher_rate[0]) * higher_rate[1] // 100)
    cap_and_percentage = additional_rate

# if the variable has been altered from false, we feed it into tax_maths function to scoop off the top and add the
# result to total tax
if cap_and_percentage:
    tax_paid += tax_maths(annual_salary_pennies, cap_and_percentage)

net_pay = annual_salary_pennies - tax_paid

# Write to CSV
itc_writer = csv.writer(sys.stdout)
itc_writer.writerow(["Monthly tax (£)", "Monthly take home pay (£)", "Annual tax (£)", "Annual take home pay (£)"])
itc_writer.writerow([
    "{:.2f}".format(tax_paid // 12 / 100),
    "{:.2f}".format(net_pay // 12 / 100),
    "{:.2f}".format(tax_paid / 100),
    "{:.2f}".format(net_pay / 100)
])

# for more readable output option UNCOMMENT THESE:
# print("Gross annual pay: £{:.2f}".format(annual_salary_pennies / 100))
# print("Tax paid monthly: £{:.2f}".format(tax_paid // 12 / 100))
# print("Tax paid annually: £{:.2f}".format(tax_paid / 100))
# print("Net monthly pay: £{:.2f}".format(net_pay // 12 / 100))
# print("Net annual pay: £{:.2f}".format(net_pay / 100))

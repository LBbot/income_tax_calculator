# income_tax_calculator
Python 3 script where you input annual salary in GBP to calculate income tax across the 4 current UK tax bands. Displays tax and net pay - monthly and annual - in CSV format. Does not include National Insurance payments OR Personal Allowance reduction (incurred for every £2 over £100,000 adjusted net income).

itc2.py - Can be run on its own as a user-friendly version, prompting user to enter annual salary with detailed explanation, or can be run with annual salary as an argument (enter an annual salary after the script name when running in the terminal) for immediate output.

These two options were previously the separate files:
income_tax_calculator.py - User-friendly version, opens prompting user to enter annual salary with detailed explanation.
itc_terminal_input.py - Faster alternative where annual salary is supplied as an argument after the script name when running it from the terminal. Calculations are the same. Displays CSV without any other print statements.

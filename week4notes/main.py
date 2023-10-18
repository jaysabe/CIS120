# Notes for week 4:

# if you have consts in global scope, you can alter it in different functions without errors
# there isn't really a const variable in python, meaning that they can change ex:

MAX_AGE = 130
#******************************************************************************
# Author:           Jay Abegglen
# Lab:              3
# Date:             10/09/2023
# Description:      This program takes in the names of food orders and their prices,
#                   calculates the total and suggested tip amounts, before printing them to
#                   the console. Then prompts user if they wish to calculate another receipt.
#
# Input:            item_name, item_price, restart
# Output:           displays receipt with suggested tip amounts
# Sources:          Lab 3 specifications
#                   Module 3
#******************************************************************************

import sys
# if you want to use this as a library -> sys.<nameoffunction>
# OR

import calc_rec

MAX_AGE = 130


def input_string(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Form must not be empty.")


def input_int_in_range(prompt, min_, max_):
    while True:
        value = input_int(prompt)
        if min_ <= value <= max_:
            return value
        print(f"Number must be between {min_} and {max_}.")


def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Error detected. Not a whole number.')



   
def display_results():
    print(f"The area of a rectangle with width of {width} and height of {height} = {area}")    
   
    

print(MAX_AGE)


def main():
    global MAX_AGE # refers to global value instead of taking the scoped version
    # MAX_AGE = 120
# it'll print 130
    print(MAX_AGE)
    
# if we run this at top level name = __main__
# if we want to exe as
'''
exe as a library:

exe as a script:

'''


# print("__name__:", __name__)

# ****************************************************************
if __name__==__main__:
    main()
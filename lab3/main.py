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
#
#
# def order_food():
#     total = 0.0
#
#     while True:
#         print("----------------------------------------------------------------\n")
#         item_name = input("Enter food order (type \'done\' when finished): ")
#         if item_name.lower() == 'done':
#             break
#         elif item_name.isdigit():
#             print_error()
#             continue
#
#         item_price = input(f"Enter the price for {item_name}: $")
#
#         # catch not valid prices
#         if not is_valid_price(item_price):
#             continue
#
#         # set price to float value and validate
#         price = is_valid_price(item_price)
#         if price is not None:
#             # accumulate total
#             total += price
#
#             # for testing TODO
#             # print("Current Total:", total)
#
#     tip_percentages = [10, 15, 20]
#
#     print_receipt(total, tip_percentages)
#
#
# def calculate_tip(total, tip_percentage):
#     return total * tip_percentage / 100.0
#
#
# def print_receipt(total, tip_percentages):
#     print("\n----- Receipt -----")
#     print(f"\nTotal: ${total:.2f}\nTip Suggestions:")
#     for tip_percentage in tip_percentages:
#         tip_amount = calculate_tip(total, tip_percentage)
#         print(f"{tip_percentage}%: ${tip_amount:.2f}")
#
#
# def is_valid_price(price):
#     if not price.replace('.', '', 1).isdigit():
#         print("Invalid input. Enter a numeric value for the price.")
#         return None
#
#     if float(price) < 0:
#         print("Price must be positive. Enter a valid amount.")
#         return None
#
#     return float(price)
#
#
# def print_error():
#     print("Invalid Selection. Please try again.\n")
#
#
# def welcome():
#     center = '\t\t\t '
#     prompt_start = '\n\n'
#     print("\n", center, "|| MEAL RECEIPT GENERATOR || ", prompt_start)
#
#
# def main():
#     welcome()
#     while True:
#         order_food()
#
#         restart = input("Would you like to run the program again? (yes/no): ").lower()
#         if restart != 'yes':
#             break
#
#

import sys

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


def get_dimensions():
    width = input_int_in_range("What is the width of the rectangle? ", 0, sys.maxsize)
    height = input_int_in_range("What is the height of the rectangle? ", 0, sys.maxsize)
    return width, height # this is the a tuple


def calc_rec():
    width, height = get_deminsions()
    area = calc_rec(width, height)
    display_results(width, height, area)

def main():
    age = input_int_in_range("How old are you? ", 1, MAX_AGE)
    print(f"You are {age}, next year you will be {age + 1}")
    teaching = input_int_in_range("How long have you been teaching? ", 0, MAX_AGE)
    print("Wow! That s a long time. ")
    name = input_string("What is your name? ")

# ****************************************************


if __name__ == '__main__':
    main()


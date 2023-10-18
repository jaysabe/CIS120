# ******************************************************************************
# Author:           Fidel Cervantes, Jay Abegglen
# Lab:              4
# Date:             10/17/2023
# Description:      This program mimics an ATM. It displays a menu to a user with options to
# withdrawal money, deposit, print balance and exit.
#
# Input:            choice, withdrawal, deposit
# Output:           balance
# Sources:          Lab 4 specifications
#                   Module 4
# ******************************************************************************

import out
from input import check_int_value


def main():
    out.print_menu()
    choice = 0
    balance = 1000

    while True:
        # call input func:
        choice = check_int_value("Enter option ")
        balance = out.choice(choice, balance)

        # set variable to input to either loop or exit
        if choice == 3:
            break

    out.print_title()
    out.print_balance(balance)


# **********************************
if __name__ == '__main__':
    main()

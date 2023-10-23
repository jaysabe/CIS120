# ******************************************************************************
# Author:           Jay Abegglen
# Lab:              5
# Date:             10/23/2023
# Description:      This program simulates a shopping cart for a family that is ordering smoothies for a party.
#                   The program allows you to add, edit, and remove smoothies,
#                   check the status, search, etc
#
# Input:            match statements, smoothies, attributes of the smoothies dictionary
# Output:
# Sources:          Lab 5 specifications
#                   Module 5 -- had to do on own due to traveling this week
# ******************************************************************************

import calc
from output import smoothie_menu


def main():
    print("Your Insta Smoothie Cart: \n")
    smoothie_menu()

    # Smoothie dictionary :
    smoothies = {
        "OJ Julius":
            {"price": 4, "fruit": "oranges-&-bananas", "base": "Orange Juice", "sweetener": "sugar"},
        "Blackberry Sabbath":
            {"price": 7, "fruit": "blackberries", "base": "Lemonade", "sweetener": "orange bitters"},
        "Mango Starr":
            {"price": 5, "fruit": "mango-pineapple", "base": "Peach Juice", "sweetener": "none"},
        "Strawberryl Streep":
            {"price": 11, "fruit": "strawberry-banana", "base": "Oatmilk", "sweetener": "honey"}
    }

    while True:
        match (input("Option: ").lower()):
            case "show":
                # call cart_stats
                calc.cart_stats()

            case "list":
                # call check_cart
                calc.check_cart(smoothies)

            case "add":
                # call mod_smoothie with add
                calc.mod_smoothie(smoothies, typeof="add")

            case "change":
                # call mod_smoothie with change
                calc.mod_smoothie(smoothies, typeof="change")

            case "checkout":
                break
            case _:
                print("Not a valid option. Please try again. \n")
        smoothie_menu()

    print("Thank you for stopping by! 🛒")






# *****************************************************
if __name__ == '__main__':
    main()

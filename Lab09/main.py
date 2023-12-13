# ******************************************************************************
# Author:           Jay Abegglen
# Lab:              9
# Date:             11/26/2023
# Description:      Using pygubu, a GUI pop up program takes in information from the US Census and then prints
# them in terms of their name, birth year, gender, and count.
# Input:            Input comes from Microsoft SQL server 'NAMES'
# Output:           Displays attributes from SQL Server
# Sources:          Lab 9 specifications
#
# ******************************************************************************
import util
from Name import Name


class App:
    @staticmethod
    def get_search_criteria():
        gender = util.chk_char(input("Please select a gender ('M' for male or 'F' for female)? "))
        year = util.validate_range(input("Which year (between 1915 and 2014) would you like to see? "), 1915, 2014)

        return year, gender

    @classmethod
    def search(cls):
        year, gender = cls.get_search_criteria()
        print(f"\n50 most popular names for {gender} babies in {year}:\n ")
        rows = Name.read_names(year, gender)

        # formatting
        print(f"{'Year':<6}{'Name':<20}{'Gender':<8}{'Count':<10}")
        for row in rows[:50]:
            print(f"{row.get_year():<6}{row.get_name():<20}{row.get_gender():<8}{row.get_name_count():<10}")

    @classmethod
    def run(cls):
        while True:
            print("Welcome to my Popularity Program! \n")
            cls.search()
            restart = input("Do you want to run the program again ('n' to quit)? ").lower()
            if restart == 'n':
                break
            else:
                print("Restarting program . . . \n")

        print("Thank you for stopping by! ")


if __name__ == '__main__':
    App.run()

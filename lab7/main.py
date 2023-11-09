# ******************************************************************************
# Author:           Jay Abegglen
# Lab:              7
# Date:             11/08/2023
# Description:      Program takes in information from the US Census and then prints
# them in terms of their name, birth year, gender, and count
# Input:            Input comes from Microsoft SQL server 'NAMES'
# Output:           Displays attributes from SQL Server
# Sources:          Lab 7 specifications
#
# ******************************************************************************
import util
from Name import Name


class App:
    @staticmethod
    def get_search_criteria():
        name = util.validate_str(input("What name would you like to search? "))
        year = util.validate_range(input("What year would you like to pick (must be between 1915 and 2014)? "), 1915,
                                   2014)
        gender = util.chk_char(input("Which gender ('M' for male or 'F' for female)?"))

        return name, year, gender

    @classmethod
    def search(cls, name, year, gender, name_count):
        name, year, gender = cls.get_search_criteria()
        names = Name.read_names(name, year, gender, name_count)
        for name in names:
            print(name.get_name(), name.get_year(), name.get_gender(), name.get_name_count())

    @classmethod
    def run(cls):
        while True:
            cls.search()
            restart = input("Do you want to run the program again ('n' to quit)? ").toLower()
            if restart == 'n':
                break


if __name__ == '__main__':
    App.run()

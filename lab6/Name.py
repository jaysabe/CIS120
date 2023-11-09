# defines Name class
from Database import Database


class Name:
    def __init__(self, name, year, gender, count):
        # name mangling:
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__count = count

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_gender(self):
        return self.__gender

    def get_count(self):
        return self.__count

    # Save setters for later
    # def set_name(self, name):
    #     self.__name = name
    #
    # def set_year(self, year):
    #     self.__year = year
    #
    # def set_gender(self, gender):
    #     self.__gender = gender
    #
    # def set_count(self, count):
    #     self.__count = count

    @staticmethod
    def read_names():
        # Call Data.read_names() and return Name objects
        names_data = Database.read_names()
        return [Name(**data) for data in names_data]

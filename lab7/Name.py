from Database import Database


class Name:
    name = ""
    year = ""
    gender = ''
    name_count = 0

    def __init__(self, name, year, gender, name_count):
        self.name = name
        self.year = year
        self.gender = gender
        self.name_count = name_count

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_gender(self):
        return self.gender

    def get_name_count(self):
        return self.name_count

    @staticmethod
    def read_names(name, year, gender, name_count):
        rows = Database.fetch_names(name, year, gender, name_count)
        return rows

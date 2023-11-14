from Database import Database


class Name:
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
    def read_names(year, gender):
        rows = Database.fetch_names(year, gender)
        return [Name(row[0], row[1], row[2], row[3]) for row in rows]

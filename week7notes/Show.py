from Database import Database


class Show:
    type = ""
    title = ""
    year = ""
    runtime = 0
    rating = 0
    num_votes = 0

    def __init__(self, type, title, year, runtime, rating, num_votes):
        self.type = type
        self.title = title
        self.year = year
        self.runtime = runtime
        self.rating = rating
        self.num_votes = num_votes

    def get_type(self):
        return self.type

    def get_title(self):
        return self.title

    def get_rating(self):
        return self.rating

    def get_num_votes(self):
        return self.num_votes

    @staticmethod
    def fetch_shows(year, type, num_votes):
        rows = Database.fetch_shows(year, type, num_votes)

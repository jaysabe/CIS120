from Show import Show


class AppUI:
    @staticmethod
    def get_search_criteria():
        year = input("What year do you want? ")
        type = input("What type of show do you want? ")
        num_votes = input("What is the minimum number of votes? ")

        return year, type, num_votes

    @classmethod
    def search(cls, year, type, num_votes):
        year, type, num_votes = cls.get_search_criteria()
        shows = Show.fetch_shows(year, type, num_votes)
        for show in shows:
            print(show.get_type(), show.get_title(), show.get_rating(), show.get_num_votes())

    @classmethod
    def run(cls):
        while True:
            cls.search()
            run_again = input("Do you want to run the program again? ")
            if run_again == 'n':
                break


if __name__ == '__main__':
    AppUI.run()

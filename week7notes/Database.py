import pymssql


class Database:
    connection = None

    @classmethod
    def connect(cls):
        if cls.connection is None:
            cls.connection = pymssql.connect(
                server="cisdbss.pcc.edu",
                database="IMDB",
                user="275student",
                password="275student",
                driver="{ODBC Driver 17 for SQL Server}"
            )

    @classmethod
    def fetch_movies(cls, year, type, num_votes):
        cursor = cls.connection.cursor()
        sql = """
        SELECT TOP 50 titleType, primaryTitle, startYear, runtimeMinutes
        FROM title_basics
        JOIN titleRatings ON title_basics.tconst = title_ratings.tconst
        WHERE startYear = %d
        AND titleType = %s
        AND numVotes > %d
        ORDER BY averageRating DESC;
        """
        cursor.execute(sql, year, type, num_votes)
        rows = cursor.fetchall()
        return rows

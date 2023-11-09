import pymssql


class Database:
    connection = None

    @classmethod
    def connect(cls):
        if cls.connection is None:
            cls.connection = pymssql.connect(
                server='cisdbss.pcc.edu',
                user='275student',
                password='275student',
                database='NAMES')

    @classmethod
    def fetch_names(cls, name, year, gender, name_count):
        cursor = cls.connection.cursor()
        sql = """
        SELECT TOP 50 Name, Year, Gender, NameCount
        FROM names
        JOIN name_counts ON names.NameID = name_counts.FK_NameID
        JOIN year_gender_totals ON name_counts.FK_YearGenderTotalID = year_gender_totals.YearGenderTotalID
        WHERE Name = %s
        WHERE Year = %d
        WHERE Gender = %s
        Where NameCount = %d
        ORDER BY NameCount DESC;
        """
        cursor.execute(sql, name, year, gender, name_count)
        rows = cursor.fetchall()
        return rows

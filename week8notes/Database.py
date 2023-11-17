import pyodbc
class Database:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = pyodbc.connect(
                server='cisdbss.pcc.edu',
                database='NAMES',
                user='275student',
                password='275student',
                trustservercertificate="Yes",
                driver="{ODBC Driver 17 for SQL Server}")

    @classmethod
    def fetch_names(cls, year, gender):
        if cls._connection is None:
            cls.connect()
        cursor = cls._connection.cursor()
        sql = """
        SELECT TOP 50 Name, Year, Gender, NameCount
        FROM names
        JOIN name_counts ON names.NameID = name_counts.FK_NameID
        JOIN year_gender_totals ON name_counts.FK_YearGenderTotalID = year_gender_totals.YearGenderTotalID
        WHERE Year = ? 
        AND Gender = ?
        ORDER BY NameCount DESC;
        """
        cursor.execute(sql, year, gender)
        rows = cursor.fetchall()
        print(rows)
        return rows


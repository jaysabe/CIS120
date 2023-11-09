# import pyodbc
#
# myConnection = pyodbc.connect(
#     server="cisdbss.pcc.edu",
#     database="IMDB",
#     user="275student",
#     password="275student",
#     driver="{ODBC Driver 17 for SQL Server}"
# )
#
# print(myConnection)
#
# cursor = myConnection.cursor()
# sql = """
# SELECT TOP 50 *
# FROM title_basics;
# """
# cursor.execute(sql)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# myConnection.close()
#

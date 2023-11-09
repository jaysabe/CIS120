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
# year = input("What year do you want? ")
# type = input("What type of show do you want? ")
# num_votes = input("What is the minimum number of votes? ")
#
# cursor = myConnection.cursor()
# sql = """
# SELECT TOP 50 titleType, primaryTitle, startYear, runtimeMinutes
# FROM title_basics
# JOIN titleRatings ON title_basics.tconst = title_ratings.tconst
# WHERE startYear = ?
# AND titleType = ?
# AND numVotes > ?
# ORDER BY averageRating DESC;
# """
# cursor.execute(sql, year, type, num_votes)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# myConnection.close()
#
#
#

'''
SQL 

Steps:
SQL -- compare most popular movies from 2000s:

SELECT TOP 50 titleType, primaryTitle, startYear, runtimeMinutes
FROM title_basics
JOIN titleRatings ON title_basics.tconst = title_ratings.tconst
WHERE startYear = 2000 
AND titleType = 'movie'
AND numVotes > 10000
ORDER BY averageRating DESC;

Note: don't's
1. f strings in the sql -- prone to SQL inject security issues
2.


import pymssql

myConnection = pymssql.connect(
    server="cisdbss.pcc.edu",
    database="IMDB",
    user="275student",
    password="275student",
    driver="{ODBC Driver 17 for SQL Server}"
)

print(myConnection)
year = input("What year do you want? ")
type = input("What type of show do you want? ")
num_votes = input("What is the minimum number of votes? ")

cursor = myConnection.cursor()
sql = """
SELECT TOP 50 titleType, primaryTitle, startYear, runtimeMinutes
FROM title_basics
JOIN titleRatings ON title_basics.tconst = title_ratings.tconst
WHERE startYear = %d 
AND titleType = %s
AND numVotes > &d
ORDER BY averageRating DESC;
"""
cursor.execute(sql, (year, type, num_votes))
rows = cursor.fetchall()
for row in rows:
    print(row)

myConnection.close()



'''
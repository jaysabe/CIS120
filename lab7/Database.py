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

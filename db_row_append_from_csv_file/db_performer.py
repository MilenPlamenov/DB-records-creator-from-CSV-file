import mysql.connector


class Performer:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        cursor = db.cursor()
        return cursor, db

    def execute(self, sql, mapper):
        cursor, db = self.connect()
        cursor.executemany(sql, mapper)
        db.commit()

        print(cursor.rowcount, "rows were inserted.")


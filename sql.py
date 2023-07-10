import sqlite3

class SQLDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        print("Connected to database.")

    def disconnect(self):
        self.connection.close()
        print("Disconnected from database.")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

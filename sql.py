import sqlite3

class SQLDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        self.connection.close()
    
    def commit(self):
        self.connection.commit()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                userid TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                api_key TEXT
            )
        '''
        self.execute_query(query)

    def insert_data(self, userid, username, api_key):
        query = 'INSERT INTO users VALUES (?, ?, ?)'
        values = (userid, username, api_key)
        self.execute_query(query, values)
        self.commit()

    def select_all(self):
        query = 'SELECT * FROM users'
        result = self.execute_query(query)
        return result

    def get_api_key(self, userid):
        query = 'SELECT api_key FROM users WHERE userid = ?'
        result = self.execute_query(query, (userid,))
        if result:
            return result[0][0]
        else:
            return None


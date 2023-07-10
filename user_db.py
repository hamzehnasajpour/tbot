from sql import SQLDatabase


class UserDB:
    def __init__(self, db_path):
        self.database = SQLDatabase(db_path)
        self.database.connect()
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                userid INTEGER,
                api_key TEXT NOT NULL
            )
        '''
        self.database.execute_query(create_table_query)

    def insert(self, username, userid, api_key):
        insert_data_query = '''
            INSERT INTO users (username, userid, api_key)
            VALUES (?, ?, ?)
        '''
        self.database.execute_query(insert_data_query, (username, userid, api_key))

    def api_key(self, userid):
        fetch_data_query = 'SELECT * FROM users WHERE userid = ?'
        return self.database.execute_query(fetch_data_query, (userid))['api_key']
        
        # database.disconnect()


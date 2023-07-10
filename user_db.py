from sql import SQLDatabase


class UserDB:
    def __init__(self, db_path):
        self.database = SQLDatabase(db_path)
        self.database.connect()
        self.database.create_table()

    def insert(self, username, userid, api_key):
        self.database.insert_data(username, userid, api_key)

    def api_key(self, userid):
        return self.database.get_api_key(userid)

    def __del__(self):
        self.database.disconnect()
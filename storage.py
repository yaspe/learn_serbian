import sqlite3


class Storage:
    def __init__(self):
        self.con = sqlite3.connect("data.db")
        self.create_database()

    def create_database(self):
        self.con.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, chat_id INTEGER UNIQUE)")
        self.con.commit()

    def count_users(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT COUNT(*) FROM users")
        return res.fetchone()[0]

    def is_known_user(self, chat_id):
        cur = self.con.cursor()
        res = cur.execute("SELECT COUNT(*) FROM users WHERE chat_id = :chat_id", {'chat_id': chat_id})
        return res.fetchone()[0] == 1

    def add_user(self, username, chat_id):
        if self.is_known_user(chat_id):
            return
        cur = self.con.cursor()
        cur.execute("INSERT INTO users (name, chat_id) VALUES (:username, :chat_id)", {'username': username, 'chat_id': chat_id})
        self.con.commit()

    def list_users(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT name FROM users")
        return [user[0] for user in res.fetchall()]


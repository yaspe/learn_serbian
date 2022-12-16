import sqlite3
import data
import random


class Storage:
    def __init__(self):
        self.con = sqlite3.connect("data.db")
        self.create_database()

    def create_database(self):
        self.con.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, chat_id INTEGER UNIQUE)")
        self.con.commit()

        self.con.execute("CREATE TABLE IF NOT EXISTS topics(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR UNIQUE)")
        self.con.commit()

        self.con.execute("CREATE TABLE IF NOT EXISTS user_stat(user_id INTEGER UNIQUE, total INTEGER, correct INTEGER)")
        self.con.commit()

        for topic in data.get_topics():
            try:
                self.add_topic(topic)
            except Exception as e:
                print(e, topic)

        try:
            self.con.execute("CREATE TABLE words(id INTEGER PRIMARY KEY AUTOINCREMENT, topic_id INTEGER, eng VARCHAR, srb VARCHAR)")
            self.con.commit()

            topics = self.list_topics()
            for topic in topics:
                for word in data.get_all_by_topic(topic[1]):
                    self.add_word(topic[0], word.eng, word.srb)

        except Exception as e:
            print(e)

    def add_answer(self, user_id, is_correct):
        cur = self.con.cursor()
        res = cur.execute("SELECT total, correct FROM user_stat WHERE user_id = :user_id", {'user_id': user_id})
        fetched = res.fetchone()

        if fetched:
            total = fetched[0] + 1
            correct = fetched[1] + (1 if is_correct else 0)
            cur.execute("UPDATE user_stat SET total = :total, correct = :correct WHERE user_id = :user_id",
                        {'user_id': user_id, 'total': total, 'correct': correct})
        else:
            cur = self.con.cursor()
            cur.execute("INSERT INTO user_stat (user_id, total, correct) VALUES (:user_id, :total, :correct)",
                        {'user_id': user_id, 'total': 1, 'correct': 1 if is_correct else 0})
        self.con.commit()

    def get_user_stat(self, user_id):
        cur = self.con.cursor()
        res = cur.execute("SELECT total, correct FROM user_stat WHERE user_id = :user_id", {'user_id': user_id})
        fetched = res.fetchone()

        if not fetched:
            return 0

        total = fetched[0]
        correct = fetched[1]
        return correct/total

    def add_word(self, topic_id, eng, srb):
        cur = self.con.cursor()
        cur.execute("INSERT INTO words (topic_id, eng, srb) VALUES (:topic_id, :eng, :srb)", {'topic_id': topic_id, 'eng': eng, 'srb': srb})
        self.con.commit()

    def get_words_by_topic(self, topic_id):
        cur = self.con.cursor()
        res = cur.execute("SELECT id, topic_id, eng, srb FROM words where topic_id = :topic_id", {'topic_id': topic_id})
        return res.fetchall()

    def get_some_words_by_topic(self, topic_id):
        words = self.get_words_by_topic(topic_id)
        random.shuffle(words)
        return words[:4]

    def count_words(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT COUNT(*) FROM words")
        return res.fetchone()[0]

    def add_topic(self, name):
        cur = self.con.cursor()
        cur.execute("INSERT INTO topics (name) VALUES (:name)", {'name': name})
        self.con.commit()

    def list_topics(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT id, name FROM topics")
        return res.fetchall()

    def list_topics_names(self):
        return [topic[1] for topic in self.list_topics()]

    def get_random_topic(self):
        return random.choice(self.list_topics())

    def get_topic_id(self, name):
        cur = self.con.cursor()
        res = cur.execute("SELECT id FROM topics WHERE name = :name", {'name': name})
        return res.fetchone()[0]

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
        res = cur.execute("SELECT name, chat_id FROM users")
        return ['%s (%s) = %s' % (user[0], user[1], self.get_user_stat(user[1])) for user in res.fetchall()]


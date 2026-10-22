"""Local SQLite storage with explicit connection lifecycle."""
import sqlite3
from pathlib import Path

class Database:
    def __init__(self, path=None):
        path = path if path is not None else Path(__file__).with_name('factory.db')
        self.conn = sqlite3.connect(path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL, vibration REAL, status TEXT, score INTEGER
        )''')
        self.conn.commit()

    def insert_reading(self, temp, vib, status, score):
        with self.conn:
            self.conn.execute(
                'INSERT INTO readings(temperature,vibration,status,score) VALUES (?,?,?,?)',
                (temp, vib, status, score))

    def fetch_all(self):
        return self.conn.execute('SELECT * FROM readings ORDER BY id DESC').fetchall()

    def close(self):
        self.conn.close()

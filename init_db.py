# init_db.py
import sqlite3
from pathlib import Path

DB = Path('lab.db')

def init():
    if DB.exists():
        print("Removing existing lab.db")
        DB.unlink()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL  -- plaintext on purpose for demo ONLY
    )
    ''')
    # sample users
    users = [
        ('alice', 'alicepwd'),
        ('bob', 'bobpwd'),
        ('admin', 'admin123')
    ]
    c.executemany('INSERT INTO users (username, password) VALUES (?, ?)', users)
    conn.commit()
    conn.close()
    print("Initialized lab.db with sample users.")

if __name__ == '__main__':
    init()

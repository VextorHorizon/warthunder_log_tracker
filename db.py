import sqlite3

def connect_db():
    return sqlite3.connect("stats.db")

def create_table():
    with connect_db() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS sessions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        vehicle TEXT,
                        kills INTEGER,
                        deaths INTEGER,
                        map_name TEXT
                    )''')
        conn.commit()

def insert_session(date, vehicle, kills, deaths, map_name):
    with connect_db() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO sessions (date, vehicle, kills, deaths, map_name) VALUES (?, ?, ?, ?, ?)",
                (date, vehicle, kills, deaths, map_name))
        conn.commit()
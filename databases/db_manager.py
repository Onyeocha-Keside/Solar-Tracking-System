import sqlite3
from config import DB_PATH

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            optimal_azimuth REAL,
            optimal_elevation REAL,
            verified_azimuth REAL,
            verified_elevation REAL
        )
    """)
    conn.commit()
    conn.close()

def log_entry(time_and_date, optimal_position, verified_position):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (timestamp, optimal_azimuth, optimal_elevation, verified_azimuth, verified_elevation)
        VALUES (?, ?, ?, ?, ?)
    """, (time_and_date, optimal_position[0], optimal_position[1], verified_position[0], verified_position[1]))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return logs
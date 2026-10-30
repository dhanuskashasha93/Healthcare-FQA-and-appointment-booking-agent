import sqlite3

def save_appointment(doctor, date, time):

    connection = sqlite3.connect("healthcare.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor TEXT,
            date TEXT,
            time TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO appointments (doctor, date, time) VALUES (?, ?, ?)",
        (doctor, date, time)
    )

    connection.commit()
    connection.close()
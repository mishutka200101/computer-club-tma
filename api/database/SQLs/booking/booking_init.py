TABLE = """
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        seat_number INT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL,
        start TEXT NOT NULL,
        end TEXT NOT NULL,
        date TEXT NOT NULL,
        user_id TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(tg_id)
    );
"""
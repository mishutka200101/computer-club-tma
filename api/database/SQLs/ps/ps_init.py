TABLE = """
    CREATE TABLE IF NOT EXISTS ps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT DEFAULT 'free' NOT NULL,
        start_order TEXT,
        end_order TEXT
    );
"""

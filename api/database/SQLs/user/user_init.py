TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        tg_id TEXT PRIMARY KEY,
        username TEXT,
        last_pc INTEGER,
        last_pc_date TEXT,
        last_ps INTEGER,
        last_ps_date TEXT
    );
"""

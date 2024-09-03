import os

settings = {
    'DB_URL': f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@postgres:5432/{os.getenv('DB_DB')}",
}

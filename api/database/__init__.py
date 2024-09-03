from playhouse.db_url import connect

from database.config import settings

database = connect(settings["DB_URL"])

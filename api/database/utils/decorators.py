from pydantic import ValidationError
from peewee import IntegrityError
from loguru import logger


def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            logger.error('Pydantic error: ' + str(e))
            return None
        except IntegrityError as e:
            logger.error('Peewee error: ' + str(e))
            return None
        except Exception as e:
            logger.error('Unknown error: ' + str(e))
            return None
    return wrapper

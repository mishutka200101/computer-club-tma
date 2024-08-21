from loguru import logger

from models.ps import PS
from database.helper import process_sql, get_object, get_all_objects


def create_ps() -> None:
    SQL = """
        INSERT INTO ps(status) VALUES('free');
    """
    result = process_sql(SQL=SQL)
    if result:
        logger.success("Created new ps")
    else:
        logger.error("Error creating ps")


def get_ps(ps_id: int) -> PS | None:
    SQL = f"""
        SELECT * FROM ps
        WHERE id = '{ps_id}';
    """
    ps = get_object(SQL=SQL, table=PS)
    return ps


def get_all_ps() -> list[PS] | None:
    SQL = """
        SELECT * FROM ps;
    """
    pss = get_all_objects(SQL=SQL, table=PS)
    return pss


def edit_ps(ps: PS) -> bool:
    SQL = f"""
        UPDATE ps
        SET status = '{ps.status}',
            start_order = '{ps.start_order}',
            end_order = '{ps.end_order}'
        WHERE id = {ps.id};
    """
    result = process_sql(SQL=SQL)
    if result:
        logger.success(
            f"Edited ps №{ps.id} | status: {ps.status}, start_order={ps.start_order}, end_order={ps.end_order}")
    else:
        logger.error(f"Error editing ps №{ps.id}")
    return result

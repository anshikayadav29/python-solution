from contextlib import contextmanager

@contextmanager
def temp_transaction(db_connection):
    cursor = db_connection.cursor()
    try:
        yield cursor
        db_connection.commit()
    except Exception as e:
        db_connection.rollback()
        raise e

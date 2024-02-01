from contextlib import contextmanager
from sqlite3 import Error

import config
from backend_prd.api.models.others import SQLiteConnectionPool

db_pool = SQLiteConnectionPool(config.db_info)


@contextmanager
def get_db():
    # database
    conn = db_pool.get_connection()
    try:
        yield conn
    finally:
        db_pool.return_connection(conn)


def execute_sqlite_sql(sql, params=None, should_print=False, fetch_size=None):
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            if sql.strip().upper().startswith("SELECT"):
                if fetch_size:
                    results = cursor.fetchmany(fetch_size)
                else:
                    results = cursor.fetchall()

                if should_print:
                    for row in results:
                        print(row)
                return results
            else:
                conn.commit()
                return None
    except Error as e:
        config.logger.error(f"An error occurred while executing SQL: {e}")
        return None


def create_tables():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS siscon_test (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        );
    """
    execute_sqlite_sql(create_table_query)


def close_db_connection():
    db_pool.close_all_connections()

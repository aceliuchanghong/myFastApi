from contextlib import contextmanager
from sqlite3 import Error
from backend_prd.api.schemas import create_table_queries
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


def safe_format_sql(sql, parameters):
    # 使用 SQLite 的参数替换机制来安全地格式化 SQL 语句
    # 注意：这只是为了打印目的，不要使用这个函数来执行实际的 SQL 语句
    parameterized_sql = sql
    if parameters:
        for param in parameters:
            # 替换参数占位符
            parameterized_sql = parameterized_sql.replace("?", repr(param), 1)
    return parameterized_sql


def execute_sqlite_sql(sql, params=None, should_print=False, fetch_size=None, should_log=False):
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            if should_log:
                formatted_sql = safe_format_sql(sql, params)
                config.logger.info(f"Executing SQL statement: {formatted_sql}")
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
    for query in create_table_queries:
        execute_sqlite_sql(query)


def close_db_connection():
    db_pool.close_all_connections()

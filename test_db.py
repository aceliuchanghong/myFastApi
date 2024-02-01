from backend_prd.core.database import execute_sqlite_sql

table_list = """SELECT name FROM sqlite_master WHERE type='table'"""

if __name__ == '__main__':
    execute_sqlite_sql(table_list, should_print=True, fetch_size=10)

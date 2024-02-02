from backend_prd.api.schemas import task_list_query
from backend_prd.core.database import execute_sqlite_sql

table_list = """SELECT name FROM sqlite_master WHERE type='table'"""
table_list_test = """SELECT name FROM sqlite_master WHERE type= ? """
task_info_list = """SELECT *  FROM task_info"""

if __name__ == '__main__':
    # execute_sqlite_sql(table_list, should_print=True, fetch_size=10, should_log=True)
    # execute_sqlite_sql(table_list_test, params=('table',), should_print=True, fetch_size=10, should_log=True)
    execute_sqlite_sql(task_info_list, should_print=True, fetch_size=10, should_log=True)
    rows = execute_sqlite_sql(task_list_query, should_log=True)
    for row in rows:
        print(row)

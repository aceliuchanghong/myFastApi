task_insert_sql = f"""
INSERT INTO task_info (user_id, task_type, task_id, task_name, task_status, start_time, last_modify_time, remark)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS siscon_test (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS task_info (
        user_id TEXT,
        task_type TEXT,
        task_id TEXT,
        task_name TEXT,
        task_status TEXT,
        start_time TEXT,
        last_modify_time TEXT,
        remark TEXT,
        PRIMARY KEY (user_id, task_type, task_id)
    );
    """
]

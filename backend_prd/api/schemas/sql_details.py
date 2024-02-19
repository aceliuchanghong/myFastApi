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
    """,
    """
    -- 用户信息表 (user_info)
    CREATE TABLE IF NOT EXISTS user_info (
      user_id TEXT,
      username TEXT,
      password_hash TEXT,
      email TEXT,
      created_at TEXT,
      last_login TEXT,
      last_login_ip TEXT,
      last_login_mac TEXT,
      is_active TEXT
    );
    """,
    """
    -- 用户购买历史表 (purchase_history)
    CREATE TABLE IF NOT EXISTS purchase_history (
      purchase_id TEXT,
      user_id TEXT,
      product_id TEXT,
      quantity TEXT,
      purchase_date TEXT,
      total_price TEXT,
      is_successful TEXT
    );
    """,
    """
    -- 配置信息表 (user_settings)
    CREATE TABLE IF NOT EXISTS user_settings (
      setting_id TEXT,
      user_id TEXT,
      setting_name TEXT,
      setting_value TEXT
    );
    """,
    """
    -- 产品信息表 (product_info)
    CREATE TABLE IF NOT EXISTS product_info (
      product_id TEXT,
      product_name TEXT ,
      product_description TEXT,
      price TEXT 
    );
    """
]

task_list_query = """
        SELECT
            task_type,
            SUM(CASE WHEN task_status = 'SUC' THEN 1 ELSE 0 END) AS success_count,
            SUM(CASE WHEN task_status = 'RUN' THEN 1 ELSE 0 END) AS in_progress_count,
            SUM(CASE WHEN task_status = 'ERR' THEN 1 ELSE 0 END) AS failure_count
        FROM task_info
        GROUP BY task_type
    """

user_task_list_query = """
        SELECT
            task_type,
            SUM(CASE WHEN task_status = 'SUC' THEN 1 ELSE 0 END) AS success_count,
            SUM(CASE WHEN task_status = 'RUN' THEN 1 ELSE 0 END) AS in_progress_count,
            SUM(CASE WHEN task_status = 'ERR' THEN 1 ELSE 0 END) AS failure_count
        FROM task_info where user_id = ? 
        GROUP BY task_type
    """

user_task_detail_query = """
        SELECT
        user_id,
        task_type,
        task_id,
        task_name,
        task_status,
        start_time,
        last_modify_time,
        remark
        FROM task_info where user_id = ? and task_type = ? 
        order by last_modify_time desc,task_name desc
    """

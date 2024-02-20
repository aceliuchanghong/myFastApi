# job/task
task_insert_sql = f"""
INSERT INTO task_info (user_id, task_type, task_id, task_name, task_status, start_time, last_modify_time, remark)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""
job_log_insert_sql = f"""
INSERT INTO job_history (job_id, task_id, user_id, job_run_date, job_run_times, job_status, job_run_log, job_remark)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

task_list_query = """
        SELECT
            task_type,
            SUM(CASE WHEN task_status = 'SUC' THEN 1 ELSE 0 END) AS success_count,
            SUM(CASE WHEN task_status = 'RUN' THEN 1 ELSE 0 END) AS in_progress_count,
            SUM(CASE WHEN task_status = 'ERR' THEN 1 ELSE 0 END) AS failure_count
        FROM task_info
        GROUP BY task_type
    """

# user/task
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

user_task_del = """
        delete FROM task_info where user_id = ? and task_id = ? 
    """

user_task_rerun = """
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

# user
user_insert_sql = f"""
INSERT INTO user_info (user_id, username, password_hash, email, role, created_dt, last_login, last_login_ip, last_login_mac, is_active)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
user_query_sql = f"""
SELECT user_id, username, email, role, created_dt, last_login, is_active
FROM user_info
WHERE user_id = ?;
"""
user_update_sql = f"""
UPDATE user_info
SET username = ?, email = ?, role = ?, last_login = ?, last_login_ip = ?, last_login_mac = ?, is_active = ?
WHERE user_id = ?;
"""
user_del_sql = f"""
DELETE FROM user_info
WHERE user_id = ?;
"""

# purchase_history
goods_his_insert_sql = f"""
INSERT INTO purchase_history (purchase_id, user_id, product_id, quantity, purchase_date, total_price, is_successful)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
goods_his_query_sql = f"""
SELECT purchase_id, user_id, product_id, quantity, purchase_date, total_price, is_successful
FROM purchase_history
WHERE user_id = ?;
"""
goods_his_update_sql = f"""
UPDATE purchase_history
SET quantity = ?, total_price = ?, is_successful = ?
WHERE purchase_id = ?;
"""
goods_his_del_sql = f"""
DELETE FROM purchase_history
WHERE purchase_id = ?;
"""

# product_info
goods_insert_sql = f"""
INSERT INTO product_info (product_id, product_name, product_description, price)
VALUES (?, ?, ?, ?);
"""
goods_query_sql = f"""
SELECT product_id, product_name, product_description, price
FROM product_info;
"""
goods_update_sql = f"""
UPDATE product_info
SET product_name = ?, product_description = ?, price = ?
WHERE product_id = ?;
"""
goods_del_sql = f"""
DELETE FROM product_info
WHERE product_id = ?;
"""

# tables
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
      role TEXT,
      created_dt TEXT,
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
    -- 产品信息表 (product_info)
    CREATE TABLE IF NOT EXISTS product_info (
      product_id TEXT,
      product_name TEXT ,
      product_description TEXT,
      price TEXT 
    );
    """,
    """
    -- 用户执行操作历史表 (job_history)
    CREATE TABLE IF NOT EXISTS job_history (
      job_id TEXT,
      task_id TEXT,
      user_id TEXT,
      job_run_date TEXT,
      job_run_times TEXT,
      job_status TEXT,
      job_run_log TEXT,
      job_remark TEXT
    );
    """,
    """
    -- 参数表
    CREATE TABLE IF NOT EXISTS this_sys_param (
      aspect TEXT,
      mapping_filed TEXT,
      code TEXT,
      answer TEXT,
      remark1 TEXT,
      remark2 TEXT
    );
    """
]

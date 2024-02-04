import sqlite3
from sqlite3 import Error
from config import logger
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


# 数据库模型
class SQLiteConnectionPool:
    def __init__(self, db_file, max_connections=15):
        self.db_file = db_file
        self.max_connections = max_connections
        self.pool = []

    def get_connection(self):
        if self.pool:
            conn = self.pool.pop()
            logger.info("Reusing connection from pool.")
            return conn
        else:
            return self.create_connection()

    def return_connection(self, conn):
        if len(self.pool) < self.max_connections:
            logger.info("Returning connection to pool.")
            self.pool.append(conn)
        else:
            logger.info("Closing excess connection.")
            conn.close()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            logger.info("Created new database connection.")
            return conn
        except Error as e:
            logger.error(f"Database connect error: {e}")
            return None

    def close_all_connections(self):
        while self.pool:
            conn = self.pool.pop()
            conn.close()
        logger.info("Closed all database connections.")

from dotenv import load_dotenv
import os

# 加载.env文件中的环境变量
load_dotenv()
"""
DATABASE_USER=example_user
DATABASE_PASS=example_password
SECRET_KEY=mysecretkey
API_KEY=apikey123456789
"""
# 访问环境变量
database_user = os.getenv('DATABASE_USER')
database_pass = os.getenv('DATABASE_PASS')
secret_key = os.getenv('SECRET_KEY')
api_key = os.getenv('API_KEY')

print(database_user)

# backend/core/config.py

from fastapi.templating import Jinja2Templates

from pathlib import Path

# 获取当前文件的路径
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 初始化Jinja2Templates实例，指定模板文件夹的绝对路径
templates = Jinja2Templates(directory=str(BASE_DIR / 'frontend/templates'))

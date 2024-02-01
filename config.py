from starlette.templating import Jinja2Templates
import logging

templates = Jinja2Templates(directory="frontend_prd/templates")
proxies = {
    "http": "http://127.0.0.1:10809",
    "https": "http://127.0.0.1:10809"
}

# database
db_info = "backend_prd/core/site_basic.db"

# DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = "INFO"

# 设置日志
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

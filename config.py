from starlette.templating import Jinja2Templates
import logging

# 模板位置
templates = Jinja2Templates(directory="frontend_prd/templates")

# 代理信息
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

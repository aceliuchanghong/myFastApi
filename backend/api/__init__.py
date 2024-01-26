# ├── api/                     # 存放与API相关的代码
# │   ├── v1/                  # 版本控制，方便未来的扩展
# │   │   ├── endpoints/       # 存放具体的API端点
# │   │   │   ├── auth.py      # 认证相关的API
# │   │   │   ├── users.py     # 用户相关的API
# │   │   │   ├── content.py   # 内容处理相关API
# │   │   │   └── ...
# │   │   ├── __init__.py
# │   │   └── deps.py          # 依赖项（如数据库会话、权限校验等）
# │   ├── __init__.py
# │   └── routers.py           # 路由注册

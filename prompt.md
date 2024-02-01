初始化:
使用的后端是fastapi,前端bootstrap+jinja2,已经引入了
```
<script src="{{ url_for('static', path='/others_js/jquery.min.js') }}"></script>
<!-- Popper.JS -->
<script src="{{ url_for('static', path='/others_js/popper.min.js') }}"></script>
<!-- Bootstrap JS -->
<script src="{{ url_for('static', path='/others_js/bootstrap.bundle.min.js') }}"></script>
```
请尽量使用已有的脚本完成以下任务



我需要一个fastapi+bootstrap编写的前后端工程,其会在项目的不同部分中进行开发,大致目的是提供不同的服务在左边选项,用户点击之后
可以选择创建一个对应任务,然后填写对应任务他所需要的表单信息,点击提交,就可以了,然后可以查看任务进度,项目结构如下:
```
后端说明：
app/main.py 是FastAPI应用的入口文件。
app/models.py 定义你的数据库模型（ORM）。
app/schemas.py 用于请求和响应模型的Pydantic模型。
app/crud.py 包含与数据库交互的逻辑。
app/deps.py 包含依赖项函数，如获取数据库会话等。
db/base.py 用于设置数据库和表的基类。
api/api_v1/endpoints/ 包含特定的API路由和视图函数。
core/config.py 包含配置相关代码，如读取环境变量。
tests/ 包含测试代码。

前端说明：
frontend/layui/ 包含layui框架的文件。
frontend/css/ 和 frontend/js/ 包含自定义的样式和脚本。
frontend/views/ 包含HTML模板文件。
frontend/index.html 是前端的入口文件。

myproject/
│
├── backend/           # 后端代码
│   ├── app/           # FastAPI应用
│   │   ├── __init__.py
│   │   ├── main.py    # FastAPI应用入口
│   │   ├── models.py  # 数据模型
│   │   ├── schemas.py # 数据校验和序列化
│   │   ├── crud.py    # 数据库的CRUD操作
│   │   └── deps.py    # 依赖项，如数据库会话、授权等
│   │
│   ├── db/            # 数据库迁移和初始化
│   │   ├── __init__.py
│   │   └── base.py    # 数据库设置和基类
│   │
│   ├── api/           # API路由和视图
│   │   ├── __init__.py
│   │   ├── api_v1/    # 版本1的API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── task.py      # 任务相关API
│   │   │   │   └── progress.py  # 进度相关API
│   │   │   └── deps.py
│   │   └── dependencies.py
│   │
│   └── core/          # 核心模块，如配置
│       ├── __init__.py
│       └── config.py  # 配置文件
│
├── frontend/          # 前端代码
│   ├── layui/         # layui库相关文件
│   │   └── ...
│   ├── css/           # 自定义样式
│   ├── js/            # JavaScript脚本
│   ├── views/         # HTML模板
│   └── index.html     # 主页文件
│
├── tests/             # 测试代码
│   ├── __init__.py
│   └── test_api.py
│
├── requirements.txt   # 项目依赖
├── README.md          # 项目文档
└── .env               # 环境变量和配置
```
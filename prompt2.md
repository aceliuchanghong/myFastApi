这个是项目结构,使用FastApi+bootstrap+jquery+jinja2+sqlite开发,并且将md文件嵌入fastapi,后端暂时略去
```项目框架
myFastApi/
|
├── LICENSE
├── README.md
├── config.py
├── main.py
├── requirements.txt
├── backend_prd/
│   ├── api/
│   │   ├── models/
│   │   │   ├── audio.py
│   │   │   ├── image.py
│   │   │   ├── user.py
│   │   │   ├── video.py
│   │   │   └── webpage.py
│   │   ├── routes/
│   │   │   ├── audio.py
│   │   │   ├── auth.py
│   │   │   ├── image.py
│   │   │   ├── video.py
│   │   │   └── webpage.py
│   │   └── schemas/
│   │       ├── audio.py
│   │       ├── image.py
│   │       ├── user.py
│   │       ├── video.py
│   │       └── webpage.py
│   └── core/
│       ├── audio_processor.py
│       ├── database.py
│       ├── image_processor.py
│       ├── security.py
│       ├── video_processor.py
│       └── webpage_scraper.py
└── utils/
    └── markdown.py
```
项目有
1. 用户登录注册
2. 提供4个大的功能,视频文件处理,网页爬取,音频文件处理,图片处理

```main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from fastapi import Depends

from backend_prd.api.routes import audio, image, video, webpage
from backend_prd.api.routes.auth import auth_router
from backend_prd.core.database import create_tables, close_db_connection

app = FastAPI()
templates = Jinja2Templates(directory="frontend_prd/templates")
app.mount("/static", StaticFiles(directory="frontend_prd/static"), name="static")
app.add_event_handler("startup", create_tables)
app.add_event_handler("shutdown", close_db_connection)

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    # Your registration logic here
    return {"message": "User registered successfully"}
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    # Your login logic here
    return {"message": "Login successful"}
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(audio.router, prefix="/audio", tags=["Audio"])
app.include_router(image.router, prefix="/image", tags=["Image"])
app.include_router(video.router, prefix="/video", tags=["Video"])
app.include_router(webpage.router, prefix="/webpage", tags=["Webpage"])
```
帮我优化一下main

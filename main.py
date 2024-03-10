from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic
from passlib.context import CryptContext
import uvicorn
from backend_prd.api.routes import audio, image, video, webpage, start
from backend_prd.api.routes.auth import auth_router
from backend_prd.core.database import create_tables
from backend_prd.core.exception_handlers import *
from config import templates
# 开始吧
app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend_prd/static"), name="static")
app.add_event_handler("startup", create_tables)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(audio.router, prefix="/audio", tags=["Audio"])
app.include_router(image.router, prefix="/image", tags=["Image"])
app.include_router(video.router, prefix="/video", tags=["Video"])
app.include_router(webpage.router, prefix="/webpage", tags=["Webpage"])
app.include_router(start.router, tags=["Starter"])

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=2024, reload=True)

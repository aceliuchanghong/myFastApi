import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from jinja2 import TemplateNotFound
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_404_NOT_FOUND
from starlette.exceptions import HTTPException as StarletteHTTPException

from backend.core.config import templates
from backend.library.helpers import openfile
from pydantic import BaseModel
from backend.app.routes import router

app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


class Item(BaseModel):
    name: str
    description: str = None


@app.exception_handler(TemplateNotFound)
async def template_not_found_handler(request, exc):
    # 当模板未找到时，返回自定义的404页面
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    if exc.status_code == HTTP_404_NOT_FOUND:
        return templates.TemplateResponse("404.html", {"request": request})
    # 如果不是404错误，可以继续抛出异常或者处理其他错误
    raise exc


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openfile(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/task/{task_name}", response_class=HTMLResponse)
async def task(request: Request, task_name: str):
    data = openfile(task_name + ".md")
    return templates.TemplateResponse(f"task/{task_name}.html", {"request": request, "data": data})


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

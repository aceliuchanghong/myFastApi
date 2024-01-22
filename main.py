import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from backend.library.helpers import openfile

app = FastAPI()

templates = Jinja2Templates(directory='frontend/templates')
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


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
    return templates.TemplateResponse("task.html", {"request": request, "data": data})


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

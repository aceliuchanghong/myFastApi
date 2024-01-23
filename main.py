import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
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


@app.post("/answer", response_class=HTMLResponse)
async def answer(request: Request):
    form_data = await request.form()
    answer2 = form_data.get("answer2")
    return templates.TemplateResponse("task/confirmation.html", {"request": request, "answer2": answer2})


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

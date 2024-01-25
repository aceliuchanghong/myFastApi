import shutil
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from langchain_community.document_loaders import WebBaseLoader
from fastapi import File, Form, UploadFile
from backend.core.config import templates, proxies
from backend.library.helpers import *

router = APIRouter()


def allowed_file_images(filename):
    # 检查文件扩展名是否合法
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


@router.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openfile(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@router.get("/task/{task_name}", response_class=HTMLResponse)
async def task(request: Request, task_name: str):
    data = openfile(task_name + ".md")
    return templates.TemplateResponse(f"task/{task_name}.html",
                                      {"request": request, "data": data, "active_page": task_name})


@router.get("/info", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.post("/work/crawl_url", response_class=HTMLResponse)
async def answer(request: Request):
    form_data = await request.form()
    use_proxy = form_data.get("use_proxy") == "True"  # 检查是否有 "use_proxy" 字段且其值为 "True"
    my_proxy = None
    if use_proxy:
        my_proxy = proxies
    answer2 = form_data.get("answer2")
    if answer2 == "因为困难多壮志":
        return templates.TemplateResponse("task/crawl_url_confirmation.html", {"request": request, "answer2": answer2})
    if is_valid_url(answer2) and re.match(url_regex, answer2):
        # loader = WebBaseLoader(answer2)
        loader = WebBaseLoader(answer2, proxies=my_proxy)
        docs = loader.load()
        for doc in docs:
            answer2 = doc.page_content
        return templates.TemplateResponse("task/crawl_url_confirmation.html", {"request": request, "answer2": answer2})
    else:
        return templates.TemplateResponse("task/crawl_url_confirmation.html",
                                          {"request": request, "answer2": "不合法连接"})


@router.post("/work/deal_images", response_class=HTMLResponse)
async def page(request: Request, file: UploadFile = File(...),
               format: str = Form(...),
               filename: str = Form(...)):
    file_location = f"testfiles/{filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.read())

    # 处理完毕后，您可以重定向用户或返回所需的任何信息
    return JSONResponse(content={"redirect": "/"})


@router.get("/work/make_pay", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.get("/work/没想好", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.post("/work/upload_file")
async def upload_file(file: UploadFile = File(...)):
    # 保存文件或进行其他处理
    file_directory = Path("testfiles")
    file_directory.mkdir(exist_ok=True)
    file_location = file_directory / file.filename  # 构建文件路径

    # 使用异步方式写入文件
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print({"filename": file.filename})
    return {"filename": file.filename}


@router.post("/work/submit_form")
async def submit_form(username: str = Form(...), email: str = Form(...)):
    print({"username": username, "email": email})
    return {"username": username, "email": email}

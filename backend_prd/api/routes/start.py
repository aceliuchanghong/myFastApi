from fastapi import Request, Form, Depends
from starlette.responses import HTMLResponse
from fastapi.security import HTTPBasicCredentials
from backend_prd.api.schemas import task_list_query, user_task_list_query
from backend_prd.core.database import execute_sqlite_sql
from config import templates
from fastapi import APIRouter, BackgroundTasks
import os
from test.test_bg_task import write_log
from utils.url_valid import openfile

router = APIRouter()


@router.get("/Pages/About")
def get_page_about(request: Request, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message='liu')
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/Pages/Faq")
def get_page_contact(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})


@router.get("/Pages/Crawl")
def get_page_crawl(request: Request):
    return templates.TemplateResponse("web_crawl.html", {"request": request})


@router.get("/Pages/Image")
def get_image_deal(request: Request):
    return templates.TemplateResponse("deal_image.html", {"request": request})


@router.get("/Pages/Video")
def get_video_deal(request: Request):
    return templates.TemplateResponse("deal_video.html", {"request": request})


@router.get("/Pages/Audio")
def get_audio_deal(request: Request):
    return templates.TemplateResponse("deal_audio.html", {"request": request})


@router.get("/Pages/Task")
def get_task_info(request: Request):
    rows = execute_sqlite_sql(task_list_query, should_log=True)
    task_info = []
    if rows:
        for row in rows:
            task_type, success_count, in_progress_count, failure_count = row
            task_info.append({
                "task_type": task_type,
                "success_count": success_count,
                "in_progress_count": in_progress_count,
                "failure_count": failure_count
            })
    return templates.TemplateResponse("task_info.html", {"request": request, "task_info": task_info})


@router.get("/Pages/Task/{user_id}", response_class=HTMLResponse)
def get_task_info(request: Request, user_id: str):
    results = execute_sqlite_sql(user_task_list_query, params=(user_id,), should_log=True)
    task_info = []
    if results:
        for result in results:
            task_type, success_count, in_progress_count, failure_count = result
            task_info.append({
                "task_type": task_type,
                "success_count": success_count,
                "in_progress_count": in_progress_count,
                "failure_count": failure_count
            })
    redirect_url = "redirect/user_task_info.html"
    return templates.TemplateResponse(redirect_url, {"request": request, "task_info": task_info})


@router.get("/Docs", response_class=HTMLResponse)
def get_docs_list(request: Request):
    files = []
    for filename in os.listdir('frontend_prd/templates/docs'):
        if filename.endswith('.md'):
            file_id = os.path.splitext(filename)[0]
            file_name = file_id.replace('_', ' ').title()
            files.append({'id': file_id, 'name': file_name})
    return templates.TemplateResponse("docs.html", {"request": request, "files": files})


@router.get("/Docs/{md_file_name}", response_class=HTMLResponse)
def get_doc(request: Request, md_file_name: str):
    files = []
    for filename in os.listdir('frontend_prd/templates/docs'):
        if filename.endswith('.md'):
            file_id = os.path.splitext(filename)[0]
            file_name = file_id.replace('_', ' ').title()
            files.append({'id': file_id, 'name': file_name})

    data = openfile(md_file_name + ".md")
    return templates.TemplateResponse("docs/docs_details.html", {"request": request, "files": files, "data": data})


@router.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    # Your registration logic here
    return {"message": "User registered successfully"}


@router.post("/login")
def login(request: Request):
    # Your login logic here
    return {"message": "Login successful"}

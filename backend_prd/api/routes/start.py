from fastapi import Request
from config import templates
from fastapi import APIRouter, BackgroundTasks

from test.test_bg_task import write_log

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
    return templates.TemplateResponse("task_info.html", {"request": request})


@router.get("/Docs")
def get_docs_list(request: Request):
    return templates.TemplateResponse("docs/index.html", {"request": request})

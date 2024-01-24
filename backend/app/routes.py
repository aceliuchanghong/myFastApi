from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from langchain_community.document_loaders import WebBaseLoader

from backend.core.config import templates
from backend.library.helpers import *

router = APIRouter()


@router.get("/info", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.post("/work/crawl_url", response_class=HTMLResponse)
async def answer(request: Request):
    form_data = await request.form()
    answer2 = form_data.get("answer2")
    if answer2 == "因为困难多壮志":
        return templates.TemplateResponse("task/crawl_url_confirmation.html", {"request": request, "answer2": answer2})
    if is_valid_url(answer2) and re.match(url_regex, answer2):
        loader = WebBaseLoader(answer2)
        docs = loader.load()
        for doc in docs:
            answer2 = doc.page_content
        return templates.TemplateResponse("task/crawl_url_confirmation.html", {"request": request, "answer2": answer2})
    else:
        return templates.TemplateResponse("task/crawl_url_confirmation.html",
                                          {"request": request, "answer2": "不合法连接"})


@router.get("/work/deal_images", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.get("/work/make_pay", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.get("/work/没想好", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from backend.core.config import templates

router = APIRouter()


@router.get("/info", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})


@router.post("/answer", response_class=HTMLResponse)
async def answer(request: Request):
    form_data = await request.form()
    answer2 = form_data.get("answer2")
    return templates.TemplateResponse("task/confirmation.html", {"request": request, "answer2": answer2})

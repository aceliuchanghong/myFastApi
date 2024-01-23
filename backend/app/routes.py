from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from backend.core.config import templates

router = APIRouter()


@router.get("/info", response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("info.html", {"request": request})

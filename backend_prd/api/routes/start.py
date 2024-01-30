from fastapi import Request

from fastapi import APIRouter

from config import templates

router = APIRouter()


@router.get("/Pages/About")
def get_page_about():
    return {"message": "Get image list"}


@router.get("/Pages/Contact")
def get_page_contact():
    return {"message": "Get image list"}


@router.get("/Pages/Login")
def get_page_login():
    return {"message": "Get image list"}


@router.get("/Docs")
def get_docs_list(request: Request):
    return templates.TemplateResponse("docs/index.html", {"request": request})

import re
from fastapi import Request

from fastapi import APIRouter
from langchain_community.document_loaders import WebBaseLoader

from backend_prd.api.models.others import InputInfo
from config import templates, proxies
from utils.url_valid import is_valid_url, url_regex

router = APIRouter()


@router.get("/Pages/About")
def get_page_about():
    return {"message": "Get image list"}


@router.get("/Pages/Contact")
def get_page_contact():
    return {"message": "Get image list"}


@router.get("/Pages/Login")
def get_page_login(request: Request):
    return templates.TemplateResponse("test_files.html", {"request": request})


@router.get("/Docs")
def get_docs_list(request: Request):
    return templates.TemplateResponse("docs/index.html", {"request": request})


@router.post("/webpage/info")
async def process_info(request: Request, input_data: InputInfo):
    """
    eg:
        https://www.4hu.tv/view/202401/79272.html
        https://www.sohu.com/a/744144846_121687421
        https://www.runoob.com/fastapi/fastapi-form.html
    :param request:
    :param input_data:
    :return:
    """
    modified_text = input_data.inputText
    # 可以根据checkboxState的值来调整返回的内容
    my_proxy = None
    if input_data.checkboxState:
        my_proxy = proxies
    if modified_text == "因为困难多壮志":
        return {"output_text": modified_text + ",不教红尘惑坚心"}
    elif is_valid_url(modified_text.strip()) and re.match(url_regex, modified_text.strip()):
        loader = WebBaseLoader(modified_text, proxies=my_proxy)
        docs = loader.load()
        content = ""
        for doc in docs:
            content += doc.page_content.replace("\n", "").replace(" ", "")
        return {"output_text": content}
    else:
        return {"output_text": "不规则链接"}

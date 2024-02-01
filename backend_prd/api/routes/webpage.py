from fastapi import APIRouter
from langchain_community.document_loaders import WebBaseLoader
import re
from fastapi import Request

from backend_prd.api.models.webpage import InputInfo
from config import proxies
from utils.url_valid import is_valid_url, url_regex

router = APIRouter()


@router.post("/info")
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
        try:
            loader = WebBaseLoader(modified_text, proxies=my_proxy)
            docs = loader.load()
            content = ""
            for doc in docs:
                content += doc.page_content.replace("\n", "").replace(" ", "")
            return {"output_text": content}
        except Exception as e:
            print("Error:", e)
            return {"output_text": "网站拒绝访问,可以尝试使用代理\n" + str(e)}
    else:
        return {"output_text": "不规则链接"}

import os.path
import markdown
from urllib.parse import urlparse


def openfile(filename):
    filepath = os.path.join("backend/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return data


def is_valid_url(url):
    try:
        result = urlparse(url)
        # 校验协议（scheme）和网络位置（netloc）是否存在
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

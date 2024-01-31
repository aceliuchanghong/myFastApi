import os.path
import markdown
from urllib.parse import urlparse
import re


def openfile(filename):
    filepath = os.path.join("backend/pages/", filename)
    if not os.path.exists(filepath):
        data = {
            "text": f"no {filename}.md file"
        }
    else:
        with open(filepath, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        html = markdown.markdown(text)
        data = {
            "text": html
        }
    return data


def is_valid_url(url):
    parsed = urlparse(url)
    # 检查方案（scheme）和网络位置部分（netloc）
    return bool(parsed.scheme) and bool(parsed.netloc)


# 正则表达式，用于初步验证URL的格式
url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

from pydantic import BaseModel


# 创建一个模型来解析传入的数据
class InputInfo(BaseModel):
    inputText: str
    checkboxState: bool

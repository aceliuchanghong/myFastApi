from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional, List, Union

import jwt
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from fastapi import APIRouter, Path, Query, Body, Cookie, Header, Depends
from starlette.exceptions import HTTPException
from starlette.status import *

from fastapi.security import OAuth2PasswordBearer

from backend_prd.api.models.others import Token

router2 = APIRouter()


# 第一节:hello world
@router2.get('/test/helloworld')
async def helloworld():
    return {'message': 'hello world'}


# 第二节:路径参数
@router2.get('/test/user1/{user_id}')
async def get_user1(user_id):
    return {'user': f'hello world {user_id}'}


# 2.1增加参数限制
@router2.get('/test/user2/{user_id}')
async def get_user2(user_id: int):
    return {'user': f'hello world {user_id}'}


# 2.2增加选项
class Gender(str, Enum):
    male = "male"
    female = "female"


@router2.get('/test/user3/{gender}')
async def get_user3(gender: Gender):
    return {'user': f'hello world {gender.value}'}


# 第三节:查询参数(设置默认值)
@router2.get('/test/info1')
async def get_info1(user_id: int, page_num: Optional[int] = 10):
    # http://127.0.0.1:8000/test/info1?user_id=2&page_num=3
    return {'info': f'{page_num} hello world {user_id}'}


# 3.1混合使用
@router2.get('/test/{user_id}/info2')
async def get_info2(user_id: int, page_num: Optional[int] = 10):
    # http://127.0.0.1:8000/test/22222/info2?page_num=99
    return {'info': f'{page_num} hello world {user_id} 2 '}


# 第四节:请求体
# post-增加 put-修改 delete-删除 patch
class UserModel(BaseModel):
    username: str = Field(..., min_length=2, examples=["liu"])
    description: Optional[str] = "nothing"
    money: Optional[str] = Field("QAQ", max_length=16)
    feature: List[str] = []


@router2.post('/test/body1/{o_id}')
async def post_body1(o_id: int, user_model: UserModel):
    print({'info': f'{user_model.username} hello world {user_model.description}'})
    ans = user_model.model_dump()
    ans.update({'id': f'666 {o_id}'})
    return ans


# 第五节:路径参数的校验
@router2.get('/test/user4/{user_id}')
async def get_user4(user_id: int = Path(..., title="id", ge=0, le=1000)):
    return {'user': f'hello world 4 {user_id}'}


# 5.1查询参数的校验
@router2.get('/test/user5')
async def get_user5(user_id: int = Query(666, alias='user-id', title="喵喵喵", ge=0, le=1000)):
    return {'user': f'hello world 5 {user_id}'}


# 第六节:请求体深入-校验
@router2.post('/test/body2/{o_id}')
async def post_body2(o_id: int, user_model: UserModel, o_id2: int = Body(..., ge=2)):
    ans = {
        "username": user_model.username,
        "description": user_model.description,
        "money": user_model.money,
        "o_id": o_id,
        "o_id2": o_id2
    }
    return ans


# 第八节:Cookie和header
@router2.put('/test/cookie_header')
async def post_cookie_header(*,
                             favorite_schema: Optional[str] = Cookie(None, alias="favorite-schema"),
                             api_token: Union[str, None] = Header(None, alias="api-token")
                             ):
    ans = {
        "favorite_schema": favorite_schema,
        "api_token": api_token
    }
    return ans


# 第九节:响应模型
@router2.get('/test/response_body/{username}', response_model=UserModel)
async def get_response_body(username: str):
    ans = UserModel(username=username, feature=[])
    return ans


# 第十节:状态码和异常

# 第十一节:依赖注入
async def run_fun(words: Optional[str] = "hello"):
    return words + " ll"


@router2.get('/test/get_item')
async def get_item2(item_info: str = Depends(run_fun)):
    return {"item_info": item_info}


# 第十二节:api身份认证
"""
client-->login-->API
"""

SECURITY_KEY = "rvsvwAiA2mHPIhxvS_hn5blQwcf5WctVwOaFLoqSjLI"
ALGORITHMS = "HS256"
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/test/token")


async def test_validate_user(username, password):
    if username == "liu" and password == "aaa":
        return username
    return None


async def test_get_user(token: str = Depends(oauth2_schema)):
    unauth = HTTPException(HTTP_401_UNAUTHORIZED, detail="未授权")
    try:
        username = None
        token_data = jwt.decode(token, SECURITY_KEY, ALGORITHMS)
        if token_data:
            current_time = datetime.now(timezone.utc)
            exp = datetime.fromtimestamp(token_data.get("exp"), timezone.utc)
            if current_time >= exp:
                raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token 已过期")
            username = token_data.get("username", None)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token 已过期")
    except Exception as error:
        raise unauth from error
    if not username:
        raise unauth
    return username


@router2.post('/test/token')
async def test_login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = await test_validate_user(form_data.username, form_data.password)
    if not username:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="账号或者密码错误",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    token_expire = datetime.now(timezone.utc) + timedelta(minutes=300)
    token_data = {
        "username": username,
        "exp": token_expire
    }
    token = jwt.encode(token_data, SECURITY_KEY, algorithm=ALGORITHMS)
    return Token(access_token=token, token_type="bearer")


@router2.get('/test/pass_token')
async def pass_token(username: str = Depends(test_get_user)):
    return {"item_info": username}

# 第十三节:api身份认证
# 第十四节:api身份认证
# 第十五节:api身份认证
# 第十六节:api身份认证

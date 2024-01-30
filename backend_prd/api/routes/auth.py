from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

auth_router = APIRouter()

security = HTTPBasic()


@auth_router.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    # 用户登录逻辑
    return {"message": "Login successful"}


@auth_router.post("/register")
def register(username: str, password: str):
    # 用户注册逻辑
    return {"message": "User registered successfully"}

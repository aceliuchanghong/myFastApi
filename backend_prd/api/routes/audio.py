import os

from fastapi import APIRouter, Request, UploadFile, Form, File

from backend_prd.api.schemas import task_insert_sql
from backend_prd.core.database import execute_sqlite_sql
from utils.path_valid import validate_output_path

router = APIRouter()


@router.get("/")
def get_audio_list():
    # 获取音频列表的逻辑
    return {"message": "Get audio list"}


@router.post("/")
def upload_audio():
    # 处理上传音频的逻辑
    return {"message": "Upload audio"}


@router.get("/{audio_id}")
def get_audio(audio_id: int):
    # 获取特定音频的逻辑
    return {"message": f"Get audio {audio_id}"}


@router.put("/{audio_id}")
def update_audio(audio_id: int):
    # 更新特定音频的逻辑
    return {"message": f"Update audio {audio_id}"}


@router.delete("/{audio_id}")
def delete_audio(audio_id: int):
    # 删除特定音频的逻辑
    return {"message": f"Delete audio {audio_id}"}


@router.post("/fix")
async def process_info(request: Request, file: UploadFile = File(...), input_task_name: str = Form(...),
                       input_user_name: str = Form(...),
                       radio_value: str = Form(...), checkbox_value: bool = Form(...)):
    # 创建文件路径
    directory = f"testfiles/{input_user_name}/{input_task_name}"
    # 确保目录存在
    validate_output_path(directory)
    basename, extension = os.path.splitext(file.filename)
    # 拼接完整的文件路径
    file_location = os.path.join(directory, file.filename)

    print(radio_value, checkbox_value)
    print(basename, extension)
    with open(file_location, "wb+") as file_object:
        file_content = await file.read()  # 使用await来异步读取文件
        file_object.write(file_content)
    execute_sqlite_sql(task_insert_sql, params=(
        input_user_name, 'audio', input_task_name, input_task_name, 'SUC', '0', 'last_modify_time', 'remark'),
                       should_log=True)

    print({"message": "Upload successful"})

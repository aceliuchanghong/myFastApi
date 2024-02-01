import os

from fastapi import APIRouter, Request, UploadFile, Form, File
from fastapi.responses import HTMLResponse, JSONResponse

from utils.path_valid import validate_output_path

router = APIRouter()


@router.get("/")
def get_image_list():
    return {"message": "Get image list"}


@router.post("/")
def upload_image():
    return {"message": "Upload image"}


@router.get("/{image_id}")
def get_image(image_id: int):
    return {"message": f"Get image {image_id}"}


@router.put("/{image_id}")
def update_image(image_id: int):
    return {"message": f"Update image {image_id}"}


@router.delete("/{image_id}")
def delete_image(image_id: int):
    return {"message": f"Delete image {image_id}"}


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

    print({"message": "Upload successful"})

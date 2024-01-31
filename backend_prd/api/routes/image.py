from fastapi import APIRouter, Request, UploadFile, Form, File
from fastapi.responses import HTMLResponse, JSONResponse

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

    file_location = f"testfiles/{input_user_name}/{input_task_name}/name"
    print(radio_value, checkbox_value)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.read())

    print({"message": "Upload successful"})
    return JSONResponse(content={"redirect": "/Pages/Task"})

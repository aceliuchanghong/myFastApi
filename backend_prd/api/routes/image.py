from fastapi import APIRouter

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

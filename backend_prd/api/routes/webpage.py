from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_page_list():
    return {"message": "Get page list"}


@router.post("/")
def upload_page():
    return {"message": "Upload page"}


@router.get("/{page_id}")
def get_page(page_id: int):
    return {"message": f"Get page {page_id}"}


@router.put("/{page_id}")
def update_page(page_id: int):
    return {"message": f"Update page {page_id}"}


@router.delete("/{page_id}")
def delete_page(page_id: int):
    return {"message": f"Delete page {page_id}"}

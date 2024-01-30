from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_video_list():
    return {"message": "Get video list"}


@router.post("/")
def upload_video():
    return {"message": "Upload video"}


@router.get("/{video_id}")
def get_video(video_id: int):
    return {"message": f"Get video {video_id}"}


@router.put("/{video_id}")
def update_video(video_id: int):
    return {"message": f"Update video {video_id}"}


@router.delete("/{video_id}")
def delete_video(video_id: int):
    return {"message": f"Delete video {video_id}"}

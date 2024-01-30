from fastapi import APIRouter

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

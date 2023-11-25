from fastapi import APIRouter, Depends, Body, HTTPException, UploadFile, File
from dependency_injector.wiring import Provide, inject
from starlette import status
import json

from apps.news.command import PostCommandUseCase
from apps.shared_kernel.container import AppContainer
from apps.news import schema as post_schema


router = APIRouter(prefix="/posts")

# TODO: 관리자 계정에 대해서만 접근 가능하도록 처리
@router.post("/news/upload", response_model=list[post_schema.CreatePostResponse])
@inject
async def post_news_upload(
    files: list[UploadFile] = File(...),
    # current_user: str = Depends(get_current_user),
    post_command: PostCommandUseCase = Depends(Provide[AppContainer.post.post_command]),
) -> None:
    for file in files:
        content = await file.read()
        try:
            data = json.loads(content)
            ret = []
            for post in data:
                new_post = post_command.create_post(request=post)
                ret.append({"id": new_post.id, "title": new_post.title})

        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON format in file")
    return ret

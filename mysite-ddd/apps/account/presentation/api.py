from fastapi import Depends, FastAPI, HTTPException
from typing import List
from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject
from apps.account.presentation.request import GetUserRequest
from apps.account.presentation.response import UserResponse, UserSchema
from apps.account.domain.entity.user import User
from apps.account.application.use_case.query import AccountQueryUseCase

from project.infra.database.connection import SessionFactory, engine, get_db_session
from project.infra.container import AppContainer

router = APIRouter(prefix="/users")

@router.get("/")
@inject
def get_users(
    request: GetUserRequest = Depends(),
    account_query: AccountQueryUseCase = Depends(Provide[AppContainer.account.query]),
) -> UserResponse:
    users: List[User] = account_query.get_users()
    return UserResponse(
        detail="ok",
        result=[UserSchema.from_orm(user) for user in users]
    )

# @router.post("/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# @router.get("/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db_session)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.post("/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db_session)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
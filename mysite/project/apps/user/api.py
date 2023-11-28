from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from apps.user import repository, schema
from apps.database import connection
from apps.user.query import UserQueryUseCase, oauth2_scheme, SECRET_KEY, ALGORITHM
from apps.user.command import UserCommandUseCase
from apps.user.exception import InvalidTokenException, WrongLoginInfoUserException
from apps.shared_kernel.container import AppContainer


router = APIRouter(prefix="/users")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(connection.get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
    except JWTError:
        raise InvalidTokenException
    else:
        if email is None:
            raise InvalidTokenException
        user = repository.get_user_by_email(db, email=email)
        if user is None:
            raise InvalidTokenException
        return user

@router.post(
    "/",
    response_model=schema.UserSchema,
    status_code=status.HTTP_201_CREATED,
)
@inject
def post_users(
    request: schema.CreateUserRequest,
    user_command: UserCommandUseCase = Depends(Provide[AppContainer.user.user_command]),
):
    new_user =  user_command.create_user(request=request)
    return new_user

@router.post(
    "/login",
    response_model=schema.TokenSchema,
)
@inject
def login_for_access_token(
    request: schema.LoginUser,
    user_query: UserQueryUseCase = Depends(Provide[AppContainer.user.user_query]),
) -> schema.TokenSchema:

    token_schema = user_query.get_token_schema(request)
    return token_schema
from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from apps.user import repository, schema
from apps.database import connection
from apps.user.query import UserQueryUseCase, oauth2_scheme, SECRET_KEY, ALGORITHM
from apps.user.command import UserCommandUseCase
from apps.user.exception import InvalidTokenException
from apps.shared_kernel.container import AppContainer


router = APIRouter(prefix="/users")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(connection.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = repository.get_user_by_email(db, email=email)
        if user is None:
            raise credentials_exception
        return user

@router.post(
    "/",
    response_model=schema.UserSchema,
)
@inject
def post_users(
    request: schema.CreateUserRequest,
    user_command: UserCommandUseCase = Depends(Provide[AppContainer.user.user_command]),
):
    new_user =  user_command.create_user(request=request)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
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

    try:
        token_schema = user_query.get_token_schema(request)
    except InvalidTokenException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_schema
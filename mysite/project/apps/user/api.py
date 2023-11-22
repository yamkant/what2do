from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from apps.user import repository, schema
from apps.database import orm, connection
from apps.user.command import UserCommandUseCase
from apps.shared_kernel.container import AppContainer

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

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

@router.get("/")
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(connection.get_db),
):
    users = repository.get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT
)
@inject
def post_users(
    request: schema.CreateUserRequest,
    user_command: UserCommandUseCase = Depends(Provide[AppContainer.user.user_command]),
) -> None:
    new_user =  user_command.create_user(request=request)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")

@router.post(
    "/login",
    response_model=schema.Token,
)
def login_for_access_token(
    login_user: schema.LoginUser,
    db: Session = Depends(connection.get_db)
):

    # check user and password
    user = repository.get_user_by_email(db, login_user.email)
    if not user or not repository.pwd_context.verify(login_user.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": user.email
    }
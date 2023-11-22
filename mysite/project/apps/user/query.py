from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from typing import Callable, ContextManager, List
from passlib.context import CryptContext
from jose import JWTError, jwt

from apps.user.repository import UserRDBRepository
from apps.user.exception import InvalidTokenException
from fastapi.security import OAuth2PasswordBearer
from apps.database import orm
from apps.user import schema

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

class UserQueryUseCase:
    def __init__(
        self,
        user_repo: UserRDBRepository,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.user_repo = user_repo
        self.db_session = db_session
    
    def get_user(
        self,
        email: str
    ) -> orm.User:
        with self.db_session() as session:
            user = session.query(orm.User).filter(orm.User.email == email).first()
        return user

    def get_token_schema(
        self,
        request: schema.LoginUser,
    ) -> schema.TokenSchema:
        user = self.get_user(request.email)
        if not user or not pwd_context.verify(request.password, user.hashed_password):
            raise InvalidTokenException()

        data = {
            "sub": user.email,
            "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        }
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "email": user.email,
        }
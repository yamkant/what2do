from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware

from apps.database.config import config
from apps.shared_kernel.container import AppContainer
from apps.shared_kernel.exception import CustomException

from apps.user.api import router as user_router
from apps.todo.api import router as todo_router
from apps.post.api import router as post_router

from apps.database.connection import engine
from apps.database.orm import Base

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://www.devyam.net:3000",
]

def init_routers(app_: FastAPI) -> None:
    app_.include_router(user_router)
    app_.include_router(todo_router)
    app_.include_router(post_router)

def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    return middleware


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={
                "error_code": exc.error_code,
                "message": exc.message,
            }
        )

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="What2Do",
        description="What2D API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        middleware=make_middleware()
    )
    app_.container = AppContainer()
    init_routers(app_)
    init_listeners(app_)
    return app_

app = create_app()
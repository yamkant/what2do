from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from apps.shared_kernel.container import AppContainer
from apps.shared_kernel.exception import CustomException

from apps.user.api import router as user_router
from apps.todo.api import router as todo_router
from apps.post.api import router as post_router

from apps.database.connection import engine
from apps.database.orm import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app_container = AppContainer()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://www.devyam.net:3000",
]

app.container = app_container

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(todo_router)
app.include_router(post_router)

@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.code,
        content={
            "error_code": exc.error_code,
            "message": exc.message,
        }
    )

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
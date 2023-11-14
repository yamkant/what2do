from fastapi import FastAPI

from apps.account.presentation import api as user_router
from project.infra.database.orm import init_orm_mappers
from project.infra.container import AppContainer

app_container = AppContainer()

app = FastAPI()

app.container = app_container
app.include_router(user_router.router)

init_orm_mappers()

@app.get("/")
def health_check():
    return {"ping": "pong"}

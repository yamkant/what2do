from fastapi import FastAPI
from apps.sql_app import database, orm

# from apps import todos, users
from apps.users import api as user_router
from apps.sql_app.orm import init_orm_mappers
from project.container import AppContainer

app_container = AppContainer()

app = FastAPI()

app.container = app_container
app.include_router(user_router.router)

init_orm_mappers()
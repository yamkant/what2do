from fastapi import FastAPI
from apps.sql_app import models, database

# from apps import todos, users
from apps.users import router as user_router

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.include_router(user_router.router)
# app.include_router(items.router)
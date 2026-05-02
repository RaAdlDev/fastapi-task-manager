from routers import tasks, users_auth
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.connection import engine
from database.models import Base
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield

app = FastAPI(
    lifespan=lifespan,
    title="To-DoListo API",
    description="API for tasks gestion",
    version="1.0.0")
app.include_router(tasks.router)
app.include_router(users_auth.router)
@app.get("/")
async def root():
    return {"return": "Hello To-DoListo"}
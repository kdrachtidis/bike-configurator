import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlmodel import SQLModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

import os
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','.env'))
load_dotenv(env_path)
print("DATABASE_URL:", os.environ.get("DATABASE_URL"))

from src.utils.database import create_db_and_tables
from src.utils import web
from src.views import biketype as biketype
from src.views import assemblygroup as assemblygroup
from src.views import assemblygroupmodule as assemblygroupmodule
from src.views import bikecomponent as bikecomponent
from src.views import user as auth

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, title="Bike configurator")
    app.include_router(web.router)
    app.include_router(biketype.router, prefix="/api")
    app.include_router(assemblygroup.router, prefix="/api")
    app.include_router(assemblygroupmodule.router, prefix="/api")
    app.include_router(bikecomponent.router, prefix="/api")
    app.include_router(auth.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
    return app


app = get_app()


@app.middleware("http")
async def create_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cookie",
                        value="Bike Configurator")
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlmodel import SQLModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.api.utils.database import create_db_and_tables
from app.api.utils import web
from app.api.public.biketype import views as biketype
from app.api.public.biketype.content import create_BikeTypes
from app.api.public.assemblygroup import views as assemblygroup
from app.api.public.assemblygroup.content import create_AssemblyGroups
from app.api.public.assemblygroupmodule import views as assemblygroupmodule
from app.api.public.assemblygroupmodule.content import create_AssemblyGroupModules
from app.api.public.bikecomponent import views as bikecomponent
from app.api.public.bikecomponent.content import create_BikeComponents
from app.api.auth import views as auth

import os
from dotenv import load_dotenv

load_dotenv('.env')

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_BikeTypes()
    create_AssemblyGroups()
    create_AssemblyGroupModules()
    create_BikeComponents()
    yield


def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, title="Bike configurator")
    app.include_router(web.router)
    app.include_router(biketype.router, prefix="/app/api")
    app.include_router(assemblygroup.router, prefix="/app/api")
    app.include_router(assemblygroupmodule.router, prefix="/app/api")
    app.include_router(bikecomponent.router, prefix="/app/api")
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

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import engine
from routers import assemblygroupmodules, assemblygroups, components, web, auth, biketypes

app = FastAPI(title="Bike configurator")
app.include_router(web.router)
app.include_router(biketypes.router, prefix="/api")
app.include_router(assemblygroups.router, prefix="/api")
app.include_router(assemblygroupmodules.router, prefix="/api")
app.include_router(components.router)
app.include_router(auth.router)


origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie",
                        value="you_visited_the_carsharing_app")
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

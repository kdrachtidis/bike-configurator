from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "gasoline",
        "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline",
        "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "diesel", "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"}
]


@app.get("/api/biketypes")
def get_types():
    return db


@app.get("/api/biketypes/{id}")
def biketype_by_id(id: int) -> dict:
    result = [biketype for biketype in db if biketype['id'] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike type with id={id}.")


if __name__ == "__main__":
    uvicorn.run("configurator:app", reload=True)

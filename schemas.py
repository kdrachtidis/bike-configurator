import json

from pydantic import BaseModel


class CarInput(BaseModel):
    id: int
    size: str
    fuel: str
    doors: int
    transmission: str

def load_db() -> list[CarOutput]:
    with open("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]

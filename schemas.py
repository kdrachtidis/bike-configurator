from sqlmodel import SQLModel, Field


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

    class Config:
        schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel": "hybrid"
            }
        }

class Car(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)

class CarOutput(CarInput):
    id: int
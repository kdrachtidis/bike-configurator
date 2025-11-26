from sqlmodel import SQLModel, Field, Relationship

from src.models.links import TypesToComponents


class BikeTypeInput(SQLModel):
    name: str | None = "No name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "Rennrad"
            }]
        }
    }


class BikeType(BikeTypeInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    bikecomponents: list["BikeComponent"] = Relationship(
        back_populates="biketypes", link_model=TypesToComponents)


class BikeTypeOutput(BikeTypeInput):
    id: int
    bikecomponents: list

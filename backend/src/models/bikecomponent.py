from sqlmodel import SQLModel, Field, Relationship

from src.models.links import TypesToComponents, ComponentsToParts


class BikeComponentInput(SQLModel):
    name: str | None = "No bike component name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "A bike component name"
            }]
        }
    }


class BikeComponent(BikeComponentInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    biketypes: list["BikeType"] = Relationship(
        back_populates="bikecomponents", link_model=TypesToComponents
    )
    bikeparts: list["BikePart"] = Relationship(
        back_populates="bikecomponents", link_model=ComponentsToParts
    )


class BikeComponentOutput(BikeComponentInput):
    id: int
    biketypes: list
    bikeparts: list

from sqlmodel import SQLModel, Field, Relationship

from src.models.links import ComponentsToParts, PartsToProducts

# Bike Part Models
class BikePartInput(SQLModel): # Input model for creating/updating bike parts
    name: str | None = "No bike part name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "A bike part name"
            }]
        }
    }


class BikePart(BikePartInput, table=True): # Database model for bike parts
    id: int | None = Field(default=None, primary_key=True)
    bikecomponents: list["BikeComponent"] = Relationship(
        back_populates="bikeparts", link_model=ComponentsToParts
    )
    bikeproducts: list["BikeProduct"] = Relationship(
        back_populates="bikeparts", link_model=PartsToProducts
    )


class BikePartOutput(BikePartInput): # Output model for bike parts
    id: int
    bikecomponents: list
    bikeproducts: list

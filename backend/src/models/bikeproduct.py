from sqlmodel import SQLModel, Field, Relationship

from src.models.links import PartsToProducts


class BikeProductInput(SQLModel): # Input model for creating/updating bike products
    name: str | None = "No bike product name"
    source: str | None = "Unknown"
    price: float | None = 0.00
    group: str | None = "No group"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "SHIMANO 105 KURBELGARNITUR FC-R7000 HOLLOWTECH II",
                "source": "bike-components.de",
                "price": 100.00,
                "group": "Drivetrain"
            }]
        }
    }


class BikeProduct(BikeProductInput, table=True): # Database model for bike products
    id: int | None = Field(default=None, primary_key=True)
    bikeparts: list["BikePart"] = Relationship(
        back_populates="bikeproducts", link_model=PartsToProducts
    )


class BikeProductOutput(BikeProductInput): # Output model for bike products
    id: int
    bikeparts: list

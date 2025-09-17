from sqlmodel import SQLModel, Field, Relationship

from src.models.links import ModulesToComponents


class BikeComponentInput(SQLModel):
    name: str | None = "No name"
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


class BikeComponent(BikeComponentInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    assemblygroupmodules: list["AssemblyGroupModule"] = Relationship(
        back_populates="bikecomponents", link_model=ModulesToComponents
    )


class BikeComponentOutput(BikeComponentInput):
    id: int
    assemblygroupmodules: list

from sqlmodel import SQLModel, Field, Relationship

from api.utils.link_models import TypesToGroups


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
    assemblygroups: list["AssemblyGroup"] = Relationship(
        back_populates="biketypes", link_model=TypesToGroups)


class BikeTypeOutput(BikeTypeInput):
    id: int
    assemblygroups: list

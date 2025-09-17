from sqlmodel import SQLModel, Field, Relationship

from src.models.links import TypesToGroups, GroupsToModules


class AssemblyGroupInput(SQLModel):
    name: str | None = "No name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "TestGroup"
            }]
        }
    }


class AssemblyGroup(AssemblyGroupInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    biketypes: list["BikeType"] = Relationship(
        back_populates="assemblygroups", link_model=TypesToGroups
    )
    assemblygroupmodules: list["AssemblyGroupModule"] = Relationship(
        back_populates="assemblygroups", link_model=GroupsToModules
    )


class AssemblyGroupOutput(AssemblyGroupInput):
    id: int
    biketypes: list
    assemblygroupmodules: list

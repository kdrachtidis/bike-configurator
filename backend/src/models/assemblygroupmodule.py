from sqlmodel import SQLModel, Field, Relationship

from src.models.links import GroupsToModules, ModulesToComponents


class AssemblyGroupModuleInput(SQLModel):
    name: str | None = "No Name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "TestModule"
            }]
        }
    }


class AssemblyGroupModule(AssemblyGroupModuleInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    assemblygroups: list["AssemblyGroup"] = Relationship(
        back_populates="assemblygroupmodules", link_model=GroupsToModules
    )
    bikecomponents: list["BikeComponent"] = Relationship(
        back_populates="assemblygroupmodules", link_model=ModulesToComponents
    )


class AssemblyGroupModuleOutput(AssemblyGroupModuleInput):
    id: int
    assemblygroups: list
    bikecomponents: list

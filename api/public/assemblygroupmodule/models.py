from sqlmodel import SQLModel, Field, Relationship

from schemas import GroupsToModules

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
        back_populates="assemblygroupmodules", link_model=GroupsToModules)


class AssemblyGroupModuleOutput(AssemblyGroupModuleInput):
    id: int
    assemblygroups: list

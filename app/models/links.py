from sqlmodel import SQLModel, Field


class GroupsToModules(SQLModel, table=True):
    group_id: int | None = Field(
        default=None, foreign_key="assemblygroup.id", primary_key=True
    )
    modude_id: int | None = Field(
        default=None, foreign_key="assemblygroupmodule.id", primary_key=True
    )


class TypesToGroups(SQLModel, table=True):
    type_id: int | None = Field(
        default=None, foreign_key="biketype.id", primary_key=True
    )
    group_id: int | None = Field(
        default=None, foreign_key="assemblygroup.id", primary_key=True
    )


class ModulesToComponents(SQLModel, table=True):
    module_id: int | None = Field(
        default=None, foreign_key="assemblygroupmodule.id", primary_key=True
    )
    component_id: int | None = Field(
        default=None, foreign_key="bikecomponent.id", primary_key=True
    )

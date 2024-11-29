from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

# Users -----------------------------------------------


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(
        "username", VARCHAR, unique=True, index=True))
    password_hash: str = ""

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class UserOutput(SQLModel):
    id: int
    username: str

# Links ------------------------------------------


class GroupsToModules(SQLModel, table=True):
    group_id: int | None = Field(
        default=None, foreign_key="assemblygroup.id", primary_key=True)
    modude_id: int | None = Field(
        default=None, foreign_key="assemblygroupmodule.id", primary_key=True)


class TypesToGroups(SQLModel, table=True):
    type_id: int | None = Field(
        default=None, foreign_key="biketype.id", primary_key=True)
    group_id: int | None = Field(
        default=None, foreign_key="assemblygroup.id", primary_key=True)

# Module -----------------------------------------


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
    assemblygroup: "AssemblyGroup" = Relationship(
        back_populates="assemblygroupmodules", link_model=GroupsToModules)


class AssemblyGroupModuleOutput(AssemblyGroupModuleInput):
    id: int
    assemblygroup: "AssemblyGroupOutput"

# Assembly Group --------------------------------------


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
    biketype: "BikeType" = Relationship(
        back_populates="assemblygroups", link_model=TypesToGroups)
    assemblygroupmodules: list[AssemblyGroupModule] = Relationship(
        back_populates="assemblygroup", link_model=GroupsToModules)


class AssemblyGroupOutput(AssemblyGroupInput):
    id: int
    biketype: "BikeTypeOutput"
    assemblygroupmodules: list[AssemblyGroupModuleOutput] = []

# Bike Type --------------------------------------


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
    assemblygroups: list[AssemblyGroup] = Relationship(
        back_populates="biketype", link_model=TypesToGroups)


class BikeTypeOutput(BikeTypeInput):
    id: int
    assemblygroups: list[AssemblyGroupOutput] = []


# Bike Component --------------------------------------


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
    id: int | None = Field(primary_key=True, default=None)


class BikeComponentOutput(BikeComponentInput):
    id: int

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


class TypesToGroups(SQLModel, table=True):
    type_id: int | None = Field(
        default=None, foreign_key="biketype.id", primary_key=True)
    group_id: int | None = Field(
        default=None, foreign_key="assemblygroup.id", primary_key=True)


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
    biketypes: list["BikeType"] = Relationship(
        back_populates="assemblygroups", link_model=TypesToGroups)


class AssemblyGroupOutput(AssemblyGroupInput):
    id: int
    biketypes: list

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
        back_populates="biketypes", link_model=TypesToGroups)


class BikeTypeOutput(BikeTypeInput):
    id: int
    assemblygroups: list

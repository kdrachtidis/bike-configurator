from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class UserOutput(SQLModel):
    id: int
    username: str


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(
        "username", VARCHAR, unique=True, index=True))
    password_hash: str = ""

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

# Module -----------------------------------------


class AssemblyGroupModuleInput(SQLModel):
    modulename: str | None = "No name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "modulename": "Brake Levers"
            }]
        }
    }


class AssemblyGroupModuleOutput(AssemblyGroupModuleInput):
    id: int


class AssemblyGroupModule(AssemblyGroupModuleInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    assemblygroup_id: int = Field(foreign_key="assemblygroup.id")
    assemblygroup: "AssemblyGroup" = Relationship(
        back_populates="groupmodules")


# Assembly Group --------------------------------------


class AssemblyGroupInput(SQLModel):
    name: str | None = "No name"
    #biketype: str | None = "No type"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "Cockpit",
                "biketype": "Road"
            }]
        }
    }


class AssemblyGroup(AssemblyGroupInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    groupmodules: list[AssemblyGroupModule] = Relationship(
        back_populates="assemblygroup")


class AssemblyGroupOutput(AssemblyGroupInput):
    id: int
    groupmodules: list[AssemblyGroupModuleOutput] = []


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

# Test Object -------------------------------------------


class TestObjectInput(SQLModel):
    name: str | None = "No name"

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "Test"
            }]
        }
    }


class TestObjectOutput(TestObjectInput):
    id: int


class TestObject(TestObjectInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    biketype_id: int = Field(foreign_key="biketype.id")
    biketype: "BikeType" = Relationship(back_populates="groups")

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
    groups: list[TestObject] = Relationship(back_populates="biketype")


class BikeTypeOutput(BikeTypeInput):
    id: int
    groups: list[TestObjectOutput] = []

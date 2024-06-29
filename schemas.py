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


class ModuleInput(SQLModel):
    name: str


class Module(ModuleInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    #bikecomponent_id: int = Field(foreign_key="assemblygroup.id")
    #bikecomponent: "AssemblyGroup" = Relationship(back_populates="trips")


class ModuleOutput(ModuleInput):
    id: int

# Assembly Group --------------------------------------


class AssemblyGroupInput(SQLModel):
    name: str | None = "No name"

    class GroupConfig:
        schema_extra = {
            "example": {
                "name": "Cockpit"
            }
        }


class AssemblyGroup(AssemblyGroupInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    #trips: list[Module] = Relationship(back_populates="module")


class AssemblyGroupOutput(AssemblyGroupInput):
    id: int
    #trips: list[ModuleOutput] = []


# Bike Component --------------------------------------

class BikeComponentInput(SQLModel):
    name: str | None = "No name"
    source: str | None = "Unknown"
    price: float | None = 0.00
    group: str | None = "No group"

    class Config:
        schema_extra = {
            "example": {
                "name": "SHIMANO 105 KURBELGARNITUR FC-R7000 HOLLOWTECH II",
                "source": "bike-components.de",
                "price": 100.00,
                "group": "Drivetrain"
            }
        }


class BikeComponent(BikeComponentInput, table=True):
    id: int | None = Field(primary_key=True, default=None)


class BikeComponentOutput(BikeComponentInput):
    id: int

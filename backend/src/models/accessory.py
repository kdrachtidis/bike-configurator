from sqlmodel import Field, Relationship, SQLModel

from src.models.links import AccessoryTypesToProducts


class AccessoryCategoryInput(SQLModel):
    name: str


class AccessoryCategory(AccessoryCategoryInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    accessory_types: list["AccessoryType"] = Relationship(back_populates="category")


class AccessoryCategoryOutput(AccessoryCategoryInput):
    id: int


class AccessoryTypeInput(SQLModel):
    name: str


class AccessoryType(AccessoryTypeInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="accessorycategory.id")
    category: AccessoryCategory = Relationship(back_populates="accessory_types")
    bikeproducts: list["BikeProduct"] = Relationship(
        back_populates="accessory_types", link_model=AccessoryTypesToProducts
    )


class AccessoryTypeOutput(AccessoryTypeInput):
    id: int
    category_id: int


class AccessoryProductOutput(SQLModel):
    id: int
    name: str | None
    source: str | None
    price: float | None

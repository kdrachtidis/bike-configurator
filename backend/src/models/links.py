from sqlmodel import SQLModel, Field


class ComponentsToParts(SQLModel, table=True):
    component_id: int | None = Field(
        default=None, foreign_key="bikecomponent.id", primary_key=True
    )
    part_id: int | None = Field(
        default=None, foreign_key="bikepart.id", primary_key=True
    )


class TypesToComponents(SQLModel, table=True):
    type_id: int | None = Field(
        default=None, foreign_key="biketype.id", primary_key=True
    )
    component_id: int | None = Field(
        default=None, foreign_key="bikecomponent.id", primary_key=True
    )


class PartsToProducts(SQLModel, table=True):
    part_id: int | None = Field(
        default=None, foreign_key="bikepart.id", primary_key=True
    )
    product_id: int | None = Field(
        default=None, foreign_key="bikeproduct.id", primary_key=True
    )

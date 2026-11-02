import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine

import src.models
from src.crud.accessory import (
    create_accessory_category,
    create_accessory_product,
    create_accessory_type,
    read_accessory_categories,
    read_accessory_products,
    read_accessory_types,
)
from src.models.accessory import AccessoryCategoryInput, AccessoryTypeInput
from src.models.bikeproduct import BikeProductInput


@pytest.fixture
def session():
    engine = create_engine("sqlite://")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as db_session:
        yield db_session


def test_accessory_hierarchy_reuses_bike_products(session):
    category = create_accessory_category(
        AccessoryCategoryInput(name="Lighting"), session
    )
    accessory_type = create_accessory_type(
        category.id, AccessoryTypeInput(name="Front light"), session
    )
    product = create_accessory_product(
        accessory_type.id,
        BikeProductInput(name="Front light", source="Shop", price=25.5),
        session,
    )

    assert read_accessory_categories(session) == [category]
    assert read_accessory_types(category.id, session) == [accessory_type]
    assert read_accessory_products(accessory_type.id, session) == [product]
    assert product.accessory_types == [accessory_type]


def test_read_accessory_types_requires_existing_category(session):
    with pytest.raises(HTTPException) as error:
        read_accessory_types(999, session)

    assert error.value.status_code == 404


def test_create_accessory_product_requires_existing_type(session):
    with pytest.raises(HTTPException) as error:
        create_accessory_product(
            999, BikeProductInput(name="Light"), session
        )

    assert error.value.status_code == 404

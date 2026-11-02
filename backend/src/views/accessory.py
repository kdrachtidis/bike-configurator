from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from src.crud.accessory import (
    create_accessory_category,
    create_accessory_product,
    create_accessory_type,
    read_accessory_categories,
    read_accessory_products,
    read_accessory_types,
)
from src.models.accessory import (
    AccessoryCategory,
    AccessoryCategoryInput,
    AccessoryCategoryOutput,
    AccessoryProductOutput,
    AccessoryType,
    AccessoryTypeInput,
    AccessoryTypeOutput,
)
from src.models.bikeproduct import BikeProductInput
from src.models.bikeproduct import BikeProduct
from src.utils.database import get_session
from src.models.user import User
from src.views.user import get_current_user

router = APIRouter(tags=["Accessories"])
SessionDependency = Annotated[Session, Depends(get_session)]


@router.get("/accessory-categories/", response_model=list[AccessoryCategoryOutput])
def get_accessory_categories(session: SessionDependency) -> list[AccessoryCategory]:
    return read_accessory_categories(session)


@router.post(
    "/accessory-categories/",
    response_model=AccessoryCategoryOutput,
    status_code=status.HTTP_201_CREATED,
)
def post_accessory_category(
    input: AccessoryCategoryInput,
    session: SessionDependency,
    user: User = Depends(get_current_user),
) -> AccessoryCategory:
    return create_accessory_category(input, session)


@router.get(
    "/accessory-categories/{category_id}/accessory-types/",
    response_model=list[AccessoryTypeOutput],
)
def get_accessory_types(category_id: int, session: SessionDependency) -> list[AccessoryType]:
    return read_accessory_types(category_id, session)


@router.post(
    "/accessory-categories/{category_id}/accessory-types/",
    response_model=AccessoryTypeOutput,
    status_code=status.HTTP_201_CREATED,
)
def post_accessory_type(
    category_id: int,
    input: AccessoryTypeInput,
    session: SessionDependency,
    user: User = Depends(get_current_user),
) -> AccessoryType:
    return create_accessory_type(category_id, input, session)


@router.get(
    "/accessory-types/{accessory_type_id}/bikeproducts/",
    response_model=list[AccessoryProductOutput],
)
def get_accessory_products(
    accessory_type_id: int, session: SessionDependency
) -> list:
    return read_accessory_products(accessory_type_id, session)


@router.post(
    "/accessory-types/{accessory_type_id}/bikeproducts/",
    response_model=AccessoryProductOutput,
    status_code=status.HTTP_201_CREATED,
)
def post_accessory_product(
    accessory_type_id: int,
    input: BikeProductInput,
    session: SessionDependency,
    user: User = Depends(get_current_user),
) -> BikeProduct:
    return create_accessory_product(accessory_type_id, input, session)

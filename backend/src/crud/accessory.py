from fastapi import HTTPException
from sqlmodel import Session, select

from src.models.accessory import AccessoryCategory, AccessoryCategoryInput, AccessoryType, AccessoryTypeInput
from src.models.bikeproduct import BikeProduct, BikeProductInput


def read_accessory_categories(session: Session) -> list[AccessoryCategory]:
    return list(session.exec(select(AccessoryCategory).order_by(AccessoryCategory.id)).all())


def create_accessory_category(input: AccessoryCategoryInput, session: Session) -> AccessoryCategory:
    category = AccessoryCategory(name=input.name.strip())
    if not category.name:
        raise HTTPException(status_code=422, detail="Category name cannot be empty")
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def read_accessory_types(category_id: int, session: Session) -> list[AccessoryType]:
    category = session.get(AccessoryCategory, category_id)
    if not category:
        raise HTTPException(status_code=404, detail=f"Accessory category {category_id} not found")
    return list(session.exec(
        select(AccessoryType)
        .where(AccessoryType.category_id == category_id)
        .order_by(AccessoryType.id)
    ).all())


def create_accessory_type(
    category_id: int, input: AccessoryTypeInput, session: Session
) -> AccessoryType:
    category = session.get(AccessoryCategory, category_id)
    if not category:
        raise HTTPException(status_code=404, detail=f"Accessory category {category_id} not found")
    name = input.name.strip()
    if not name:
        raise HTTPException(status_code=422, detail="Accessory type name cannot be empty")
    accessory_type = AccessoryType(name=name, category_id=category_id)
    session.add(accessory_type)
    session.commit()
    session.refresh(accessory_type)
    return accessory_type


def read_accessory_products(accessory_type_id: int, session: Session) -> list[BikeProduct]:
    accessory_type = session.get(AccessoryType, accessory_type_id)
    if not accessory_type:
        raise HTTPException(status_code=404, detail=f"Accessory type {accessory_type_id} not found")
    return list(accessory_type.bikeproducts)


def create_accessory_product(
    accessory_type_id: int, input: BikeProductInput, session: Session
) -> BikeProduct:
    accessory_type = session.get(AccessoryType, accessory_type_id)
    if not accessory_type:
        raise HTTPException(status_code=404, detail=f"Accessory type {accessory_type_id} not found")
    product = BikeProduct.model_validate(input)
    accessory_type.bikeproducts.append(product)
    session.add(accessory_type)
    session.commit()
    session.refresh(product)
    return product

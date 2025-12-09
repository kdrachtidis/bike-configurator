from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.bikepart import BikePart
from src.models.bikeproduct import BikeProduct, BikeProductInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "bike product"

# Create


def create_bikeproduct(bikepart_id: int, input: BikeProductInput, session: SessionDependency) -> BikeProduct:
    # Get the bike part to assign the product to
    bikepart = session.get(BikePart, bikepart_id)
    if bikepart:  # If the bike part exists
        bikeproduct = BikeProduct.model_validate(
            input)  # Create bike product from input
        # Assign bike product to bike part
        bikepart.bikeproducts.append(bikeproduct)
        session.commit()  # Commit to the database
        session.refresh(bikeproduct)  # Refresh to get the generated ID
        log_print("create", obj_type=msg_object_type)  # Log creation
        return bikeproduct  # Return the created bike product
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("product", obj_id=bikepart_id)
        )

# Read


def read_all_bikeproducts(source: str | None = None,
                          session: Session = Depends(get_session)) -> list:
    query = select(BikeProduct)
    if source:
        query = query.where(BikeProduct.source == source)
    log_print("read_all", obj_type=msg_object_type)
    return session.exec(query).all()


def read_bikeproduct(part_id: int, product_id: int, session: SessionDependency) -> BikeProduct:
    # First check if bike part exists
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )
    
    # Then get the bike product
    bikeproduct = session.get(BikeProduct, product_id)
    if not bikeproduct:
        raise HTTPException(
            status_code=404, detail=log_exception("product", obj_id=product_id)
        )
    
    # Verify that the bike product belongs to the specified bike part
    if bikeproduct not in bikepart.bikeproducts:
        raise HTTPException(
            status_code=404, detail=f"Bike product {product_id} not found in bike part {part_id}"
        )
    
    log_print("read", obj_id=product_id, obj_type=msg_object_type)
    return bikeproduct

    # Update


def update_bikeproduct(part_id: int, product_id: int, new_data: BikeProductInput, session: SessionDependency) -> BikeProduct:
    # First check if bike part exists
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )
    
    # Then get the bike product
    bikeproduct = session.get(BikeProduct, product_id)
    if not bikeproduct:
        raise HTTPException(
            status_code=404, detail=log_exception("product", obj_id=product_id)
        )
    
    # Verify that the bike product belongs to the specified bike part
    if bikeproduct not in bikepart.bikeproducts:
        raise HTTPException(
            status_code=404, detail=f"Bike product {product_id} not found in bike part {part_id}"
        )
    
    # Update the bike product
    bikeproduct.name = new_data.name
    bikeproduct.source = new_data.source
    bikeproduct.price = new_data.price
    session.commit()
    session.refresh(bikeproduct)
    log_print("update", obj_id=product_id, obj_type=msg_object_type)
    return bikeproduct

# Delete


def delete_bikeproduct(part_id: int, product_id: int, session: SessionDependency) -> None:
    # First check if bike part exists
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )
    
    # Then get the bike product
    bikeproduct = session.get(BikeProduct, product_id)
    if not bikeproduct:
        raise HTTPException(
            status_code=404, detail=log_exception("product", obj_id=product_id)
        )
    
    # Verify that the bike product belongs to the specified bike part
    if bikeproduct not in bikepart.bikeproducts:
        raise HTTPException(
            status_code=404, detail=f"Bike product {product_id} not found in bike part {part_id}"
        )
    
    # Delete the bike product
    session.delete(bikeproduct)
    session.commit()
    log_print("delete", obj_id=product_id, obj_type=msg_object_type)

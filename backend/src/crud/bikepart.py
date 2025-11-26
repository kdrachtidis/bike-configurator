from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart, BikePartInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "bike part"

# Read a bike part


def read_bikepart(id: int, session: SessionDependency) -> BikePart:
    bikepart = session.get(BikePart, id)
    if bikepart:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return bikepart
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=id))


# Read bike parts by hierarchy


def read_bikeparts_by_hierarchy(biketype_id: int, bikecomponent_id: int, session: SessionDependency) -> list:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if bike component exists
    bikecomponent = session.get(BikeComponent, bikecomponent_id)
    if not bikecomponent:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    # Return bike parts for this bike component
    log_print("read_by_hierarchy", group_id=bikecomponent_id,
              obj_type=msg_object_type)
    return bikecomponent.bikeparts


# Create an bike part by hierarchy


def create_bikepart_by_hierarchy(biketype_id: int, bikecomponent_id: int, input: BikePartInput, session: SessionDependency) -> BikePart:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if bike component exists
    bikecomponent = session.get(BikeComponent, bikecomponent_id)
    if not bikecomponent:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    # Create the bike part
    bikepart = BikePart.model_validate(input)
    bikecomponent.bikeparts.append(bikepart)
    session.commit()
    session.refresh(bikepart)
    log_print("create", obj_type=msg_object_type)
    return bikepart


# Read an bike part by hierarchy


def read_bikepart_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, session: SessionDependency) -> BikePart:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if bike component exists
    bikecomponent = session.get(BikeComponent, bikecomponent_id)
    if not bikecomponent:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    # Then get the bike part
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )

    # Verify that the bike part belongs to the specified bike component
    if bikepart not in bikecomponent.bikeparts:
        raise HTTPException(
            status_code=404, detail=f"Bike part {part_id} not found in bike component {bikecomponent_id}"
        )

    log_print("read", obj_id=part_id, obj_type=msg_object_type)
    return bikepart

# Update bike part by hierarchy


def update_bikepart_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, input: BikePartInput, session: SessionDependency) -> BikePart:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if bike component exists
    bikecomponent = session.get(BikeComponent, bikecomponent_id)
    if not bikecomponent:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    # Then get the bike part
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )

    # Verify that the part belongs to the specified bike component
    if bikepart not in bikecomponent.bikeparts:
        raise HTTPException(
            status_code=404, detail=f"Bike part {part_id} not found in bike component {bikecomponent_id}"
        )

    # Update the bike part
    bikepart.name = input.name
    session.commit()
    log_print("update", obj_id=part_id, obj_type=msg_object_type)
    return bikepart

# Delete bike part by hierarchy


def delete_bikepart_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, session: SessionDependency) -> None:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if bike component exists
    bikecomponent = session.get(BikeComponent, bikecomponent_id)
    if not bikecomponent:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    # Then get the bike part
    bikepart = session.get(BikePart, part_id)
    if not bikepart:
        raise HTTPException(
            status_code=404, detail=log_exception("part", obj_id=part_id)
        )

    # Verify that the bike part belongs to the specified bike component
    if bikepart not in bikecomponent.bikeparts:
        raise HTTPException(
            status_code=404, detail=f"Bike part {part_id} not found in bike component {bikecomponent_id}"
        )

    # Delete the bike part
    session.delete(bikepart)
    session.commit()
    log_print("delete", obj_id=part_id, obj_type=msg_object_type)

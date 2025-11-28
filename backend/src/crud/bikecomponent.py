from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent, BikeComponentInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "bike component"

# Read an bike component by ID


def read_bikecomponent(bikecomponent_id: int, session: SessionDependency) -> BikeComponent:
    bikecomponent = session.get(
        BikeComponent, bikecomponent_id)  # Get the bike component
    if bikecomponent:  # If bike component exists
        # Log the read action
        log_print("read", obj_id=bikecomponent_id, obj_type=msg_object_type)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id))

# Read all bike components under a bike type


def read_all_bikecomponents_by_biketype(biketype_id: int, session: SessionDependency) -> list:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Return bike components for this bike type
    log_print("read_all", obj_type=msg_object_type, obj_id=biketype_id)
    return biketype.bikecomponents

# Create a bike component under a bike type


def create_bikecomponent(biketype_id: int, input: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if biketype:  # If bike type exists
        bikecomponent = BikeComponent.model_validate(
            input)  # Create bike component from input
        # Append bike component to bike type
        biketype.bikecomponents.append(bikecomponent)
        session.commit()  # Commit the changes
        session.refresh(bikecomponent)  # Refresh the bike component instance
        log_print("create", obj_type=msg_object_type)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

# Read an bike component by bike type


def read_bikecomponent_by_biketype(biketype_id: int, bikecomponent_id: int, session: SessionDependency) -> BikeComponent:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the bike component
    bikecomponent = session.get(
        BikeComponent, bikecomponent_id)  # Get the bike component
    if not bikecomponent:  # If bike component does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:  # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent_id} not found in bike type {biketype_id}"
        )

    log_print("read", obj_id=bikecomponent.id, obj_type=msg_object_type)
    return bikecomponent


# Update a bike component by bike type


def update_bikecomponent_by_biketype(biketype_id: int, bikecomponent_id: int, input: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the bike component
    bikecomponent = session.get(
        BikeComponent, bikecomponent_id)  # Get the bike component
    if not bikecomponent:  # If bike component does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:  # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent.id} not found in bike type {biketype_id}"
        )

    # Update the bike component
    bikecomponent.name = input.name  # Update other fields as necessary
    session.commit()  # Commit the changes
    session.refresh(bikecomponent)  # Refresh the bike component instance
    log_print("update", obj_id=bikecomponent.id, obj_type=msg_object_type)
    return bikecomponent  # Return the updated bike component


# Delete a bike component by bike type

def delete_bikecomponent_by_biketype(biketype_id: int, bikecomponent_id: int, session: SessionDependency) -> None:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the bike component
    bikecomponent = session.get(
        BikeComponent, bikecomponent_id)  # Get the bike component
    if not bikecomponent:  # If bike component does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=bikecomponent_id)
        )

    # Verify that the bike component belongs to the specified bike type
    if bikecomponent not in biketype.bikecomponents:  # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Bike component {bikecomponent.id} not found in bike type {biketype_id}"
        )

    session.delete(bikecomponent)  # Delete the bike component
    session.commit()  # Commit the changes
    log_print("delete", obj_id=bikecomponent_id, obj_type=msg_object_type)

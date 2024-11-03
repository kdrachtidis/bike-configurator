from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import BikeType, BikeTypeOutput, BikeTypeInput, User

router = APIRouter(prefix="/api/biketypes")

# Reusable components

custom_tags = "Bike types"
custom_description_post = "Add a bike type."
custom_description_get = "Get the list of all bike types."
custom_description_get_id = "Get a specific bike type based on its ID."
custom_description_delete = "Remove a specific bike type based on its ID."
custom_description_put = "Edit a specific bike type based on its ID."

# Add bike type


@router.post("/", response_model=BikeType, tags=[custom_tags], description=custom_description_post)
def add_bike_type(component_input: BikeTypeInput, session: Session = Depends(get_session)) -> BikeType:
    new_type = BikeType.model_validate(component_input)
    session.add(new_type)
    session.commit()
    session.refresh(new_type)
    return new_type


# Get bike types

@router.get("/", tags=[custom_tags], description=custom_description_get)
def get_bike_types(session: Session = Depends(get_session)) -> list:
    query = select(BikeType)
    return session.exec(query).all()

# Get bike type by id


@router.get("/{id}", response_model=BikeTypeOutput, tags=[custom_tags], description=custom_description_get_id)
def bike_type_by_id(id: int, session: Session = Depends(get_session)) -> BikeType:
    bike_type = session.get(BikeType, id)
    if bike_type:
        return bike_type
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike type with id={id}.")

# Edit a biketype


@router.put("/{id}", response_model=BikeType, tags=[custom_tags], description=custom_description_put)
def edit_bike_type(id: int, new_data: BikeTypeInput, session: Session = Depends(get_session)) -> BikeType:
    biketype = session.get(BikeType, id)

    if biketype:
        biketype.name = new_data.name
        session.commit()
        return biketype
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike type with id={id}.")

# Delete a bike type


@router.delete("/{id}", status_code=204, tags=[custom_tags], description=custom_description_delete)
def remove_bike_type(id: int, session: Session = Depends(get_session)) -> None:
    bike_type = session.get(BikeType, id)
    if bike_type:
        session.delete(bike_type)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike type with id={id}.")

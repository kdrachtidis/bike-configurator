from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from api.auth.models import User
from api.public.biketype.models import BikeType, BikeTypeOutput, BikeTypeInput

router = APIRouter(prefix="/biketypes")
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components

msg_tags = "Bike Type"
msg_tags_id = "Bike Type (by ID)"
msg_description_post = "Add a bike type."
msg_description_get = "Get the list of all bike types."
msg_description_get_id = "Get a specific bike type based on its ID."
msg_description_delete = "Remove a specific bike type based on its ID."
msg_description_put = "Edit a specific bike type based on its ID."


def msg_no_item(i):
    return f"No bike type with id={i}."

# Add bike type


@router.post("/", response_model=BikeType, tags=[msg_tags], description=msg_description_post, status_code=status.HTTP_201_CREATED)
def add_bike_type(input: BikeTypeInput, session: SessionDep, user: User = Depends(get_current_user)) -> BikeType:
    new_type = BikeType.model_validate(input)
    session.add(new_type)
    session.commit()
    session.refresh(new_type)
    return new_type


# Get bike types

@router.get("/", tags=[msg_tags], description=msg_description_get)
def get_bike_types(session: SessionDep) -> list:
    query = select(BikeType)
    return session.exec(query).all()

# Get bike type by id


@router.get("/{id}", response_model=BikeTypeOutput, tags=[msg_tags_id], description=msg_description_get_id)
def bike_type_by_id(id: int, session: SessionDep) -> BikeType:
    biketype = session.get(BikeType, id)
    if biketype:
        return biketype
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Edit a biketype


@router.put("/{id}", response_model=BikeType, tags=[msg_tags_id], description=msg_description_put)
def edit_bike_type(id: int, new_data: BikeTypeInput, session: SessionDep, user: User = Depends(get_current_user)) -> BikeType:
    biketype = session.get(BikeType, id)

    if biketype:
        biketype.name = new_data.name
        session.commit()
        return biketype
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Delete a bike type


@router.delete("/{id}", status_code=204, tags=[msg_tags_id], description=msg_description_delete)
def remove_bike_type(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    biketype = session.get(BikeType, id)
    if biketype:
        session.delete(biketype)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

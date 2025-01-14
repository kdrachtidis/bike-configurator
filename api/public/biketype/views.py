from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from api.auth.views import get_current_user
from api.utils.db import get_session
from api.auth.models import User
from api.public.biketype.crud import create_biketype, read_all_biketypes, read_biketype, update_biketype, delete_biketype
from api.public.biketype.models import BikeType, BikeTypeOutput, BikeTypeInput

router = APIRouter(prefix="/biketypes")
SessionDep = Annotated[Session, Depends(get_session)]

# Swagger UI's descriptions
msg_tags = "Bike Type"
msg_description_create = "Add a bike type."
msg_description_read_all = "Get the list of all bike types."
msg_description_read = "Get a specific bike type based on its ID."
msg_description_delete = "Remove a specific bike type based on its ID."
msg_description_update = "Edit a specific bike type based on its ID."

# Create a bike type


@router.post("/", response_model=BikeType, tags=[msg_tags], description=msg_description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_type(input: BikeTypeInput, session: SessionDep, user: User = Depends(get_current_user)) -> BikeType:
    return create_biketype(input=input, session=session)


# Read all bike types

@router.get("/", tags=[msg_tags], description=msg_description_read_all)
def read_all_bike_types(session: SessionDep) -> list:
    return read_all_biketypes(session=session)

# Read a bike type


@router.get("/{id}", response_model=BikeTypeOutput, tags=[msg_tags], description=msg_description_read)
def read_a_bike_type(id: int, session: SessionDep) -> BikeType:
    return read_biketype(id=id, session=session)

# Edit a biketype


@router.put("/{id}", response_model=BikeType, tags=[msg_tags], description=msg_description_update)
def update_a_bike_type(id: int, new_data: BikeTypeInput, session: SessionDep, user: User = Depends(get_current_user)) -> BikeType:
    return update_biketype(id=id, input=new_data, session=session)

# Delete a bike type


@router.delete("/{id}", status_code=204, tags=[msg_tags], description=msg_description_delete)
def delete_a_bike_type(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    return delete_biketype(id=id, session=session)

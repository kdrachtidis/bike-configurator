from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikeTypeMessages
from src.models.user import User
from src.crud.biketype import create_biketype, read_all_biketypes, read_biketype, update_biketype, delete_biketype
from src.models.biketype import BikeType, BikeTypeOutput, BikeTypeInput

router = APIRouter(prefix="/biketypes")
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikeTypeMessages()

# Create a bike type


@router.post("/", response_model=BikeType, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_type(input: BikeTypeInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeType:
    return create_biketype(input=input, session=session)


# Read all bike types

@router.get("/", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_bike_types(session: SessionDependency) -> list:
    return read_all_biketypes(session=session)

# Read a bike type


@router.get("/{type_id}", response_model=BikeTypeOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_a_bike_type(type_id: int, session: SessionDependency) -> BikeType:
    return read_biketype(biketype_id=type_id, session=session)

# Edit a biketype


@router.put("/{type_id}", response_model=BikeType, tags=[swagger_desc.tags], description=swagger_desc.description_update)
def update_a_bike_type(type_id: int, new_data: BikeTypeInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeType:
    return update_biketype(biketype_id=type_id, input=new_data, session=session)

# Delete a bike type


@router.delete("/{type_id}", status_code=204, tags=[swagger_desc.tags], description=swagger_desc.description_delete)
def delete_a_bike_type(type_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_biketype(biketype_id=type_id, session=session)

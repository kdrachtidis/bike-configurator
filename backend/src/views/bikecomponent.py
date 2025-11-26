from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikeComponentsMessages
from src.models.user import User
from src.crud.bikecomponent import create_bikecomponent, read_all_bikecomponents_by_biketype, read_bikecomponent, read_bikecomponent_by_biketype, update_bikecomponent_by_biketype, delete_bikecomponent_by_biketype
from src.models.bikecomponent import BikeComponent, BikeComponentInput, BikeComponentOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikeComponentsMessages()


# Read a bike component


@router.get("/bikecomponents/{component_id}", response_model=BikeComponentOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_a_bike_component(component_id: int, session: SessionDependency) -> BikeComponent:
    return read_bikecomponent(bikecomponent_id=component_id, session=session)


# Read all bike components by hierarchy


@router.get("/biketypes/{type_id}/bikecomponents", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_bike_components_by_biketype(type_id: int, session: SessionDependency) -> list:
    return read_all_bikecomponents_by_biketype(biketype_id=type_id, session=session)


# Create a bike component


@router.post("/biketypes/{type_id}/bikecomponents/", response_model=BikeComponent, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_component(type_id: int, input: BikeComponentInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return create_bikecomponent(bikecomponent_id=type_id, input=input, session=session)


# Read a bike component by hierarchy


@router.get("/biketypes/{type_id}/bikecomponents/{component_id}", response_model=BikeComponentOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read, status_code=status.HTTP_200_OK)
def read_bike_component_by_biketype(type_id: int, component_id: int, session: SessionDependency) -> BikeComponent:
    return read_bikecomponent_by_biketype(biketype_id=type_id, bikecomponent_id=component_id, session=session)


# Update a bike component by hierarchy


@router.put("/biketypes/{type_id}/bikecomponents/{component_id}", response_model=BikeComponent, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_bike_component_by_biketype(type_id: int, component_id: int, new_bikecomponent: BikeComponentInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return update_bikecomponent_by_biketype(biketype_id=type_id, bikecomponent_id=component_id, input=new_bikecomponent, session=session)


# Delete a bike component by hierarchy


@router.delete("/biketypes/{type_id}/bikecomponents/{component_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_bike_component_by_biketype(type_id: int, component_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikecomponent_by_biketype(biketype_id=type_id, bikecomponent_id=component_id, session=session)

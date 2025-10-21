from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikeComponentMessages
from src.models.user import User
from src.crud.bikecomponent import create_bikecomponent, read_all_bikecomponents, read_bikecomponent, update_bikecomponent, delete_bikecomponent
from src.models.bikecomponent import BikeComponent, BikeComponentOutput, BikeComponentInput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikeComponentMessages()

# Create a bike component assigned to an assembly group module


@router.post("/assemblygroupmodules/{id}/bikecomponents/", response_model=BikeComponent, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_component(id: int, input: BikeComponentInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return create_bikecomponent(id=id, input=input, session=session)

# Read all bike components


@router.get("/bikecomponents/", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_bike_components(source: str | None = None, group: str | None = None, session: Session = Depends(get_session)) -> list:
    return read_all_bikecomponents(source=source, group=group, session=session)

# Read a bike component


@router.get("/bikecomponents/{id}", response_model=BikeComponentOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_a_bike_component(id: int, session: SessionDependency) -> BikeComponent:
    return read_bikecomponent(id=id, session=session)

# Update a bike component


@router.put("/bikecomponents/{id}", response_model=BikeComponent, tags=[swagger_desc.tags], description=swagger_desc.description_update)
def update_a_bike_component(id: int, new_data: BikeComponentInput,
                            session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return update_bikecomponent(id=id, new_data=new_data, session=session)

# Delete a bike component


@router.delete("/bikecomponents/{id}", status_code=204, tags=[swagger_desc.tags], description=swagger_desc.description_delete)
def delete_a_bike_component(id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikecomponent(id=id, session=session)

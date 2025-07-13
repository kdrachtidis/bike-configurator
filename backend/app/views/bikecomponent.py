from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from app.views.user import get_current_user
from app.utils.database import get_session
from app.models.user import User
from app.crud.bikecomponent import create_bikecomponent, read_all_bikecomponents, read_bikecomponent, update_bikecomponent, delete_bikecomponent
from app.models.bikecomponent import BikeComponent, BikeComponentOutput, BikeComponentInput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]

# Swagger UI's descriptions
msg_tags = "Bike Component"
msg_description_post = "Add a bike component."
msg_description_get = "Get the list of all bike components."
msg_description_get_id = "Get a specific bike component based on its ID."
msg_description_delete = "Remove a specific bike component based on its ID."
msg_description_put = "Edit a specific bike component based on its ID."

# Create a bike component assigned to an assembly group module


@router.post("/assemblygroupmodules/{id}/bikecomponents/", response_model=BikeComponent, tags=[msg_tags], description=msg_description_post, status_code=status.HTTP_201_CREATED)
def create_a_bike_component(id: int, input: BikeComponentInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return create_bikecomponent(id=id, input=input, session=session)

# Read all bike components


@router.get("/bikecomponents/", tags=[msg_tags], description=msg_description_get)
def read_all_bike_components(source: str | None = None, group: str | None = None, session: Session = Depends(get_session)) -> list:
    return read_all_bikecomponents(source=source, group=group, session=session)

# Read a bike component


@router.get("/bikecomponents/{id}", response_model=BikeComponentOutput, tags=[msg_tags], description=msg_description_get_id)
def read_a_bike_component(id: int, session: SessionDependency) -> BikeComponent:
    return read_bikecomponent(id=id, session=session)

# Update a bike component


@router.put("/bikecomponents/{id}", response_model=BikeComponent, tags=[msg_tags], description=msg_description_put)
def update_a_bike_component(id: int, new_data: BikeComponentInput,
                        session: SessionDependency, user: User = Depends(get_current_user)) -> BikeComponent:
    return update_bikecomponent(id=id, new_data=new_data, session=session)

# Delete a bike component


@router.delete("/bikecomponents/{id}", status_code=204, tags=[msg_tags], description=msg_description_delete)
def delete_a_bike_component(id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikecomponent(id=id, session=session)

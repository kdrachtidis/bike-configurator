from typing import Annotated

from fastapi import Depends, APIRouter, status, HTTPException
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikePartsMessages
from src.models.user import User
from src.crud.bikepart import create_bikepart, read_bikeparts, read_all_bikeparts, read_bikepart, update_bikepart, delete_bikepart
from src.models.bikepart import BikePart, BikePartInput, BikePartOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikePartsMessages()


# Read a bike part


@router.get("/bikeparts", response_model=list[BikePartOutput], tags=[swagger_desc.tags], description=swagger_desc.description_get_component_id, status_code=status.HTTP_200_OK)
def get_all_bike_parts(session: SessionDependency) -> list[BikePart]:
    return read_all_bikeparts(session=session)


# Read bike parts by hierarchy


@router.get("/biketypes/{type_id}/bikecomponents/{component_id}/bikeparts", response_model=list[BikePartOutput], tags=[swagger_desc.tags], description=swagger_desc.description_read_all, status_code=status.HTTP_200_OK)
def get_bike_parts(type_id: int, component_id: int, session: SessionDependency) -> list[BikePart]:
    return read_bikeparts(biketype_id=type_id, bikecomponent_id=component_id, session=session)

# Create a bike part by hierarchy


@router.post("/biketypes/{type_id}/bikecomponents/{component_id}/bikeparts/", response_model=BikePart, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def post_bike_part(type_id: int, component_id: int, input: BikePartInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikePart:
    return create_bikepart(biketype_id=type_id, bikecomponent_id=component_id, input=input, session=session)


# Read a bike part by hierarchy


@router.get("/biketypes/{type_id}/bikecomponents/{component_id}/bikeparts/{part_id}", response_model=BikePartOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_component_id, status_code=status.HTTP_200_OK)
def get_bike_part(type_id: int, component_id: int, part_id: int, session: SessionDependency) -> BikePart:
    return read_bikepart(biketype_id=type_id, bikecomponent_id=component_id, bikepart_id=part_id, session=session)


# Update bike part by hierarchy


@router.put("/biketypes/{type_id}/bikecomponents/{component_id}/bikeparts/{part_id}", response_model=BikePart, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def put_bike_part(type_id: int, component_id: int, part_id: int, input: BikePartInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikePart:
    return update_bikepart(biketype_id=type_id, bikecomponent_id=component_id, bikepart_id=part_id, input=input, session=session)


# Delete a bike part by hierarchy


@router.delete("/biketypes/{type_id}/bikecomponents/{component_id}/bikeparts/{part_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_204_NO_CONTENT)
def delete_bike_part(type_id: int, component_id: int, part_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikepart(biketype_id=type_id, bikecomponent_id=component_id, bikepart_id=part_id, session=session)

from typing import Annotated

from fastapi import Depends, APIRouter, status, HTTPException
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikePartsMessages
from src.models.user import User
from src.crud.bikepart import create_bikepart_by_hierarchy, read_bikeparts_by_hierarchy, read_bikepart, read_bikepart_by_hierarchy, update_bikepart_by_hierarchy, delete_bikepart_by_hierarchy
from src.models.bikepart import BikePart, BikePartInput, BikePartOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikePartsMessages()


# Read a bike part


@router.get("/bikeparts/{part_id}", response_model=BikePartOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id)
def read_a_bike_part(part_id: int, session: SessionDependency) -> BikePart:
    return read_bikepart(id=part_id, session=session)


# Read bike parts by hierarchy


@router.get("/biketypes/{biketype_id}/bikecomponents/{bikecomponent_id}/bikeparts", response_model=list[BikePartOutput], tags=[swagger_desc.tags], description="Read all bike parts within the hierarchy")
def read_bike_parts_by_hierarchy(biketype_id: int, bikecomponent_id: int, session: SessionDependency) -> list[BikePart]:
    return read_bikeparts_by_hierarchy(biketype_id=biketype_id, bikecomponent_id=bikecomponent_id, session=session)

# Create a bike part by hierarchy


@router.post("/biketypes/{biketype_id}/bikecomponents/{bikecomponent_id}/bikeparts/", response_model=BikePart, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_part_by_hierarchy(biketype_id: int, bikecomponent_id: int, input: BikePartInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikePart:
    return create_bikepart_by_hierarchy(biketype_id=biketype_id, bikecomponent_id=bikecomponent_id, input=input, session=session)


# Read a bike part by hierarchy


@router.get("/biketypes/{biketype_id}/bikecomponents/{bikecomponent_id}/bikeparts/{part_id}", response_model=BikePartOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id, status_code=status.HTTP_200_OK)
def read_bike_part_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, session: SessionDependency) -> BikePart:
    return read_bikepart_by_hierarchy(biketype_id=biketype_id, bikecomponent_id=bikecomponent_id, part_id=part_id, session=session)


# Update bike part by hierarchy


@router.put("/biketypes/{biketype_id}/bikecomponents/{bikecomponent_id}/bikeparts/{part_id}", response_model=BikePart, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_bike_part_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, input: BikePartInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikePart:
    return update_bikepart_by_hierarchy(biketype_id=biketype_id, bikecomponent_id=bikecomponent_id, part_id=part_id, input=input, session=session)


# Delete bike part by hierarchy


@router.delete("/biketypes/{biketype_id}/bikecomponents/{bikecomponent_id}/bikeparts/{part_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_bike_part_by_hierarchy(biketype_id: int, bikecomponent_id: int, part_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikepart_by_hierarchy(biketype_id=biketype_id, bikecomponent_id=bikecomponent_id, part_id=part_id, session=session)

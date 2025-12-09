from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import BikeProductsMessages
from src.models.user import User
from src.crud.bikeproduct import create_bikeproduct, read_all_bikeproducts, read_bikeproduct, update_bikeproduct, delete_bikeproduct
from src.models.bikeproduct import BikeProduct, BikeProductOutput, BikeProductInput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = BikeProductsMessages()


# Read all bike products


@router.get("/bikeproducts/", tags=[swagger_desc.tags], description=swagger_desc.description_read_all, response_model=list[BikeProductOutput], status_code=status.HTTP_200_OK)
def get_bike_products(source: str | None = None, session: Session = Depends(get_session)) -> list:
    return read_all_bikeproducts(source=source, session=session)

# Create a bike product assigned to a bike part


@router.post("/bikeparts/{part_id}/bikeproducts/", response_model=BikeProduct, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def post_bike_product(part_id: int, input: BikeProductInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeProduct:
    return create_bikeproduct(bikepart_id=part_id, input=input, session=session)

# Read a bike product


@router.get("/bikeparts/{part_id}/bikeproducts/{product_id}", response_model=BikeProductOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read, status_code=status.HTTP_200_OK)
def get_bike_product(part_id: int, product_id: int, session: SessionDependency) -> BikeProduct:
    return read_bikeproduct(part_id=part_id, product_id=product_id, session=session)

# Update a bike product


@router.put("/bikeparts/{part_id}/bikeproducts/{product_id}", response_model=BikeProduct, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def put_bike_product(part_id: int, product_id: int, new_data: BikeProductInput,
                     session: SessionDependency, user: User = Depends(get_current_user)) -> BikeProduct:
    return update_bikeproduct(part_id=part_id, product_id=product_id, new_data=new_data, session=session)

# Delete a bike product


@router.delete("/bikeparts/{part_id}/bikeproducts/{product_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_204_NO_CONTENT)
def delete_bike_product(part_id: int, product_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikeproduct(part_id=part_id, product_id=product_id, session=session)

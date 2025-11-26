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

# Create a bike product assigned to a bike part


@router.post("/bikeparts/{part_id}/bikeproducts/", response_model=BikeProduct, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_a_bike_product(part_id: int, input: BikeProductInput, session: SessionDependency, user: User = Depends(get_current_user)) -> BikeProduct:
    return create_bikeproduct(bikepart_id=part_id, input=input, session=session)

# Read all bike products


@router.get("/bikeproducts/", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_bike_products(source: str | None = None, group: str | None = None, session: Session = Depends(get_session)) -> list:
    return read_all_bikeproducts(source=source, group=group, session=session)

# Read a bike product


@router.get("/bikeproducts/{product_id}", response_model=BikeProductOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_a_bike_product(product_id: int, session: SessionDependency) -> BikeProduct:
    return read_bikeproduct(bikeproduct_id=product_id, session=session)

# Update a bike product


@router.put("/bikeproducts/{product_id}", response_model=BikeProduct, tags=[swagger_desc.tags], description=swagger_desc.description_update)
def update_a_bike_product(product_id: int, new_data: BikeProductInput,
                          session: SessionDependency, user: User = Depends(get_current_user)) -> BikeProduct:
    return update_bikeproduct(bikeproduct_id=product_id, new_data=new_data, session=session)

# Delete a bike product


@router.delete("/bikeproducts/{product_id}", status_code=204, tags=[swagger_desc.tags], description=swagger_desc.description_delete)
def delete_a_bike_product(product_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_bikeproduct(bikeproduct_id=product_id, session=session)

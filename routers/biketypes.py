from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import BikeType, BikeTypeOutput, BikeTypeInput

router = APIRouter(prefix="/api/biketypes")

# Add bike type

@router.post("/", response_model=BikeType, tags=["Bike Type"], description="Add a bike type.")
def add_bike_type(component_input: BikeTypeInput, session: Session = Depends(get_session)) -> BikeType:
    new_type = BikeType.model_validate(component_input)
    session.add(new_type)
    session.commit()
    session.refresh(new_type)
    return new_type
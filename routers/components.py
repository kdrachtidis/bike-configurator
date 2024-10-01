from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import BikeComponent, BikeComponentOutput, BikeComponentInput, User

router = APIRouter(prefix="/api/bikecomponents")

# Add bike component


@router.post("/", response_model=BikeComponent, tags=["Bike components"])
def add_bike_component(component_input: BikeComponentInput,
                       session: Session = Depends(get_session)) -> BikeComponent:
    # user: User = Depends(get_current_user)) -> BikeComponent:
    new_component = BikeComponent.model_validate(component_input)
    session.add(new_component)
    session.commit()
    session.refresh(new_component)
    return new_component

# Get bike components


@router.get("/", tags=["Bike components"])
def get_bike_components(source: str | None = None, group: str | None = None,
                        session: Session = Depends(get_session)) -> list:
    query = select(BikeComponent)
    if source:
        query = query.where(BikeComponent.source == source)
    if group:
        query = query.where(BikeComponent.group == group)
    return session.exec(query).all()

# Get bike component by id


@router.get("/{id}", response_model=BikeComponentOutput, tags=["Bike components"])
def bike_component_by_id(id: int, session: Session = Depends(get_session)) -> BikeComponent:
    component = session.get(BikeComponent, id)
    if component:
        return component
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike component with id={id}.")


# Delete a bike component


@router.delete("/{id}", status_code=204, tags=["Bike components"])
def remove_bike_component(id: int, session: Session = Depends(get_session)) -> None:
    component = session.get(BikeComponent, id)
    if component:
        session.delete(component)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No bike component with id={id}.")

# Edit a bike component


@router.put("/{id}", response_model=BikeComponent, tags=["Bike components"])
def edit_bike_component(id: int, new_data: BikeComponentInput,
                        session: Session = Depends(get_session)) -> BikeComponent:
    component = session.get(BikeComponent, id)
    if component:
        component.name = new_data.name
        component.source = new_data.source
        component.price = new_data.price
        component.group = new_data.group
        session.commit()
        return component
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

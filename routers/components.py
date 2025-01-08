from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import User
from api.public.bikecomponent.models import BikeComponent, BikeComponentOutput, BikeComponentInput

router = APIRouter(prefix="/api/bikecomponents")
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components

msg_tags = "Bike Component"
msg_tags_id = "Bike Component (by ID)"
msg_description_post = "Add a bike component."
msg_description_get = "Get the list of all bike components."
msg_description_get_id = "Get a specific bike component based on its ID."
msg_description_delete = "Remove a specific bike component based on its ID."
msg_description_put = "Edit a specific bike component based on its ID."


def msg_no_item(i):
    return f"No bike component with id={i}."

# Add bike component


@router.post("/", response_model=BikeComponent, tags=[msg_tags], description=msg_description_post)
def add_bike_component(component_input: BikeComponentInput,
                       session: SessionDep, user: User = Depends(get_current_user)) -> BikeComponent:
    new_component = BikeComponent.model_validate(component_input)
    session.add(new_component)
    session.commit()
    session.refresh(new_component)
    return new_component

# Get bike components


@router.get("/", tags=[msg_tags], description=msg_description_get)
def get_bike_components(source: str | None = None, group: str | None = None,
                        session: Session = Depends(get_session)) -> list:
    query = select(BikeComponent)
    if source:
        query = query.where(BikeComponent.source == source)
    if group:
        query = query.where(BikeComponent.group == group)
    return session.exec(query).all()

# Get bike component by id


@router.get("/{id}", response_model=BikeComponentOutput, tags=[msg_tags_id], description=msg_description_get_id)
def bike_component_by_id(id: int, session: SessionDep) -> BikeComponent:
    component = session.get(BikeComponent, id)
    if component:
        return component
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))


# Delete a bike component


@router.delete("/{id}", status_code=204, tags=[msg_tags_id], description=msg_description_delete)
def remove_bike_component(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    component = session.get(BikeComponent, id)
    if component:
        session.delete(component)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Edit a bike component


@router.put("/{id}", response_model=BikeComponent, tags=[msg_tags_id], description=msg_description_put)
def edit_bike_component(id: int, new_data: BikeComponentInput,
                        session: SessionDep, user: User = Depends(get_current_user)) -> BikeComponent:
    component = session.get(BikeComponent, id)
    if component:
        component.name = new_data.name
        component.source = new_data.source
        component.price = new_data.price
        component.group = new_data.group
        session.commit()
        return component
    else:
        raise HTTPException(status_code=404, detail=msg_no_item(id))

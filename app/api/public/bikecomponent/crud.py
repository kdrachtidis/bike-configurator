from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.api.utils.db import get_session
from app.api.public.assemblygroupmodule.models import AssemblyGroupModule
from app.api.public.bikecomponent.models import BikeComponent, BikeComponentInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_init = "Bike Configurator API"  # API logs identifier
msg_create = ": Create bike component."
msg_read_all = ": Read all bike components."
msg_read = ": Read bike component with id ="
msg_update = ": Update bike component with id ="
msg_delete = ": Delete bike component with id ="

# HTTPException details messages


def msg_no_module(i):
    return f"No assembly group module with id={i}."


def msg_no_item(i):
    return f"No bike component with id={i}."

# Create


def create_bikecomponent(id: int, input: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        bikecomponent = BikeComponent.model_validate(input)
        assemblygroupmodule.bikecomponents.append(bikecomponent)
        session.commit()
        session.refresh(bikecomponent)
        print(msg_init, end="")
        print(msg_create)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id)
        )

# Read


def read_all_bikecomponents(source: str | None = None, group: str | None = None,
                            session: Session = Depends(get_session)) -> list:
    query = select(BikeComponent)
    if source:
        query = query.where(BikeComponent.source == source)
    if group:
        query = query.where(BikeComponent.group == group)
    print(msg_init, end="")
    print(msg_read_all)
    return session.exec(query).all()


def read_bikecomponent(id: int, session: SessionDependency) -> None:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        print(msg_init, end="")
        print(msg_read, id)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

    # Update


def update_bikecomponent(id: int, new_data: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        bikecomponent.name = new_data.name
        bikecomponent.source = new_data.source
        bikecomponent.price = new_data.price
        bikecomponent.group = new_data.group
        session.commit()
        print(msg_init, end="")
        print(msg_update, id)
        return bikecomponent
    else:
        raise HTTPException(status_code=404, detail=msg_no_item(id))

# Delete


def delete_bikecomponent(id: int, session: SessionDependency) -> None:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        session.delete(bikecomponent)
        session.commit()
        print(msg_init, end="")
        print(msg_delete, id)
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

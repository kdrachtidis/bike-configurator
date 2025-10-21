from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.assemblygroupmodule import AssemblyGroupModule
from src.models.bikecomponent import BikeComponent, BikeComponentInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "bike component"

# Create


def create_bikecomponent(id: int, input: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        bikecomponent = BikeComponent.model_validate(input)
        assemblygroupmodule.bikecomponents.append(bikecomponent)
        session.commit()
        session.refresh(bikecomponent)
        log_print("create", obj_type=msg_object_type)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=id)
        )

# Read


def read_all_bikecomponents(source: str | None = None, group: str | None = None,
                            session: Session = Depends(get_session)) -> list:
    query = select(BikeComponent)
    if source:
        query = query.where(BikeComponent.source == source)
    if group:
        query = query.where(BikeComponent.group == group)
    log_print("read_all", obj_type=msg_object_type)
    return session.exec(query).all()


def read_bikecomponent(id: int, session: SessionDependency) -> None:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=id))

    # Update


def update_bikecomponent(id: int, new_data: BikeComponentInput, session: SessionDependency) -> BikeComponent:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        bikecomponent.name = new_data.name
        bikecomponent.source = new_data.source
        bikecomponent.price = new_data.price
        bikecomponent.group = new_data.group
        session.commit()
        log_print("update", obj_id=id, obj_type=msg_object_type)
        return bikecomponent
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=id))

# Delete


def delete_bikecomponent(id: int, session: SessionDependency) -> None:
    bikecomponent = session.get(BikeComponent, id)
    if bikecomponent:
        session.delete(bikecomponent)
        session.commit()
        log_print("delete", obj_id=id, obj_type=msg_object_type)
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("component", obj_id=id))

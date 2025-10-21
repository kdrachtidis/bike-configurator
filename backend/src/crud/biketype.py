from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.biketype import BikeType, BikeTypeInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "bike type"

# HTTPException details messages


def msg_no_item(i):
    return f"No bike type with id={i}."

# Create


def create_biketype(input: BikeTypeInput, session: SessionDependency) -> BikeType:
    biketype = BikeType.model_validate(input)
    session.add(biketype)
    session.commit()
    session.refresh(biketype)
    log_print("create", obj_type=msg_object_type)
    return biketype

# Read


def read_all_biketypes(session: SessionDependency) -> list:
    query = select(BikeType)
    log_print("read_all", obj_type=msg_object_type)
    return session.exec(query).all()


def read_biketype(id: int, session: SessionDependency) -> BikeType:
    biketype = session.get(BikeType, id)
    if biketype:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return biketype
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Update


def update_biketype(id: int, input: BikeTypeInput, session: SessionDependency) -> BikeType:
    biketype = session.get(BikeType, id)
    if biketype:
        biketype.name = input.name
        session.commit()
        log_print("update", obj_id=id, obj_type=msg_object_type)
        return biketype
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Delete


def delete_biketype(id: int, session: SessionDependency) -> None:
    biketype = session.get(BikeType, id)
    if biketype:
        session.delete(biketype)
        session.commit()
        log_print("delete", obj_id=id, obj_type=msg_object_type)
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

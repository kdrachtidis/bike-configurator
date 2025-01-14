from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from api.utils.db import get_session
from api.public.biketype.models import BikeType, BikeTypeInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_init = "Bike Configurator API"  # API logs identifier
msg_create = ": Create bike type."
msg_read_all = ": Read all bike types."
msg_read = ": Read bike type with id ="
msg_update = ": Update bike type with id ="
msg_delete = ": Delete bike type with id ="

# HTTPException details messages


def msg_no_item(i):
    return f"No bike type with id={i}."

# Create


def create_biketype(input: BikeTypeInput, session: SessionDependency) -> BikeType:
    biketype = BikeType.model_validate(input)
    session.add(biketype)
    session.commit()
    session.refresh(biketype)
    print(msg_init, end="")
    print(msg_create)
    return biketype

# Read


def read_all_biketypes(session: SessionDependency) -> list:
    query = select(BikeType)
    print(msg_init, end="")
    print(msg_read_all)
    return session.exec(query).all()


def read_biketype(id: int, session: SessionDependency) -> BikeType:
    biketype = session.get(BikeType, id)
    if biketype:
        print(msg_init, end="")
        print(msg_read, id)
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
        print(msg_init, end="")
        print(msg_update, id)
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
        print(msg_init, end="")
        print(msg_delete, id)
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))
